# Generated by Django 4.1.1 on 2022-09-16 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrivals_departures', '0003_alter_arrivals_expected_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrivals',
            name='expected_time',
            field=models.TimeField(default=None, null=True, verbose_name='Hora esperada'),
        ),
        migrations.AlterField(
            model_name='departures',
            name='expected_time',
            field=models.TimeField(default=None, null=True, verbose_name='Hora esperada'),
        ),
    ]
