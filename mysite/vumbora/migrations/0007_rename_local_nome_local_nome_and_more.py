# Generated by Django 4.2.7 on 2023-11-12 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vumbora', '0006_alter_local_local_cep_alter_local_local_nome_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='local',
            old_name='local_nome',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='usuario_nome',
            new_name='nome',
        ),
    ]