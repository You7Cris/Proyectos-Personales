# Generated by Django 4.1.1 on 2022-09-16 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrivals_departures', '0002_alter_departures_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrivals',
            name='expected_time',
            field=models.TimeField(null=True, verbose_name='Hora esperada'),
        ),
    ]
