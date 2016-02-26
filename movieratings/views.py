from django.shortcuts import render

# Create your views here.
import operator
from movieratings.models import Movie, Review
from django.db.models import Avg


def index_views(request):
    return render(request, 'index.html', {})



def get_all_averages(request):
    average_rating = []
    for item in Movie.objects.all():
        average_rating.append(Review.objects.filter(movie=item).aggregate(Avg('rating')))
    top_twenty = sorted(average_rating, key=lambda k: k['rating__avg'], reverse=True)[:20]
    return render(request, 'top_twenty.html', {'top_twenty': top_twenty})


def movie_views(request):
    return render(request,'movies.html', {})