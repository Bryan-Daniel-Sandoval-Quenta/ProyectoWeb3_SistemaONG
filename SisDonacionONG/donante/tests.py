from django.test import TestCase
from .models import Donante

class DonanteTestCase(TestCase):
    def test_crear_donante(self):
        donante = Donante.objects.create(
            nombre="Juan Pérez",
            telefono="123456789",
            direccion="Calle Falsa 123",
            dni="12345678"
        )
        self.assertEqual(donante.nombre, "Juan Pérez")
        self.assertEqual(donante.dni, "12345678")
