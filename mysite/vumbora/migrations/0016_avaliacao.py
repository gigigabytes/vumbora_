# Generated by Django 4.2.7 on 2023-11-26 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vumbora', '0015_usuario_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('evento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='vumbora.evento')),
                ('nota', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
                ('comentario', models.CharField(max_length=200, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vumbora.usuario')),
            ],
            bases=('vumbora.evento',),
        ),
    ]
