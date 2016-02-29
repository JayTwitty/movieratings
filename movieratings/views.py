from django.shortcuts import render

# Create your views here.
from movieratings.models import Movie, Review, Rater


def top_twenty_views(request):
    sorted_top_twenty = Movie.objects.order_by('-avg_rating')[:20]
    return render(request, 'top_twenty.html', {'top_twenty': sorted_top_twenty})



def movie_page(request, pk):
    movie = Movie.objects.get(id=pk)
    print(request.POST)
    if request.POST:
        rater_age = request.POST['age_input']
        rater_gender = request.POST['gender_input']
        rater_occupation = request.POST['occupation_input']
        rater_zipcode = request.POST['zipcode_input']
        rater_review = request.POST['rating_input']
        try:
            rater = Rater.objects.create(age=rater_age, gender=rater_gender, occupation=rater_occupation, zip_code=rater_zipcode)
        except Exception:
            print("Invalid Entry")
        try:
            Review.objects.create(reviewer= rater, movie=movie, rating=rater_review)
        except Exception:
            print("Invalid Entry")
    reviewers = Review.objects.filter(movie_id=pk)
    movie_ratings = Movie.objects.filter(id=pk)
    return render(request, 'movies.html', {'reviewers': reviewers,
                                           'movie': movie,
                                           'movie_ratings': movie_ratings
                                           })


def all_of_the_movies(request):
    all_movies = Movie.objects.all()
    return render(request,'index.html', {'every_movie': all_movies})



def every_user(request, pk):
    individual_user = Rater.objects.get(id=pk)
    rater_movies = Review.objects.filter(reviewer=individual_user.pk)
    return render(request, 'every_user.html', {'individual':individual_user,
                                               'rater_movies':rater_movies})

