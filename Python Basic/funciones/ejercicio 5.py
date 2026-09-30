text = 'Hi Mauro Nice To See You Again.'

def letter_identifier(text):
    upper = 0
    lower = 0 

    for letter in text:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1


    return f'there is {upper} upper cases and {lower} lower cases'

print(letter_identifier(text))


