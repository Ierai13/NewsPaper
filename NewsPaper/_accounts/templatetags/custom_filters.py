from django import template

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
