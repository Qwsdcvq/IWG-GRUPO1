# Generated by Django 4.2.4 on 2023-09-06 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=30, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('patente', models.CharField(blank=True, default='', max_length=9)),
            ],
        ),
    ]