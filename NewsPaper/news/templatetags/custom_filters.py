from django import template


register = template.Library()


CENSOR_WORDS = [
    'котопес',
    'шиншилозавр'
]


@register.filter()
def censor(value):
    """ Фильтр, который заменяет буквы нежелательных слов в заголовках и текстах статей на символ «*» """
    for word in CENSOR_WORDS:
        value = value.replace(word[1:], '*' * len(word[1:]))
    return value
