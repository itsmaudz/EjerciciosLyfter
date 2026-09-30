products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

total_per_category = {}

for total in products:
    if total['category'] not in total_per_category:
        total_per_category[total['category']] = 0
    total_per_category[total["category"]] += total['price']

print(total_per_category)