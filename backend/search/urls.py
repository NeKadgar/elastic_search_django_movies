from django.urls import path

from .views import SearchMovies

urlpatterns = [
    path("movie/<str:query>", SearchMovies.as_view()),
]
