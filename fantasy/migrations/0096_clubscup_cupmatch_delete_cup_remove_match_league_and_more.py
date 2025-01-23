# Generated by Django 4.1.5 on 2023-01-27 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fantasy', '0095_alter_poll_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubsCup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('LOCAL', 'Local'), ('INTERNATIONAL', 'International')], default='', max_length=20)),
                ('name', models.CharField(default='', max_length=50)),
                ('groups', models.SmallIntegerField(default=0)),
                ('proceed_places', models.SmallIntegerField(default=0)),
                ('lower_cup_places', models.SmallIntegerField(default=0)),
                ('clubs', models.ManyToManyField(to='fantasy.club')),
            ],
        ),
        migrations.CreateModel(
            name='CupMatch',
            fields=[
                ('match_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fantasy.match')),
                ('stage', models.IntegerField(default=0)),
                ('cup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fantasy.clubscup')),
            ],
            bases=('fantasy.match',),
        ),
        migrations.DeleteModel(
            name='Cup',
        ),
        migrations.RemoveField(
            model_name='match',
            name='league',
        ),
        migrations.RemoveField(
            model_name='match',
            name='matchday',
        ),
        migrations.AlterField(
            model_name='poll',
            name='type',
            field=models.CharField(choices=[('POLL', 'Poll'), ('QUIZ', 'Quiz')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='pollchoice',
            name='image_url',
            field=models.URLField(default=''),
        ),
        migrations.CreateModel(
            name='LeagueMatch',
            fields=[
                ('match_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fantasy.match')),
                ('matchday', models.SmallIntegerField(default=0)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fantasy.league')),
            ],
            bases=('fantasy.match',),
        ),
    ]
