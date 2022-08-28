from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()  # экземпляр класса Library, регистрирует новые фильтры


@register.filter(name='split')
@stringfilter  # гарантирует, что value будет принимать значением только строку!
def split(value, key=' '):  # key ─ разделитель строки value
    return value.split(key)
