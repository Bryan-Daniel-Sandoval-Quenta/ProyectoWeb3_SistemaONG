from django.test import TestCase
from .models import Campania
from datetime import date

class CampaniaTestCase(TestCase):
    def test_crear_campania(self):
        campania = Campania.objects.create(
            titulo="Campaña Escolar",
            descripcion="Recaudación para útiles",
            meta_financiera=1000,
            fecha_inicio=date.today(),
            fecha_limite=date(2025, 12, 31),
            estado='A'
        )
        self.assertEqual(campania.estado, 'A')
