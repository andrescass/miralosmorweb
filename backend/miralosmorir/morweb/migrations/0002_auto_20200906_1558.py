# Generated by Django 3.1.1 on 2020-09-06 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=70)),
                ('link', models.CharField(blank=True, default='', max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='TagClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=70)),
            ],
        ),
        migrations.AlterField(
            model_name='movielist',
            name='by',
            field=models.CharField(blank=True, default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='movielist',
            name='description',
            field=models.CharField(blank=True, default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='movielist',
            name='img',
            field=models.CharField(blank=True, default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='movielist',
            name='words',
            field=models.CharField(blank=True, default='', max_length=70),
        ),
        migrations.AddField(
            model_name='movielist',
            name='movies',
            field=models.ManyToManyField(blank=True, related_name='Peliculas', to='morweb.Movie'),
        ),
        migrations.AddField(
            model_name='movielist',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='morweb.TagClass'),
        ),
    ]
