import csv

def csv_reader_by_line(path):
    with open(path, "r", encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        developer = input('Ingrese el desarrollador: ').strip().lower()

        print(f'Videojuegos desarrollados por {developer}:')

        found = False

        for row in reader:

            if row[2].lower() == developer:
                found = True
                print(f'- {row[0]} (clasificacion: {row[3]}, Genero: {row[1]})')

        if found == False:

                print('no hay ningun juego con este dearrollador')

csv_reader_by_line('new_games_rankings.csv')


