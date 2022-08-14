from . import views
from django.urls import path

urlpatterns = [
    path('', views.PokedexView.as_view(), name='pokedex'),
    path('pokemon/<int:pokemon_id>',
         views.PokemonView.as_view(), name='pokemon_detail'),
]
