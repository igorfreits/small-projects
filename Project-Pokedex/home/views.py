from django.shortcuts import render
from . import models
import requests
from django.db.models import Q
from django.views.generic.base import TemplateView


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/index.html'


class SearchView(TemplateView):
    termo = models.Search.objects.all()
    if termo:
        termo = termo[0].termo
        termo = termo.capitalize()
        termo = termo.split(' ')
        termo = '-'.join(termo)
        url = 'https://pokeapi.co/api/v2/pokemon/' + termo
        response = requests.get(url)
        return response.json()
    else:
        return None


class PokemonView(TemplateView):
    def get(self, request, pokemon):
        pokemon = self.search(pokemon)
        if pokemon['count'] > 0:
            pokemon = pokemon['results'][0]
            pokemon['image'] = pokemon['url'].split('/')[-2] + '.png'
            pokemon['abilities'] = pokemon['abilities'][0]['ability']['name']
            pokemon['evolution'] = pokemon['species']['evolution_chain']['url'].split(
                '/')[-2]
            pokemon['number'] = pokemon['url'].split('/')[-2]
            pokemon['type'] = pokemon['types'][0]['type']['name']
            pokemon['description'] = pokemon['species']['flavor_text_entries'][3]['flavor_text']
            pokemon['name'] = pokemon['name'].capitalize()
            pokemon['abilities'] = pokemon['abilities'].capitalize()
            pokemon['type'] = pokemon['type'].capitalize()
            pokemon['description'] = pokemon['description'].capitalize()
            pokemon['evolution'] = pokemon['evolution'].capitalize()
            pokemon['number'] = int(pokemon['number'])
            pokemon['image'] = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/' + \
                str(pokemon['number']) + '.png'
            pokemon['abilities'] = pokemon['abilities'].capitalize()
            pokemon['type'] = pokemon['type'].capitalize()
            pokemon
        else:
            pokemon = None
        return render(request, 'home/pokemon.html', {'pokemon': pokemon})

    def search(self, pokemon):
        url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon
        response = requests.get(url)
        return response.json()
