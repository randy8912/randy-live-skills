# app/templatetags/qparams.py
from django import template
from django.utils.http import urlencode

register = template.Library()

@register.simple_tag
def qurl(request, **kwargs):
    """
    Bouw een URL met de huidige query params + overrides uit kwargs.
    Voorbeeld: {% qurl request page=2 q="django" tech="" %}
    Lege string verwijdert de param.
    """
    params = request.GET.copy()  # QueryDict
    for key, val in kwargs.items():
        if val == "" or val is None:
            params.pop(key, None)
        else:
            params[key] = val
    qs = params.urlencode()
    return f"?{qs}" if qs else "?"