from datetime import datetime
from django import template


register = template.Library()


@register.simple_tag()  # опишем наш тег вывода текущего времени
def current_time(format_string='%b/%d/%Y'):
    return datetime.utcnow().strftime(format_string)
