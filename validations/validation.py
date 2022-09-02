import math
import datetime
import re
from utilities.colprint.colprint import NewPrint as col

il = "Enter your {}....:"


class Validate:

    def validate_input(val, digits):
        user_input = input(il.format(val))
        try:
            user_input = int(user_input)
        except:
            col.col_print(
                f"Invalid {val}, please enter a valid {digits} digit {val}", "red")
            return Validate.validate_input(val, digits)
        else:
            if math.floor(math.log10(user_input)+1) == digits:
                return user_input
            col.col_print(
                f"Invalid {val}, please enter a valid {digits} digit {val}", "red")
            return Validate.validate_input(val, digits)

    def validate_email():
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email = input(il.format("Email"))
        if not re.fullmatch(regex, email):
            col.col_print("Invalid email, please enter a valid email.", "red")
            return Validate.validate_email()
        else:
            return email

    def validate_dob():
        format = "%Y-%m-%d"
        date = input("Enter DOB (YYYY-MM-DD) ...:")
        try:
            bool(datetime.datetime.strptime(date, format))
        except ValueError:
            col.col_print(
                "Invalid date, please enter a valid date...!!", "red")
            return Validate.validate_dob()
        else:
            return date

    def validate_gen():
        gen = input(il.format("Gender M/F"))
        if gen not in ["M", "F"]:
            col.col_print("Please enter a valid input (M/F)...:", "red")
            return Validate.validate_gen()
        else:
            return gen

    def get_age(dob):
        today = datetime.datetime.today()
        dob = str(dob)
        dob = datetime.datetime.strptime(dob, '%Y-%m-%d')
        age = str((today-dob)/365).split(" ")[0]
        return age
