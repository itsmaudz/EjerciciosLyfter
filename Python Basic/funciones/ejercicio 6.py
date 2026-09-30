text = 'amor-atencion-sabiduria-paz-traquilidad-lealtad'

def arrange_words(text):
    new_list = text.split('-')
    new_list.sort()
    return '-'.join(new_list)

print(arrange_words(text))