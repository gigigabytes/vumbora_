# Generated by Django 4.2.7 on 2023-11-07 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vumbora', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='local_rua',
            field=models.CharField(default='Inserir', max_length=200),
        ),
    ]