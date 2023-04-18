from django.core import exceptions


def validate_only_letters(symbols):
    for ch in symbols:
        if not ch.isalpha():
            raise exceptions.ValidationError('Only letters are allowed')
