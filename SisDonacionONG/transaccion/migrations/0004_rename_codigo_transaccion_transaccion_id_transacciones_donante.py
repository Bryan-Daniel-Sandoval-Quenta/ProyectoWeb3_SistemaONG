# Generated by Django 4.2.11 on 2025-06-16 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaccion', '0003_remove_transaccion_onante_transaccion_donante'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaccion',
            old_name='codigo_transaccion',
            new_name='id_transacciones_donante',
        ),
    ]
