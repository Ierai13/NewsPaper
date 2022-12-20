from django_filters import FilterSet, ModelChoiceFilter, CharFilter, widgets, DateFilter
from django import forms
from .models import Post, Category

class PostFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label='Категории',
        empty_label='Любая'
    )
    time = DateFilter(widget=forms.DateInput(attrs={'type': 'date', 'value': '2022-12-13'}), lookup_expr='gt')
    title = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['title', 'time']

