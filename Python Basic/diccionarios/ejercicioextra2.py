employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofia", "email": "sofia@empresa.com", "department": "RRHH"},
    {"name": "Maria", "email": "maria@empresa.com", "department": "CEO"}
]

department = {}

for depart in employees:
    if depart["department"] not in department:
        department[depart["department"]] = []
    department[depart["department"]].append(depart)

print(department)