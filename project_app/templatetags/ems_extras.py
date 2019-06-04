from django import template

register = template.Library()

@register.filter
def check_empty(obj_attr):
    if(str(obj_attr)==""):
        return "-"
    if(obj_attr is None):
        return "-"
    return obj_attr

@register.filter
def print_false_true(obj_attr):
    print(obj_attr)
    if(obj_attr is False):
        return "Nie"
    else:
        return "Tak"

