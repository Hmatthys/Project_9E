# Generated by Django 2.2.28 on 2023-03-16 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_auto_20230316_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
