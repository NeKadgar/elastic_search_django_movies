# Generated by Django 3.2 on 2021-12-30 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_homepage_alter_movie_imdb_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielanguage',
            name='name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movielanguage',
            name='origin_country',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='productioncountry',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
