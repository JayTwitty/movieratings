from django.contrib import admin

# Register your models here.
from movieratings.models import Rater, Movie, Review

admin.site.register(Rater)
admin.site.register(Movie)
admin.site.register(Review)

