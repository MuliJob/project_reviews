'''Custom Template Tag'''
from django import template

register = template.Library()

@register.filter
def range_filter(start, end):
    '''Custom Template Tag'''
    return range(start, end)
