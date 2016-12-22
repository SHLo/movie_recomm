# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 07:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('release', models.DateField(blank=True, null=True)),
                ('imdb', models.CharField(max_length=256)),
                ('genre_unknown', models.BooleanField(default=False)),
                ('genre_Action', models.BooleanField(default=False)),
                ('genre_Adventure', models.BooleanField(default=False)),
                ('genre_Animation', models.BooleanField(default=False)),
                ('genre_Children', models.BooleanField(default=False)),
                ('genre_Comedy', models.BooleanField(default=False)),
                ('genre_Crime', models.BooleanField(default=False)),
                ('genre_Documentary', models.BooleanField(default=False)),
                ('genre_Drama', models.BooleanField(default=False)),
                ('genre_Fantasy', models.BooleanField(default=False)),
                ('genre_Film_Noir', models.BooleanField(default=False)),
                ('genre_Horror', models.BooleanField(default=False)),
                ('genre_Musical', models.BooleanField(default=False)),
                ('genre_Mystery', models.BooleanField(default=False)),
                ('genre_Romance', models.BooleanField(default=False)),
                ('genre_Sci_Fi', models.BooleanField(default=False)),
                ('genre_Thriller', models.BooleanField(default=False)),
                ('genre_War', models.BooleanField(default=False)),
                ('genre_Western', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('rating', models.IntegerField()),
                ('timestamp', models.CharField(max_length=64)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Item')),
            ],
        ),
    ]
