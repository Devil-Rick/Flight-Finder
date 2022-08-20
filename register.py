import re
from replit import clear
import data_manager as data


EMAIL_FORMAT = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def start():
    print("\nWELCOME!!!\nRegister fast to get the Cheapest Flight Deals.")
    print("\nHere we send you send you cheapest Flight Deals and email you.")


def register_email():
    first_name = input("Enter your Firstname: ")
    last_name = input("Enter your Lastname: ")
    email_id = input("Enter your email: ")
    if re.fullmatch(EMAIL_FORMAT, email_id):
        email_verify = input("Enter your email again: ")
        if email_id == email_verify:
            print("You are in the CLUB...")
            return first_name, last_name, email_id
        else:
            print("Email id doesn't match")
    else:
        print("Invalid Email")


class Register:
    def __init__(self):
        start()
        self.x = register_email()

    def register_user(self):
        try:
            dm = data.DataManager()
            users_list = dm.add_user(first_name=self.x[0], last_name=self.x[1], email_id=self.x[2])
            return users_list
        except TypeError:
            clear()
            print("TRY Again....\n")
            Register()
