from menu import display_menu, get_menu_options
from actions import add_student, show_students, show_top_students, show_all_average_students, delete_student, show_failed_students
from data import export_students, import_students

def main():

    students = []

    while True:
        display_menu()
        option = get_menu_options()

        if option == '1':

            add_student(students)

        elif option == '2':

            show_students(students)

        elif option == '3':

            show_top_students(students)

        elif option == '4':

            show_all_average_students(students)

        elif option == '5':
            
            if not students:
                print('No students to export yet.')
            else:
                export_students('students.csv', students)
                print('Students exported successfully.')

        elif option == '6':
            imported_students = import_students('students.csv')

            if imported_students is None:
                print('Import failed. Current students were not changed.')
            else:
                students = imported_students

                if students:
                    print(f'{len(students)} students imported successfully.')
                else:
                    print('The CSV contains no student records.')

        elif option == '7':

            delete_student(students)

        elif option == '8':

            show_failed_students(students)

        elif option == '0':

            break


if __name__ == '__main__':
    main()


