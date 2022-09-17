# Generated by Django 4.1.1 on 2022-09-16 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrivals_departures', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departures',
            options={'verbose_name': 'Salida', 'verbose_name_plural': 'Salidas'},
        ),
        migrations.AlterModelOptions(
            name='remarks_arrivals',
            options={'verbose_name': 'Comentario llegada', 'verbose_name_plural': 'Comentarios de llegada'},
        ),
        migrations.AlterModelOptions(
            name='remarks_departures',
            options={'verbose_name': 'Comentario de salida', 'verbose_name_plural': 'Comentarios de salida'},
        ),
        migrations.AlterField(
            model_name='departures',
            name='expected_time',
            field=models.TimeField(null=True, verbose_name='Hora esperada'),
        ),
        migrations.AlterField(
            model_name='remarks_arrivals',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Comentarios de llegada'),
        ),
    ]
