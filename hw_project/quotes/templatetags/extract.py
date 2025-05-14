from django import template
from ..models import Author

register = template.Library()

@register.filter
def author(author_obj):
    if isinstance(author_obj, Author):
        return author_obj.fullname
    return "Unknown Author"