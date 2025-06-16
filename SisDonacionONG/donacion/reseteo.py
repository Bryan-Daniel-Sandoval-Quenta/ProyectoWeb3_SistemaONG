import os
import django
from django.db import connection

# Primero configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SisDonacionONG.settings')
django.setup()

with connection.cursor() as cursor:
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='donacion_transaccion'")
    print("Autoincremento para 'donacion_transaccion' reseteado.")

