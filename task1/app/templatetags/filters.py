from django import template

register = template.Library()


@register.filter
def to_float(value):
    return float(value)


@register.filter
def to_color(value):
    h = hex(245 - int(float(value)*100)).split('x')[-1]
    return f'#{h}A9A9'


