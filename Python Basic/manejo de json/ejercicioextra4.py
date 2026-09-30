import json

def read_pokemons(path):

    with open(path, 'r', encoding='utf-8') as file:

        pokemons = json.load(file)

        return pokemons


def average_level_by_type(pokemons):

    levels = {}
    counts = {}

    for pokemon in pokemons:

        if pokemon['type'] not in levels:

            levels[pokemon['type']] = pokemon['level']

            counts[pokemon['type']] = 1

        else:

            levels[pokemon['type']] += pokemon['level']
            
            counts[pokemon['type']] += 1

    for pokemon_type in levels:

        print(f'Tipo: {pokemon_type} --> Promedio de nivel:  {levels[pokemon_type]/counts[pokemon_type]}')



def main():

    pokemons = read_pokemons('pokemons.json')

    average_level_by_type(pokemons)
        

if __name__ == '__main__':
    main()
