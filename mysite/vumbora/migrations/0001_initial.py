# Generated by Django 4.2.7 on 2023-11-07 18:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evento_nome', models.CharField(max_length=200)),
                ('evento_datahora', models.DateTimeField(default=django.utils.timezone.now)),
                ('evento_genero', models.CharField(max_length=200)),
                ('evento_valor', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_nome', models.CharField(default='Nome', max_length=200)),
                ('local_estacionamento', models.BooleanField(default=True)),
                ('local_bairro', models.CharField(max_length=200)),
                ('local_cep', models.DecimalField(decimal_places=8, default=0, max_digits=8)),
                ('local_longitude', models.IntegerField(default=0)),
                ('local_latitude', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario_nome', models.CharField(default='SOME STRING', max_length=200)),
                ('usuario_email', models.EmailField(default='SOME STRING', max_length=200)),
                ('usuario_tipo', models.CharField(choices=[('F', 'Física'), ('J', 'Jurídica')], default='F', max_length=14)),
            ],
        ),
    ]