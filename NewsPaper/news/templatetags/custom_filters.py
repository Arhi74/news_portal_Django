from django import template
from .bad_words import bad_words

register = template.Library()


@register.filter()
def censor(value):
    split_str = value.split()
    new_split_string = []

    for word in split_str:
        for bad_word in bad_words:
            bad_len = len(bad_word)
            index = word.lower().find(bad_word)
            if index != -1:
                new_split_string.append(word[:index] + '*' * bad_len + word[index + bad_len:])
                break
        else:
            new_split_string.append(word)

    return ' '.join(new_split_string)
