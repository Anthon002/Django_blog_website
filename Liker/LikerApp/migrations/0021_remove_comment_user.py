# Generated by Django 4.1.2 on 2023-01-23 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LikerApp', '0020_psuedocomment_comment_post_commented'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
