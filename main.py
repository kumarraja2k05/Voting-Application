from session.auth import Auth
import pyfiglet
from configuration.config import main_menu, dashboard, Invalid
from utilities.colprint.colprint import NewPrint as col
from tabulate import tabulate


class Main:

    def entry_loop():
        col.col_print(dashboard, "Yellow")
        operations = [[idx, (" ").join(x.split("_"))] for idx, x in enumerate(main_menu, 0)]
        print(tabulate(operations, headers=[
              "Enter", "Operation"], tablefmt='fancy_grid'))

        choice = input("Enter your choice : ")
        if choice.isdigit() and int(choice) == 1:
            Auth.sign_up()
        elif choice.isdigit() and int(choice) == 2:
            Auth.login()
        elif choice.isdigit() and int(choice) == 0:
            print(pyfiglet.figlet_format("THANKS \nFOR VISITING"))
            exit()
        else:
            col.col_print(Invalid, 'Red')


print(pyfiglet.figlet_format("V o t i n g   \nS y s t e m"))
while True:
    Main.entry_loop()
