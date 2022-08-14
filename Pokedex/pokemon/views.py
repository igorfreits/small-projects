from django.shortcuts import render
from django.views.generic import View, DetailView

# Create your views here.


class PokedexView(View):
    template_name = 'pokemon/pokedex.html'

    def get(self, request):
        return render(request, 'pokemon/pokedex.html')


class PokemonView(DetailView):
    template_name = 'pokemon/pokemon_detail.html'

    def get(self, request, pokemon_id):
        return render(request, 'pokemon/pokemon_detail.html')
