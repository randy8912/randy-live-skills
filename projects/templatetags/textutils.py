# projects/templatetags/textutils.py
from django import template

register = template.Library()

@register.filter(name="splitcsv")
def splitcsv(value):
    """
    Split a comma-separated string into a list of trimmed items.
    Example: 'Python, Django, Tailwind' -> ['Python', 'Django', 'Tailwind']
    """
    if not value:
        return []
    return [s.strip() for s in str(value).split(",") if s.strip()]