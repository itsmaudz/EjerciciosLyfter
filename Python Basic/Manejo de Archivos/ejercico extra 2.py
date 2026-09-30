def count_words(path):
    with open(path, 'r', encoding='utf-8') as file:
        new_file = file.read()
        result = len(new_file.split())

    print(f'Este archivo contiene {result} palabras')

count_words('hola mundo.txt')