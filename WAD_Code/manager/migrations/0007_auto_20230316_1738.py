# Generated by Django 2.2.28 on 2023-03-16 17:38

from django.db import migrations, models
import manager.models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_merge_20230316_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='slug',
        ),
        migrations.AlterField(
            model_name='player',
            name='profile_pic',
            field=models.ImageField(default='images/default_profile.jpeg', upload_to=manager.models.user_directory_path),
        ),
    ]
