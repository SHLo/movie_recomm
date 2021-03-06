# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 13:39
from __future__ import unicode_literals

from django.db import migrations

def insert_rating(apps, schema_editor):
    Rating = apps.get_model('main', 'Rating')
    Item = apps.get_model('main', 'Item')
    with open('./main/data/ml-100k/u.data') as rating_file:
        for line in rating_file:
            try:
                user, item, rating, timestamp = line.split()
                item = Item.objects.get(id=item)
            except:
                import pdb
                pdb.set_trace()
                continue
            rating = Rating(
                user='dummy' + user.strip(),
                item=item,
                rating=rating.strip(),
                timestamp=timestamp.strip(),
            )
            rating.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_insert_item_and_genre'),
    ]

    operations = [
        migrations.RunPython(insert_rating),
    ]
