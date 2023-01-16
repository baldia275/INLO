from django.core.exceptions import ValidationError
from django.db.models import Model, IntegerField, CharField


def validate_country(value):
    if value != 'Suisse':
        raise ValidationError('Vous devez avoir une adresse suisse pour vous inscrire')


def validate_age(value):
    if value < 18:
        raise ValidationError('Vous devez être majeur pour pouvoir vous inscrire.')


class Client(Model):
    name = CharField(max_length=15)
    age = IntegerField(validators=[validate_age])
    username = CharField(max_length=15)
    address = CharField(max_length=30)
    town = CharField(max_length=15)
    country = CharField(max_length=15,validators=[validate_country])
