from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import models
from django.urls import reverse


# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.user.username}'

    def update_rating(self):
        self.rating = 0
        post_rating = 0
        com_rating = 0
        total_com_rating = 0
        s = Author.objects.filter(user_id=self.user).values('user')[0].get('user')
        for _ in Comment.objects.filter(user_id=self.user).values('rating'):
            com_rating += _.get('rating')
        for _ in Post.objects.filter(author_id=s).values('rating'):
            post_rating += _.get('rating')
        if Post.objects.filter(author_id=s):
            for _ in Post.objects.filter(author_id=s):
                for e in Comment.objects.filter(post_id=_.id).values('rating'):
                    total_com_rating += e.get('rating')




        post_rating *= 3
        self.rating += post_rating + com_rating + total_com_rating
        self.save()



class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):

    news = 'news'
    post = 'post'
    CHOISES = [
        (news, 'Новость'),
        (post, 'Статья')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    _type = models.CharField(max_length=4, choices=CHOISES, default=news)
    categories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.FloatField(default=0.0)

    def categoriess(self):
        category = []
        for i in self.categories.values('name'):
            category.append(i.get('name'))
        return category

    def typee(self):
        return self._type

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:124] + ' ...'

    def __str__(self):
        return f'{self.time} {self.title} {self.preview()} {self.rating} \n'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'product-{self.pk}')


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0.0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class UserCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
