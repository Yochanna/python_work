from django import template
register = template.Library()

@register.filter
def shout(value: str) -> str:
    return (value or "").upper() + "!"

@register.filter
def currency(value) -> str:
    try:
        return f"${float(value):,.2f}"
    except Exception:
        return str(value)