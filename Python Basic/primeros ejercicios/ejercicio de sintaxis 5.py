print("promedio de notas")

grade_count = 1
passing_grade_count = 0
failed_grade_count = 0
average_passing_grade = 0
average_failed_grade = 0
average_total_grade = 0 

grade_total = int(input("ingrese el numero total de notas: "))

while grade_count <= grade_total:
    print(f"ingrese la nota numero {grade_count}: ")
    current_grade = int(input("ingrese la nota: "))
    if current_grade < 70:
        failed_grade_count += 1
        average_failed_grade += current_grade
        grade_count += 1
    else:
        passing_grade_count += 1
        average_passing_grade += current_grade
        grade_count += 1
    average_total_grade = average_total_grade + (current_grade/grade_total)


print(f"el promedio de notas total es: {average_total_grade}")
print(f"la cantidad de notas aprobadas es: {passing_grade_count}")
print(f"la cantidad de notas desaprobadas es: {failed_grade_count}")
if passing_grade_count > 0:
    average_passing_grade = average_passing_grade / passing_grade_count
    print(f"El promedio de notas aprobadas es: {average_passing_grade}")
else:
    print("El promedio de notas aprobadas es: 0")
if failed_grade_count > 0:
    average_failed_grade = average_failed_grade / failed_grade_count   
    print(f"El promedio de notas desaprobadas es: {average_failed_grade}")
else:
    print("El promedio de notas desaprobadas es: 0")