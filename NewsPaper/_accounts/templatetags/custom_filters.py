from django import template

from _accounts.models import Category

register = template.Library()

BAD_CHECK = {
    'альн': '****',
}

@register.filter()
def fcheck(value):

    for a, b in BAD_CHECK.items():
        if a in value:
            value = value.replace(a, b)
    return f'{value}'


@register.filter()
def dictKey(the_dict):
   return the_dict['usercategory__category__name']


@register.filter()
def get_cat_id(cat):
    return Category.objects.get(name=cat).id
