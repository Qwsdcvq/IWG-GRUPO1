# Generated by Django 4.2.4 on 2023-11-26 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intro', '0004_remove_user_patente_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='puntos',
            field=models.IntegerField(default=100),
        ),
    ]