# Generated by Django 4.1.4 on 2023-01-28 01:28

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=50, verbose_name='Cargo')),
                ('descripcion', ckeditor.fields.RichTextField(verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidades', models.CharField(max_length=50, verbose_name='Habilidades')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades',
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellido')),
                ('fecha_nacimiento', models.DateField(blank=True, verbose_name='Fecha de nacimiento')),
                ('t_documento', models.CharField(choices=[('DNI', 'DNI'), ('CI', 'CI'), ('PASAPORTE', 'PASAPORTE'), ('CARNET DE EXTRANGERIA', 'CARNET DE EXTRANGERIA')], default='DNI', max_length=30)),
                ('n_documento', models.IntegerField(verbose_name='Numero de documento')),
                ('foto', models.ImageField(upload_to='media/', verbose_name='Foto')),
                ('aportes', ckeditor.fields.RichTextField(verbose_name='Aportes')),
                ('deficiencias', ckeditor.fields.RichTextField(verbose_name='Deficiencias')),
                ('faltas', ckeditor.fields.RichTextField(verbose_name='Hoja de Vida')),
                ('fecha_ingreso', models.DateField(blank=True, verbose_name='Fecha de ingreso')),
                ('cargo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='personal.cargo')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
                ('habilidades', models.ManyToManyField(to='personal.habilidades')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
    ]