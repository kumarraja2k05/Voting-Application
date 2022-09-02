import session.registration as registration
import bcrypt
import maskpass
from utilities.utility import Util
import configuration.config as cf
from utilities.colprint.colprint import NewPrint as col
from user.user_choice import Options


class Auth:

    def login():
        user_id = input("Enter your Id : ")
        current_user_from_db = 0
        try:
            current_user_from_db = list(Util.find_id(user_id))
        except:
            col.col_print("Invalid user, try again....", "red")
            Auth.login()
        else:
            if len(current_user_from_db) == 0:
                col.col_print("No such user found, try again...", "red")
                return Auth.login()
            stored_pass = current_user_from_db[0][8]
            if Auth.validate_pass(stored_pass) == False:
                return
            user_type = Util.get_user_type(user_id)[0][0]
            if user_type != 1:
                if Util.check_is_user_approved(user_id)[0][0] == 0 or False:
                    col.col_print(
                        "You are not yet approved, please wait until approval", "red")
                    return
            col.col_print(
                f"\n---------Welcome {current_user_from_db[0][1]}---------\n", "Yellow")
            is_logged_in = True
            while is_logged_in:
                is_logged_in = Auth.display_options(user_type, user_id)


    def validate_pass(stored_pass):
        input_password = maskpass.advpass().encode('utf-8')
        tries = 2
        while not bcrypt.checkpw(input_password, stored_pass.encode('utf-8')):
            if tries == 0:
                col.col_print("Incorrect password, try again !", "Red")
                return False
            col.col_print(f'Invlaid password, {tries} tries left', "red")
            tries -= 1
            input_password = maskpass.advpass().encode('utf-8')
        else:
            return True

    def sign_up():
        result = registration.Register.reg_new_user()
        if result[0] == True:
            col.col_print(
                f'''\nSuccessfully regiistered\nYour UserId is : {result[1]}, please remember it !!\n''', "cyan")
        return True

    def display_options(user_type, user_id):
        available_operations = cf.roles[user_type]
        user_choice = Options.get_choice(available_operations)
        return cf.role_function_mapping[user_choice](user_id)