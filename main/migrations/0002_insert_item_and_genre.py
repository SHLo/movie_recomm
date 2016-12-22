# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 07:16
from __future__ import unicode_literals

from django.db import migrations
import datetime
from dateutil.parser import parse

def insert_genre(apps, schema_editor):
    Genre = apps.get_model('main', 'Genre')
    with open('./main/data/ml-100k/u.genre') as genre_file:
        for line in genre_file:
            try:
                name, id = line.split('|')
                genre = Genre(id=id.strip(), name=name.strip())
            except:
                continue
            genre.save()

def insert_item(apps, schema_editor):
    Item = apps.get_model('main', 'Item')
    with open('./main/data/ml-100k/u.item') as item_file:
        for line in item_file:
            line = unicode(line, errors='ignore')
            cells = line.split('|')
            try:
                dt = parse(cells[2]).strftime('%Y-%m-%d')
            except:
                dt = None
            item = Item(
                id=cells[0].strip(),
                title=cells[1].strip(),
                release=dt,
                imdb=cells[4].strip(),
                genre_unknown = cells[5].strip(),
                genre_Action = cells[6].strip(),
                genre_Adventure = cells[7].strip(),
                genre_Animation = cells[8].strip(),
                genre_Children = cells[9].strip(),
                genre_Comedy = cells[10].strip(),
                genre_Crime = cells[11].strip(),
                genre_Documentary = cells[12].strip(),
                genre_Drama = cells[13].strip(),
                genre_Fantasy = cells[14].strip(),
                genre_Film_Noir = cells[15].strip(),
                genre_Horror = cells[16].strip(),
                genre_Musical = cells[17].strip(),
                genre_Mystery = cells[18].strip(),
                genre_Romance = cells[19].strip(),
                genre_Sci_Fi = cells[20].strip(),
                genre_Thriller = cells[21].strip(),
                genre_War = cells[22].strip(),
                genre_Western = cells[23].strip(),
            )
            item.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_genre),
        migrations.RunPython(insert_item),
    ]
