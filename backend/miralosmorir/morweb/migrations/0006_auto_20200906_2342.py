# Generated by Django 3.1.1 on 2020-09-07 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morweb', '0005_movie_words'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='mtags',
            field=models.ManyToManyField(blank=True, related_name='movie_tags', to='morweb.TagClass'),
        ),
    ]
