import json

def read_pokemons(path):

    with open(path, 'r', encoding='utf-8') as file:

        pokemons = json.load(file)

        return pokemons


def look_pokemon_by_statistics(pokemons):

        for pokemon in pokemons:

            print(pokemon['name'])
            print(f'Ataque: {pokemon['stats']['attack']}')
            print(f'Defensa: {pokemon['stats']['defense']}')
            print(f'velocidad: {pokemon['stats']['speed']}')



def main():

    pokemons = read_pokemons('pokemons.json')

    look_pokemon_by_statistics(pokemons)
        

if __name__ == '__main__':
    main()
