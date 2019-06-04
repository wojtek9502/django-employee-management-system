from django import template

register = template.Library()

@register.filter
def check_empty(obj_attr):
    if(str(obj_attr)==""):
        return "-"
    return obj_attr


