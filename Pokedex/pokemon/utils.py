import requests


def get_pokemon(url_pokemon: str) -> dict:
    response = requests.get(url_pokemon)
    pokemon = response.json()
    specie = get_pokemon_specie(pokemon['species']['url'])
    name = specie['name']
    img = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon['id']}.png"

    pokemon['img'] = img
    pokemon['name'] = name.capitalize()
    return pokemon


def get_all_pokemons(amount_pokemons: int) -> list:
    counter = 0
    limit = amount_pokemons if amount_pokemons <= 898 else 898
    url = f"https://pokeapi.co/api/v2/pokemon/?limit={limit}"
    response = requests.get(url)
    jsonObject = response.json()
    pokemonsList = jsonObject['results']

    for pokemon in pokemonsList:
        counter += 1
        img = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{counter}.png"
        pokemon['id'] = f"{counter}"
        pokemon['img'] = img
    return pokemonsList


def get_pokemon_specie(url_specie: str) -> dict:
    response = requests.get(url_specie)
    specie = response.json()
    return specie


def term_checker(pokemon: dict, term: str, array_accumulator: list):
    if term.lower() in pokemon['name'] or term.lower() in pokemon['id']:
        array_accumulator.append(pokemon)
