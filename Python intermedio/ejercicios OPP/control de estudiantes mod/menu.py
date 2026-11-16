def display_menu():

    print('Choose an option:')
    print('')
    print('1. Add student')
    print('2. Show students')
    print('3. show top 3 students')
    print('4. show all average students')
    print('5. export students to CSV')
    print('6. import students from CSV')
    print('7. Delete student')
    print('8. View failed students')
    print('0. Exit')

def get_menu_options():
    
    valid_options = ("0", "1", "2", "3", "4", "5", "6", "7","8")

    while True:
        option = input('Choose an option: ').strip()                

        if option in valid_options:
            return option 

        print('Invalid option, please try again')


