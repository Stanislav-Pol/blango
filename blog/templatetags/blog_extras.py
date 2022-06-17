from django import template
from django.contrib.auth import get_user_model
from django.utils.html import escape
from django.utils.safestring import mark_safe


user_model = get_user_model()

register = template.Library()

@register.filter
def author_details(author):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""

    if author.first_name and author.last_name:
        name = escape(f'{author.first_name} {author.last_name}')
    else:
        name = escape(f'{author.username}')
    
    name = mark_safe(name)

    if author.email:
        # Escape email address
        email = escape(author.email)
        # Mark safe generated link
        r_link = mark_safe(f'<a href="mailto:{email}">{name}</a>')
        return r_link
    
    return name