# Generated by Django 4.1.2 on 2023-03-13 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LikerApp', '0034_alter_post_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
    ]
