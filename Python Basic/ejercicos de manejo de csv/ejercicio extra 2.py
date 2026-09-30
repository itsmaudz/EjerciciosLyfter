import csv

def csv_reader_by_line(path):
    with open(path, "r", encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        classification = input('ingrese la clasificacion que desea: ').strip().upper()

        for row in reader:

            if row[3] == classification:

                print(f'{row[0]}')

csv_reader_by_line('new_games_rankings.csv')