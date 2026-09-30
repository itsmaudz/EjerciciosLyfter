import json

def read_pokemons(path):

    with open(path, 'r', encoding='utf-8') as file:

        pokemons = json.load(file)

        return pokemons

def show_pokemons(pokemons):

    for pokemon in pokemons:
        
        print(f'Nombre: {pokemon['name']}')
        print(f'Tipo: {pokemon['type']}')
        print(f'Nivel: {pokemon['level']}')
        print()

def main():

    pokemons = read_pokemons('pokemons.json')

    show_pokemons(pokemons)
        

if __name__ == '__main__':
    main()
