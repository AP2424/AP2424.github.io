# Generated by Django 3.2.12 on 2022-07-23 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fantasy', '0012_rename_players_team_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='player',
        ),
    ]
