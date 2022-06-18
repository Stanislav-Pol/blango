from django import template
from django.contrib.auth import get_user_model
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html


user_model = get_user_model()

register = template.Library()


@register.filter
def author_details(author, current_user = None):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""

    if author.first_name and author.last_name:
        name = f'{author.first_name} {author.last_name}'
    else:
        name = f'{author.username}'
    
    
    if author.email:
        # format_html Escape and Mark safe generated link
        if author==current_user:
            r_link = format_html('<a href="mailto:{}"><strong>{}</strong></a>', author.email, name,)
        else:
            r_link = format_html('<a href="mailto:{}">{}</a>', author.email, name,)
         
    else:
        r_link = format_html('{}', name)
    
    return r_link



"""
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
"""

"""
Alternate version with format_html

from django.utils.html import format_html

@register.filter
def author_details(author):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)
"""