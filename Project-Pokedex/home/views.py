from django.shortcuts import render
from . import models
import requests
from django.db.models import Q
from django.views.generic.base import TemplateView


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/index.html'


class PokemonDetail(TemplateView):
    template_name = 'home/pokemon_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pokemon'] = models.Pokemon.objects.get(pk=kwargs['pk'])
        pokemonID = requests.GET.get('pokemonID')
        pokemon = requests.get(
            f'https://pokeapi.co/api/v2/pokemon/{pokemonID}/')
        context['pokemon'] = pokemon.json()
        return context


class SearchView(TemplateView):
    pokemonID = requests.GET.get('pokemonID')
    pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemonID}/')
    context = {'pokemon': pokemon.json()}
    template_name = 'home/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pokemon'] = models.Pokemon.objects.get(pk=kwargs['pk'])
        return context
