# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 21:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, max_length=200, null=True, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Modulo')),
                ('creditos', models.IntegerField(default=0, verbose_name='Créditos')),
                ('horas_clase', models.IntegerField(default=0, verbose_name='Horas de clase')),
                ('horas_seminario', models.IntegerField(default=0, verbose_name='Horas de seminario')),
                ('horas_laboratorio', models.IntegerField(default=0, verbose_name='horas de laboratorio')),
                ('horas_taller', models.IntegerField(default=0, verbose_name='Horas de Taller')),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('anio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='parametros.Anio')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('carrera', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='parametros.Carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('rut', models.CharField(default='', max_length=12, verbose_name='RUT')),
                ('correo', models.EmailField(default='', max_length=100, verbose_name='Correo Electrónico')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametros.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='modulo',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametros.Plan'),
        ),
        migrations.AddField(
            model_name='modulo',
            name='semestre',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='parametros.Semestre'),
        ),
    ]
