from . import views
from django.urls import path

app_name = 'pokemon'

urlpatterns = [
    path('', views.PokedexView.as_view(), name='pokedex'),
    path('search/', views.PokemonView.as_view(), name='search'),
]
