# Generated by Django 4.2.4 on 2023-11-26 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intro', '0003_delete_puntos_user_puntos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='patente',
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=50),
        ),
    ]
