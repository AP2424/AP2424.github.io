# Generated by Django 3.2.12 on 2022-12-31 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantasy', '0076_auto_20221231_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='url',
            field=models.URLField(default=''),
        ),
    ]
