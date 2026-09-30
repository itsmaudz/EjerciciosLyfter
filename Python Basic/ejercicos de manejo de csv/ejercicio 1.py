import csv

def create_games():

    games = []

    number_game = int(input('Ingrese la cantidad de videojuegos que deseas en tu lista: '))

    for game in range(number_game):

        game_dict = {    

            'Name' : input('nombre del juego: '),

            'genre' : input('genero: '),

            'developer' : input('desarrollador: '),

            'ESRB_classification' : input('clasificacion ESRB: '),
        }

        games.append(game_dict)

    return games

def save_games_ranking(file_path, data):

    with open(file_path, 'w', encoding='utf-8', newline='') as file:

        headers = data[0].keys()

        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writeheader()

        writer.writerows(data)


def main():

    games = create_games()
    save_games_ranking('new_games_rankings.csv', games)

if __name__ == '__main__':
    main()





