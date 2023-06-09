# Generated by Django 2.2.28 on 2023-03-02 22:47

from django.db import migrations, models
import django.db.models.deletion
import manager.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forename', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('age', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=64)),
                ('bio', models.TextField(max_length=500)),
                ('profile_pic', models.ImageField(upload_to=manager.models.user_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=64, unique=True)),
                ('location', models.CharField(max_length=64)),
                ('age_range', models.CharField(max_length=5)),
                ('win_rate', models.FloatField(default=0.0)),
                ('bio', models.TextField(max_length=500)),
                ('logo', models.ImageField(upload_to=manager.models.logo_directory_path)),
                ('gallery', models.CharField(default=manager.models.Team.gallery_default, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Team_Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_made', models.DateField()),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Player')),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Team_Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Player')),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Team')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='registered_players',
            field=models.ManyToManyField(through='manager.Team_Players', to='manager.Player'),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('pitch', models.CharField(max_length=64)),
                ('winner', models.IntegerField()),
                ('loser', models.IntegerField()),
                ('status', models.CharField(choices=[('AC', 'Accepted'), ('PN', 'Pending'), ('DN', 'Denied'), ('CM', 'Complete')], default='PN', max_length=2)),
                ('team1_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='manager.Team')),
                ('team2_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='manager.Team')),
            ],
        ),
    ]
