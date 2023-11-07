# Generated by Django 4.2.7 on 2023-11-07 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vumbora', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='usuario_email',
            field=models.EmailField(default='SOME STRING', max_length=200),
        ),
        migrations.AddField(
            model_name='usuario',
            name='usuario_nome',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AddField(
            model_name='usuario',
            name='usuario_tipo',
            field=models.CharField(choices=[('F', 'Física'), ('J', 'Jurídica')], default='F', max_length=14),
        ),
    ]
