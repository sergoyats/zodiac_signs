from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()  # the instance of the Library class (registers new filters)


@register.filter(name='split')
@stringfilter
def split(value, key=' '):  # key is the string separator value
    return value.split(key)
