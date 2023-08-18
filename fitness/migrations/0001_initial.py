# Generated by Django 4.2.3 on 2023-08-16 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrenamientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrenamiento', models.CharField(max_length=50)),
                ('duracion', models.IntegerField()),
                ('tipo', models.CharField(max_length=15)),
                ('precio', models.BooleanField()),
                ('descripcion', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Nutricion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=50)),
                ('duracion', models.IntegerField()),
                ('tipo', models.CharField(max_length=15)),
                ('precio', models.BooleanField()),
                ('descripcion', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.BooleanField()),
                ('descripcion', models.CharField(max_length=250)),
            ],
        ),
    ]