def sort_songs(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        lines.sort()

    with open('new_order_songs.txt', 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)


sort_songs('canciones.txt')

