from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'author',
            'categories',
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if len(title) < 20:
            raise ValidationError({
                'title': 'Заголовок не может быть короче 20 символов или пустым!'
            })

        text = cleaned_data.get('text')
        if len(text) < 100:
            raise ValidationError({'text': 'Текст статьи должен быть больше 100 символов!'})

        return cleaned_data
