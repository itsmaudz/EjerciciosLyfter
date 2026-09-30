import json

def read_pokemons(path):

    with open(path, 'r', encoding='utf-8') as file:

        pokemons = json.load(file)

        return pokemons


def find_pokemon_by_type(pokemons):

    pokemon_type = input('ingrese el tipo de pokemon que desea buscar (water,electric,fire,etc): ').strip().lower()
    print('Los pokemos que existen de ese tipo son: ')
    print()

    found = False

    for pokemon in pokemons:

        if pokemon['type'].lower() == pokemon_type:

            found = True            
            
            print(pokemon['name'])

    if not found:

        print('Ninguno')


def main():

    pokemons = read_pokemons('pokemons.json')

    find_pokemon_by_type(pokemons)
        

if __name__ == '__main__':
    main()
