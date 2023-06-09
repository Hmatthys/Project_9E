# Generated by Django 2.2.28 on 2023-03-20 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_team_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='team1_id',
            new_name='team1',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='team2_id',
            new_name='team2',
        ),
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.ImageField(upload_to='team_logo/'),
        ),
    ]
