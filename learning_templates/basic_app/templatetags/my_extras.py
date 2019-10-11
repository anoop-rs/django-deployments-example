from django import template

register = template.Library()


@register.filter(name="cut_up")
def cut_up(value, arg):
    # This cuts out all values of arg from string
    return value.replace(arg, "")


# register.filter('cut_up', cut_up)
