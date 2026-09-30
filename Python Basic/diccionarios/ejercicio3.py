list_of_keys = ['hobbies','favorite_animal']

employee = {
    'name': 'OwO',
    'last_name': 'Sidor',
    'role': 'Hacker',
    'hobbies': 'be_a_lover',
    'favorite_animal': 'Donkey',
}

for delete in list_of_keys:

    employee.pop(delete)

print(employee)