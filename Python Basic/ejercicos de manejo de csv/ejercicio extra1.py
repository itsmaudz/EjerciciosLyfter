import csv

def csv_reader_by_line(path):
    with open(path, "r", encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)

        for row in reader:

            print(f'{headers[0]}: {row[0]}')
            print(f'{headers[1]}: {row[1]}')
            print(f'{headers[2]}: {row[2]}')
            print(f'{headers[3]}: {row[3]}')

csv_reader_by_line('new_games_rankings.csv')