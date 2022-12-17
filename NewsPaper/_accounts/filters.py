from django_filters import FilterSet, ModelChoiceFilter, CharFilter, widgets
from .models import Post, Category

class PostFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label='Категории',
        empty_label='Любая'
    )


    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'time': ['date__gt']
        }

