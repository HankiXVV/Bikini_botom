from django.test import TestCase
from .models import Games 

class GamesTestCase(TestCase):
    
    def test_model_name(self):
        game = Games.objects.create(name="tigr", price=20)
        self.assertEqual(game.name, "tigr")

    def test_model_price(self):
        game = Games.objects.create(name="tigr", price=20)
        self.assertEqual(game.price, 20)
