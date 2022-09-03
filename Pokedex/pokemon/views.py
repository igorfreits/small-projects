from django.views.generic import TemplateView, View
from django.core.paginator import Paginator
from . utils import get_all_pokemons, get_pokemon, term_checker
from django.shortcuts import render
# Create your views here.


class PokedexView(View):
    template_name = "pokemon/index.html"

    def get(self, request):
        pokemons = get_all_pokemons(898)
        paginator = Paginator(pokemons, 20)
        page = request.GET.get('page')
        pokemons = paginator.get_page(page)
        return render(request, self.template_name, {'pokemons': pokemons})


class PokemonView(TemplateView):
    template_name = "pokemon/pokemon.html"

    def search_pokemons(self, request):
        term = request.GET.get('term')
        if term_checker(term):
            pokemons = get_pokemon(term)
            return pokemons
        else:
            return None

    def get(self, request):
        pokemons = self.search_pokemons(request)
        if pokemons:
            return render(request, self.template_name, {'pokemons': pokemons})
        else:
            return render(request, self.template_name, {'pokemons': None})
