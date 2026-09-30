import json

def get_int(text):
    while True:
        try:
            return int(input(text).strip())

        except ValueError:
            print("Por favor, ingresa un número entero.")

def get_float(text):
    while True:
        try:
            return float(input(text).strip())

        except ValueError:
            print("Por favor, ingresa un número valido.")



def read_pokemons(path):

    with open(path, "r", encoding="utf-8") as file:
        
        data = json.load(file)

    return data


def create_pokemon():

    new_pokemons = {}
    skills = []
    stats = {}

    print('ingrese la siguente informacion del pokemon')

    new_pokemons["name"] = input('Nombre: ').strip().lower()
    new_pokemons["tyype"]= input('Tipo: ').strip().lower()
    new_pokemons["level"] = get_int('Nivel: ')
    new_pokemons["weight_kg"] = get_float('Peso(Kg): ')

    answer_is_shiny = input('Es shiny?: si/no ').strip().lower()
    new_pokemons["is_shiny"] = answer_is_shiny == "si"

    answer_held_item = input('tiene equipado algun objeto?: si(escriba el objeto)/no ').strip().lower()     

    if answer_held_item == "si":
        new_pokemons["held_item"] = input("¿Qué objeto sostiene?: ")
    else:
        new_pokemons["held_item"] = None
    

    number_skills = get_int('cuantas habilidades tiene?: ')

    for skill in range(number_skills):

        skill_data = input(f'ingresa la habilidad numero {skill+1}: ' ) 

        skills.append(skill_data)

    new_pokemons["skills"] = skills

    print('ahora ingresaremos los stats del pokemon')

    stats["hp"] = get_int('cuanta vida tendra el pokemon?: ')
    stats["attack"] = get_int('cuanta ataque tendra el pokemon?: ')
    stats["defense"] = get_int('cuanta defensa tendra el pokemon?: ')
    stats["sp_attack"] = get_int('cuanta sp de ataque tendra el pokemon?: ')
    stats["sp_defense"] = get_int('cuanta sp de defensa tendra el pokemon?: ')
    stats["speed"] = get_int('cuanta velocidad tendra el pokemon?: ')

    new_pokemons["stats"] = stats

    return new_pokemons

def save_pokemons(path,pokemons):

    with open(path, "w", encoding="utf-8") as file:

        json.dump(pokemons,file,indent=4)

def main():

    pokemons = read_pokemons("pokemons.json")
    new_pokemon = create_pokemon()
    pokemons.append(new_pokemon)
    save_pokemons("pokemons.json",pokemons)

if __name__ == "__main__":
    main()