from django.core.exceptions import ValidationError
from django.db.models import Model
from django.test import TestCase
from django.urls import resolve

from Company.models import Client
from Company.views import clients, inscription

CLIENTS_PATH = '/clients/'
INSCRIPTION_PATH = '/inscription/'


# Create your tests here.
class URLTest (TestCase):
    # Verification s'il y a un statut 200
    def test_clients_status_is_200(self):
        response = self.client.get (CLIENTS_PATH)
        self.assertEqual (200, response.status_code)

    # verifier s'il y a une vue "inscription"
    def test_inscription_calls_clients_view(self):
        urlconfig = resolve (CLIENTS_PATH)
        self.assertEqual (clients, urlconfig.func)


class ViewTest (TestCase):
    # refactor pour pas avoir a retaper self.client.get ('/inscription/') a chaque def
    def clientGet(self):
        return self.client.get (CLIENTS_PATH)

    # verifie si le titre de ma vue est "Inscription"
    def test_company_has_title(self):
        self.assertContains (self.clientGet (), 'Nos clients')

    # verifie si j'ai un template
    def test_inscription_uses_template(self):
        self.assertTemplateUsed (self.clientGet (), 'clients.html')

    # verifie si la vue contient 'clients'
    def test_company_has_clients(self):
        self.assertIn ('clients', self.clientGet ().context)

    def test_company_contains_client_from_db(self):
        c = Client (name='Bader', username='bader123', address='rue de la paix 12', town='Genève', country='Suisse',
                    age=18)

        c.save ()
        response = self.clientGet ()
        self.assertIn (c, response.context['clients'])

    def test_client_name_in_clients_template(self):
        c1 = Client (name='Bader', username='bader123', address='rue de la paix 12', town='Genève', country='Suisse',
                     age=18)
        c2 = Client (name='Amine', username='amine123', address='rue de la paix 12', town='Genève', country='Suisse',
                     age=18)
        c1.save ()
        c2.save ()
        response = self.clientGet ()
        self.assertContains (response, 'Bader')
        self.assertContains (response, "Amine")


class ModelTest (TestCase):

    def test_model_client_exists(self):
        self.assertIsInstance (Client (), Model)

    def test_can_save_client(self):
        c = Client ()
        bob = 'Bob'
        c.name = bob
        c.age = 18
        c.username = 'Bob123'
        c.address = 'rue de la fontaine 3'
        c.town = 'Genève'
        c.country = 'Suisse'

        c.save ()
        self.assertEqual (bob, Client.objects.first ().name)
        self.assertEqual (1, Client.objects.count ())
        self.assertEqual (bob, Client.objects.first ().name)

    def test_client_is_invalid_with_invalid_address(self):
        client = Client (name='Toufik', age=20, address='Avenue Champs-Elysées', country='France', username='toto',
                         town='Paris')
        self.assertRaises (ValidationError, client.full_clean)

    def test_client_is_invalid_with_invalid_age(self):
        client = Client (name='Toufik', age=16, address='Avenue Champs-Elysées', country='France', username='toto',
                         town='Paris')
        self.assertRaises (ValidationError, client.full_clean)
