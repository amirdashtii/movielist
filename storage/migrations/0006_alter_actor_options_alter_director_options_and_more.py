# Generated by Django 4.1.3 on 2022-11-21 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0005_rename_actors_movie_actor_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'ordering': ['full_name']},
        ),
        migrations.AlterModelOptions(
            name='director',
            options={'ordering': ['full_name']},
        ),
        migrations.AlterModelOptions(
            name='writer',
            options={'ordering': ['full_name']},
        ),
        migrations.AlterField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(blank=True, to='storage.actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ManyToManyField(blank=True, to='storage.director'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_id',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='orginal_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='movie',
            name='runtime',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='writer',
            field=models.ManyToManyField(blank=True, to='storage.writer'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True),
        ),
    ]
