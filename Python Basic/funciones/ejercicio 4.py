text = 'Hola Mundo Lindo'

def reverse_text(text):
    result = ''

    for letter in range(len(text)-1,-1,-1):
        result += text[letter]

    return result

print(reverse_text(text))