sales = [
{
    'date': '27/07/07',
    'customer_email': 'OwO@gmail.com',
    'items': [
        {
            'name': 'fan',
            'upc': 'item-1',
            'unit_price': 70.07,
        },
        {
            'name': 'lamp',
            'upc': 'item-2',
            'unit_price': 20.02,
        },
        {
            'name': 'cup',
            'upc': 'item-3',
            'unit_price': 50.05,
        },
    ],
},
{
    'date': '28/08/08',
    'customer_email': 'inkisidor@gmail.com',
    'items': [
        {
            'name': 'lamp',
            'upc': 'item-2',
            'unit_price': 20.02,
        },
        {
            'name': 'box',
            'upc': 'item-4',
            'unit_price': 10.01,
        },
        {
            'name': 'fan',
            'upc': 'item-1',
            'unit_price': 70.07,
        },
    ],
},
{
    'date': '26/06/06',
    'customer_email': 'evil@gmail.com',
    'items': [
        {
            'name': 'box',
            'upc': 'item-4',
            'unit_price': 10.01,
        },
    ],
},
{
    'date': '28/08/08',
    'customer_email': 'inkisidor@gmail.com',
    'items': [
        {
            'name': 'lamp',
            'upc': 'item-2',
            'unit_price': 20.02,
        },
        {
            'name': 'fan',
            'upc': 'item-1',
            'unit_price': 70.07
        },
    ],
},
]

result = {}

for sale in sales:
    for item in sale['items']:
        
        upc = item['upc']
        price = item['unit_price']

        if upc in result:
            result[upc] += price
        else:
            result[upc] = price

print(result)