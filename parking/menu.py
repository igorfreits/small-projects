from data import emoji1, emoji2, emoji3, emoji5, emoji6, emoji7, emoji8, emoji9, emoji10
from functions import parking
from clients import register, user


while True:
    option = int(input(f'\033[34m{"WELCOME TO PARKING ISTOP":-^40}'"\n"
                       f'{"Start Menu":-^40}\033[m'

                       f'\n1 -{emoji2} Login or create a new account'
                       f'\033[31m \n2 -{emoji6}  Remove vehicle \033[m'
                       f'\033[34m \n3 -{emoji1}  Jobs \033[m'
                       f'\n4 -{emoji3} Report'
                       f'\033[32m \n5 -{emoji5} Exit \033[m'

                       f'\n\n-Type the desired option: '))
    match option:
        case 1:
            option = int(input('Choose an option: \n'
                               f'\033[35m\n1 -{emoji7} Enter parking\033[m'
                               f'\n2 -{emoji8} Make a new registration.'
                               '\n\n-Type the desired option: '))

            if option == 1:
                user.login()

            if option == 2:
                register.new_register()

        case 2:
            parking.remove_car()
        case 3:
            parking.vacancys()
        case 4:
            option = int(input('Would you like to see which report?'
                               f'\n1 -{emoji9} Registered users'
                               f'\033[32m\n2 -{emoji10} Monthly report\033[m'
                               '\n\n-Type the desired option: '))
            if option == 1:
                register.report_clients()
            if option == 2:
                parking.reports()
        case 5:
            print('\033[31m\nleaving the program...\033[m')
            break
