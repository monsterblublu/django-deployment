from django import template

register = template.Library()

@register.filter(name="cut")
def ext(value,arg):
    return value.replace(arg,'')
