from django.contrib import admin

from .models import Author, Category, Comment, Post, PostCategory, UserCategory

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(UserCategory)