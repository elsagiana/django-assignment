from django.test import TestCase, Client
from django.urls import resolve

# Create your tests here.
class MywatchlistTest(TestCase):
    def test_mywatchlist_html_exists(self):
        response = Client().get('https://django-assignment-elsa.herokuapp.com/mywatchlist/html/')
        self.assertEqual(response.status_code,200)

    def test_mywatchlist_xml_exists(self):
        response = Client().get('https://django-assignment-elsa.herokuapp.com/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)    

    def test_mywatchlist_json_exists(self):
        response = Client().get('https://django-assignment-elsa.herokuapp.com/mywatchlist/json/')
        self.assertEqual(response.status_code,200)