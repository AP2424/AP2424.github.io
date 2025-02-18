# Generated by Django 3.2.12 on 2022-08-16 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fantasy', '0032_remove_team_valid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValidTeam',
            fields=[
                ('team_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fantasy.team')),
                ('points', models.BigIntegerField()),
            ],
            bases=('fantasy.team', models.Model),
        ),
    ]
