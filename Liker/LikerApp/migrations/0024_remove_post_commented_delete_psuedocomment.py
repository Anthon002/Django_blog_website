# Generated by Django 4.1.2 on 2023-01-23 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LikerApp', '0023_remove_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='commented',
        ),
        migrations.DeleteModel(
            name='PsuedoComment',
        ),
    ]
