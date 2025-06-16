from django.test import TestCase
from .models import Transaccion
class TransacionTestCase(TestCase):
    def test_crear_transacion(self):
        transaccion = Transaccion.objects.create(
            donante = "juan",
            codigoTransacion="d001",
            proveedorPago="paypal",
            estado="bien",
            comision= 35.9,
        )
        self.assertEqual(transaccion.donante,"juan")
        self.assertEqual(transaccion.codigo_transaccion, "d001")
        self.assertEqual(transaccion.comision, 35.9)
