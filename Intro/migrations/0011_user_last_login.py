# Generated by Django 4.2.4 on 2023-11-26 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intro', '0010_remove_user_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
