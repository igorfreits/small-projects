import requests


def pokemon(name):
    api = 'https://pokeapi.co/api/v2/pokemon/' + name
    response = requests.get(api)
    pokemon = response.json()
    print(pokemon['name'], pokemon['id'])


if __name__ == '__main__':
    pokemon('gengar')
