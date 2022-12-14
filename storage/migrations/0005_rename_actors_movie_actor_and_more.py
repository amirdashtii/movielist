# Generated by Django 4.1.3 on 2022-11-19 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0004_rename_actor_movie_actors_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='actors',
            new_name='actor',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='countries',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='directors',
            new_name='director',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='genres',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='languages',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='writers',
            new_name='writer',
        ),
    ]
