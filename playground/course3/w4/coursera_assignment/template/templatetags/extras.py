from django import template

register = template.Library()


@register.filter(name='inc')
def inc(n, diff):
    return int(n) + int(diff)


@register.simple_tag
def division(divd, divsr, to_int=False):
    divd = float(divd)
    divsr = float(divsr)
    if to_int:
        return int(divd / divsr)
    return divd / divsr
