from django.shortcuts import render
from django.views.generic import View, TemplateView
import requests
from django.core.paginator import Paginator

# Create your views here.


class PokedexView(View):
    template_name = 'pokemon/pokedex.html'

    def get_context_data(self, **kwargs):
        url = 'http://pokeapi.co/api/v2/pokedex/1/'
        r = requests.get(url)
        data = r.json()
        paginator = Paginator(data['pokemon_entries'], 20)
        page = self.request.GET.get('page')
        pokemon_entries = paginator.get_page(page)
        context = {
            'pokemon_entries': pokemon_entries
        }
        return context


class PokemonView(TemplateView):
    template_name = 'pokemon/pokemon_detail.html'

    def get(self, request, pokemon_id):
        url = f'http://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
        response = requests.get(url)
        data = response.json()

        return render(request, 'pokemon/pokemon_detail.html', {'data': data})
