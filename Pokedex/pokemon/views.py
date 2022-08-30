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
    template_name = 'pokemon/pokedex.html'

    def get_pokemons(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pokemon = get_pokemon(self.kwargs['url'])
        context['pokemon'] = pokemon
        return context

    def search_pokemon(self, **kwargs):
        context = super().get_context_data(**kwargs)
        term = self.request.GET.get('term')

        allPokemons = get_all_pokemons(898)
        pokemonsList = []
        for pokemon in allPokemons:
            term_checker(pokemon, term, pokemonsList)

        paginator = Paginator(pokemonsList, paginated_by)
        page = self.request.GET.get('page')
        pokemonsList = paginator.get_page(page)

        pokemons = [get_pokemon(pokemon['url']) for pokemon in pokemonsList]

        context['pokemons'] = pokemons
        context['pokemonsList'] = pokemonsList
