import csv

def export_students(file_path, students):

    with open(file_path, 'w', encoding='utf-8', newline='') as file:

        headers = [

            'name',
            'section',
            'spanish_grade',
            'english_grade',
            'social_studies_grade',
            'science_grade'
        ]

        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writeheader()
        
        writer.writerows(students)

def import_students(file_path):
    students = []

    try:
        with open(file_path, 'r', encoding='utf-8', newline='') as file:
            
            reader = csv.DictReader(file)

            for student in reader:

                student['spanish_grade'] = float(student['spanish_grade'])
                student['english_grade'] = float(student['english_grade'])
                student['social_studies_grade'] = float(student['social_studies_grade'])
                student['science_grade'] = float(student['science_grade'])
                students.append(student)
            return students

    except FileNotFoundError:
        print('file not found')
        return None