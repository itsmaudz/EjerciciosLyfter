hotel = {

    'name': 'Mendoza',
    'number_of_stars': 5,
    'rooms': [
    
        {
            'number': 1,
            'floor': 1,
            'price_per_night': 100,
        },
        {
            'number': 2,
            'floor': 2,
            'price_per_night': 200,
        },
        {
            'number': 3,
            'floor': 3,
            'price_per_night': 300,
        },
        { 
            'number': 4,
            'floor': 4,
            'price_per_night': 400,
        },
        { 
            'number': 5,
            'floor': 5,
            'price_per_night': 500,
        },
]
}

print(hotel.get('rooms')[1])