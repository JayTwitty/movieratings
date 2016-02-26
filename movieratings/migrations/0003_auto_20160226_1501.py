# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 15:01
from __future__ import unicode_literals

from django.db import migrations

from movieratings.models import Movie


def read_data(*args):
    with open("/Users/jtwitty/PycharmProjects/twitty_movies/movieratings/migrations/u.item", encoding="ISO-8859-1") as movies:
        for movie in movies.readlines():
            line = movie.split("|")
            Movie.objects.create(
                id=line[0],
                title=line[1],
                release_date=line[2],
                video_release_date=line[3],
                imdb_url=line[4],
                unknown_genre=line[5],
                action=line[6],
                adventure=line[7],
                animation=line[8],
                childrens=line[9],
                comedy=line[10],
                crime=line[11],
                documentary=line[12],
                drama=line[13],
                fantasy=line[14],
                filmnoir=line[15],
                horror=line[16],
                musical = line[17],
                mystery = line[18],
                romance = line[19],
                scifi = line[20],
                thriller = line[21],
                war = line[22],
                western = line[23]
            )

class Migration(migrations.Migration):

    dependencies = [
        ('movieratings', '0002_auto_20160226_1355'),
    ]

    operations = [
        migrations.RunPython(read_data)
    ]