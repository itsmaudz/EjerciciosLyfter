from student import Student
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

        for student in students:

            student_dict = {
                'name': student.name,
                'section': student.section,
                'spanish_grade': student.spanish_grade,
                'english_grade': student.english_grade,
                'social_studies_grade': student.social_studies_grade,
                'science_grade': student.science_grade
            }

            writer.writerow(student_dict)



def import_students(file_path):
    students = []

    try:
        with open(file_path, 'r', encoding='utf-8', newline='') as file:

            reader = csv.DictReader(file)

            for student in reader:

                new_student = Student(
                    student['name'],
                    student['section'],
                    float(student['spanish_grade']),
                    float(student['english_grade']),
                    float(student['social_studies_grade']),
                    float(student['science_grade'])
                )

                students.append(new_student)

            return students

    except FileNotFoundError:
        print('file not found')
        return None
