from django.shortcuts import render, render_to_response

# Create your views here.
from movieratings.models import Movie, Review
from django.db.models import Avg


def index_views(request):
    return render(request, 'index.html', {})


def top_twenty_views(request):
    top_twenty = []
    for item in Movie.objects.all():
        top_twenty.append((item.title, item.avg_rating))
    sorted_top_twenty = sorted(top_twenty, key=lambda x:x[1], reverse=True)[:20]
    return render_to_response('top_twenty.html', {'top_twenty': sorted_top_twenty})

"""
def get_all_averages(request):
  average_rating = []
  for item in Movie.objects.all():
      average_rating.append((item.title, (Review.objects.filter(movie=item).aggregate(Avg('rating')))))
  movie_n_rating = []
  for item in average_rating:
      movie_n_rating.append((item[0], item[1]['rating__avg']))
  print(movie_n_rating)
  top_twenty = sorted(movie_n_rating, key=lambda x: x[1], reverse=True)[:20]
  return render(request, 'top_twenty.html', {'top_twenty': top_twenty})
"""
def movie_views(request):
  average_rating = []
  for item in Movie.objects.all():
      average_rating.append((item.title, (Review.objects.filter(movie=item).aggregate(Avg('rating')))))
  movie_n_rating = []
  for item in average_rating:
      movie_n_rating.append((item[0], item[1]['rating__avg']))
  all_movies = sorted(movie_n_rating, key=lambda x: x[1], reverse=True)
  return render(request, 'movies.html', {'all_movies': all_movies})


