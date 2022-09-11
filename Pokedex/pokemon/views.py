from django.views.generic import TemplateView, View
from django.core.paginator import Paginator
from . utils import get_all_pokemons, get_pokemon, term_checker
from django.shortcuts import render
from django.db.models import Q
# Create your views here.


class PokedexView(View):
    def get(self, request):
        pokemons = get_all_pokemons(898)
        paginator = Paginator(pokemons, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'pokemon/pokedex.html', {'page_obj': page_obj})


class PokemonView(PokedexView):
    template_name = 'pokemon/pokemon.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        term = self.request.GET.get('term')
        paginated_by = 12

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

        return context
