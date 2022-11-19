# Generated by Django 4.1.3 on 2022-11-19 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='full_name',
            field=models.ManyToManyField(null=True, to='storage.movie'),
        ),
        migrations.AlterField(
            model_name='director',
            name='full_name',
            field=models.ManyToManyField(null=True, to='storage.movie'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_id',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='orginal_title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='movie',
            name='runtime',
            field=models.FloatField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.FloatField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='writer',
            name='full_name',
            field=models.ManyToManyField(null=True, to='storage.movie'),
        ),
    ]