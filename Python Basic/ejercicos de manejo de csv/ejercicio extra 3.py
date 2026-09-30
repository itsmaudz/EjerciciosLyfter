import csv

def csv_reader_by_line(path):
    with open(path, "r", encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        result = {}

        for row in reader:

            if row[1] in result:

                result[row[1]] += 1

            else:

                result[row[1]] = 1

        for genre in sorted(result):

            print(f'{genre}: {result[genre]}')

csv_reader_by_line('new_games_rankings.csv')


