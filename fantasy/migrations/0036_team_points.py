# Generated by Django 3.2.12 on 2022-08-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantasy', '0035_team_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='points',
            field=models.BigIntegerField(default=0),
        ),
    ]
