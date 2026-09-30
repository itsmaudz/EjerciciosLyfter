text = 'hola precioso mundo'

def count_vocals(text):
    count = 0
    for vocals in text:
        if vocals in 'aeiou':
            count += 1
    return f'el  numero de vocales es: {count}'

print(count_vocals(text))