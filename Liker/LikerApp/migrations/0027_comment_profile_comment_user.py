# Generated by Django 4.1.2 on 2023-01-27 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LikerApp', '0026_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='Profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='LikerApp.profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]