# Generated by Django 4.2.7 on 2023-11-14 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vumbora', '0009_evento_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='info',
            new_name='descricao',
        ),
        migrations.RemoveField(
            model_name='local',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='local',
            name='longitude',
        ),
        migrations.AddField(
            model_name='usuario',
            name='identificacao',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='evento',
            name='genero',
            field=models.CharField(choices=[('E', 'Exposição'), ('F', 'Festa'), ('G', 'Gastronomia'), ('S', 'Show'), ('T', 'Teatro')], max_length=200),
        ),
        migrations.AlterField(
            model_name='local',
            name='bairro',
            field=models.CharField(choices=[('R', 'Ribeira'), ('P', 'Ponta Negra'), ('T', 'Tirol'), ('I', 'Igapó')], max_length=1),
        ),
        migrations.AlterField(
            model_name='local',
            name='cep',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(choices=[('F', 'Física'), ('J', 'Jurídica')], default='F', max_length=1),
        ),
    ]