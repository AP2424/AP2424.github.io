# Generated by Django 3.2.12 on 2022-12-15 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantasy', '0070_nation_flag_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='image',
        ),
        migrations.AddField(
            model_name='player',
            name='image_url',
            field=models.URLField(default=''),
        ),
    ]
