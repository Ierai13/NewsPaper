from datetime import datetime

from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.utils import timezone

from .filters import PostFilter
from .forms import PostForm
from .models import Post, UserCategory, Category, Author


# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-time'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context


class PostSearch(PostList):
    ordering = '-time'
    template_name = 'search.html'
    context_object_name = 'search'
    paginate_by = 3


class PostDetail(DetailView):
    model = Post
    template_name = 'newss.html'
    context_object_name = 'newss'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_category = []
        for i in User.objects.filter(id=self.request.user.id).values('usercategory__category__name'):
            user_category.append(i.get('usercategory__category__name'))
        context['user_category'] = user_category
        return context


class PostCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('_accounts.add_post')
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post._type = 'news'
        post.author_id = self.request.user.author.id
        stop_time = datetime.now(tz=timezone.utc)-timedelta(1)
        result = Post.objects.filter(author=self.request.user.author.id, time__gte=stop_time).count() <= 3
        if result:
            return super().form_valid(form)
        else:
            return HttpResponseBadRequest('Вы можете публиковать не более трех сообщений в сутки')



class PostCreatePost(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('_accounts.add_post')
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post._type = 'post'
        post.author_id = self.request.user.author.id
        stop_time = datetime.now(tz=timezone.utc)-timedelta(1)
        result = Post.objects.filter(author=self.request.user.author.id, time__gte=stop_time).count() <= 3
        if result:
            return super().form_valid(form)
        else:
            return HttpResponseBadRequest('Вы можете публиковать не более трех сообщений в сутки')

class PostUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('_accounts.change_post')
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('_accounts.delete_post')
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


@login_required
def subscrube(request, pk):
    user = request.user.id
    category = Post.objects.get(id=pk).categories.values('name')
    user_cat = []
    for i in User.objects.filter(id=user).values('usercategory__category__name'):
        user_cat.append(i.get('usercategory__category__name'))
    for j in category:
        if j.get('name') not in user_cat:
            UserCategory.objects.create(user_id=user, category_id=Category.objects.get(name=j.get('name')).id)

            send_mail(
                subject=f'{request.user.username}',
                message=f'Вы подписались на категорию {j.get("name")}',
                from_email=DEFAULT_FROM_EMAIL,
                recipient_list=[request.user.email]
            )

            break
    return redirect('post_detail', pk)


@login_required
def unsubscrube(request, pk):
    user = request.user.id
    category = Post.objects.get(id=pk).categories.values('name')
    user_cat = []
    for i in User.objects.filter(id=user).values('usercategory__category__name'):
        user_cat.append(i.get('usercategory__category__name'))
    for j in category:
        if j.get('name') in user_cat:
            UserCategory.objects.filter(user_id=user, category__name=j.get('name')).delete()
            break
    return redirect('post_detail', pk)


