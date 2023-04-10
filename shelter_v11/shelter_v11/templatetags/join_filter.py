from django import template

register = template.Library()


@register.filter(name='my_join')
def my_join(letters):
    x = []
    for symb in letters:
        x.append(symb)
    return x