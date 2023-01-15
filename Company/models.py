from django.core.exceptions import ValidationError
from django.db.models import Model, TextField, DecimalField, IntegerField


# Create your models here.
class Client (Model):
    name = TextField ()
    age = IntegerField()
    username = TextField ()
    address = TextField ()
    town = TextField ()
    country = TextField ()

    def __str__(self):
        return self.address

    def clean(self):
        if self.age < 18:
            raise ValidationError ("Vous devez être majeur pour pouvoir vous inscrire.")
        if 'Suisse' not in self.country:
            raise ValidationError ("Vous devez avoir une adresse suisse pour vous inscrire.")
