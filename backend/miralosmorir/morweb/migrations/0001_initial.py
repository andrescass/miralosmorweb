# Generated by Django 3.1.1 on 2020-09-06 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=70)),
                ('description', models.CharField(default='', max_length=70)),
                ('img', models.CharField(default='', max_length=70)),
                ('by', models.CharField(default='', max_length=70)),
                ('words', models.CharField(default='', max_length=70)),
            ],
        ),
    ]