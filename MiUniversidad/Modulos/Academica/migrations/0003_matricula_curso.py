# Generated by Django 4.0.5 on 2022-08-19 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academica', '0002_alter_estudiante_dni'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricula',
            name='curso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Academica.curso'),
            preserve_default=False,
        ),
    ]
