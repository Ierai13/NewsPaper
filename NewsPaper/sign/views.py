from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from django.views.generic.edit import CreateView

from .models import BaseRegisterForm
from _accounts.models import Author


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

@login_required
def became_author(request):
    user = request.user
    author_group = Group.objects.get(name='Authors')
    if not request.user.groups.filter(name='Authors').exists():
        author_group.user_set.add(user)
        Author.objects.create(user_id=request.user.id)
    return redirect('/')


