from django.shortcuts import render, render_to_response, get_list_or_404

# Create your views here.
from movieratings.models import Movie, Review
from django.db.models import Avg


def index_views(request):
    return render(request, 'index.html', {})


def top_twenty_views(request):
    sorted_top_twenty = Movie.objects.order_by('-avg_rating')[:20]
    return render_to_response('top_twenty.html', {'top_twenty': sorted_top_twenty})


def movie_page(request, pk):
    reviewers = get_list_or_404(Review, movie_id=pk)
    movie = Movie.objects.get(id=pk)
    movie_ratings = Movie.objects.filter(movie=movie.pk)
    return render(request, 'movies.html', {'all_movies': movie,
                                              'reviewers': reviewers,
                                              'movie_ratings': movie_ratings
                                              })


def movie_views(request):
    return render_to_response('movies.html')