# Generated by Django 4.2.7 on 2023-12-07 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vumbora', '0017_comenta_evento_comenta_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='arte',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
