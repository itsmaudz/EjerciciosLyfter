def get_valid_grade(text):
    while True:
        try:
            grade = float(input(text).strip())

            if 0<=grade<=100:
                return grade

            print('Please enter a number between 0 and 100')
        
        except ValueError:
            print('invalid number, try again')

def is_valid_name(name):
    if not name.strip():
        return False

    for character in name:
        if character.isdigit():
            return False
        
    return True


def is_valid_section(section):

        if len(section) != 3:
            return False

        if not section[:2].isdigit():
            return False

        if not section[2].isalpha():
            return False
    
        return True


def is_student_exist(students,name,section):
    for student in students:
        if student['name'].lower() == name.lower() and student['section'] == section:
            return True

    return False

def add_student(students):
    while True:
        while True:
            name = input('Enter your name: ').strip()

            if  is_valid_name(name):
                break

            print('Invalid name, try again')

        while True:
            section = input('Enter section: ').strip().upper()

            if is_valid_section(section):
                break

            print('Invalid section, try again')

        if is_student_exist(students,name,section):
            print('Student already exists')
            continue
        break

    spanish_grade = get_valid_grade('Enter spanish grade: ')
    english_grade = get_valid_grade('Enter english grade: ')
    social_studies_grade = get_valid_grade('Enter social studies grade: ')
    science_grade = get_valid_grade('Enter science grade: ')

    new_students = {

        'name': name,
        'section': section,
        'spanish_grade': spanish_grade,
        'english_grade': english_grade,
        'social_studies_grade': social_studies_grade,
        'science_grade': science_grade

    }

    students.append(new_students)


def show_students(students):
    if not students:
        print('No students registered yet')
        return

    for student in students:

        print(f'Name: {student['name']}')
        print(f'Section: {student['section']}')
        print(f'Spanish Grade: {student['spanish_grade']}')
        print(f'English grade: {student['english_grade']}')
        print(f'Social Studies grade: {student['social_studies_grade']}')
        print(f'Science Grade: {student['science_grade']}')
        print('')


def calculate_average(student):

    return (student['spanish_grade']+student['english_grade']+student['social_studies_grade']+student['science_grade'])/(4)



def show_top_students(students):

    if not students:
        print('No students registered yet')
        return

    organized_students = sorted(students,key=calculate_average,reverse=True)

    print('Top 3 best average students')
    print('')

    for student in organized_students[:3]:

        print(f"Name: {student['name']}; Average: {calculate_average(student)}")

def show_all_average_students(students):

    if not students:
        print('No students registered yet')
        return

    sum_total = 0

    for student in students:

        average_each = calculate_average(student)

        sum_total += average_each

    overall_average = sum_total/len(students)

    print(f"Average total is: {overall_average}")


def delete_student(students):

    if not students:
        print('No students registered yet')
        return
    while True:
        name = input('Enter student  name: ').strip()

        if is_valid_name(name):
            break

        print('please enter a valid name')

    while True:
        section = input("Enter section: ").strip().upper()

        if is_valid_section(section):
            break

        print('please enter a  valid section: ')

    if not is_student_exist(students,name,section):
        print('student not found')
        return

    while True:

        confirmation = input('Are you sure you want to delete this student? (y/n): ').strip().lower()

        if confirmation == 'y':
            break

        elif confirmation == 'n':
            print('deletion cancelled')
            return

        else: 
            print('please enter y or n')

    for  index,student in enumerate(students):

        if student['name'].lower() == name.lower() and student['section'] == section:
            students.pop(index)
            print(f'this student {student['name']} of this section {student['section']} was deleted ')
            break


def show_failed_students(students):

    if not students:
        print('No students registered yet')
        return

    found_failed_student = False

    for student in students:

        failed_subjects = []

        if student['spanish_grade'] < 60:

            failed_subjects.append(f'Spanish: {student['spanish_grade']}')

        if student['english_grade'] < 60:

            failed_subjects.append(f'English: {student['english_grade']}')

        if student['social_studies_grade'] < 60:

            failed_subjects.append(f'Social studies: {student['social_studies_grade']}')

        if student['science_grade'] < 60:

            failed_subjects.append(f'science: {student['science_grade']}')

        if failed_subjects:

            found_failed_student = True

            print(student['name'])
            print(student['section'])
            print('')

            for subject in failed_subjects:
                print(subject)
                
            print('')

    if not found_failed_student:
        print('No students have failed any subjects.')

