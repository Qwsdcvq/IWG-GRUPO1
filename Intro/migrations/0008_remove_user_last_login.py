# Generated by Django 4.2.4 on 2023-11-26 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Intro', '0007_user_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
    ]