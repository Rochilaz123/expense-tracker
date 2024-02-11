import gspread
import datetime
from google.oauth2.service_account import Credentials
from colorama import Fore

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('expense-tracker')


def get_expense_category():
    """
    Get the user to choose a category for the expense.
    """
    while True:
        print(Fore.WHITE + 'Please choose a number for one of the following categories:\n')
        print(Fore.BLUE + '1 - Food & Drink \n2 - Entertainment \n3 - Travel')
        print(Fore.BLUE + '4 - Basics and Hygiene\n5 - Extras\n')
        
        category = input(Fore.WHITE + "Enter category number: " )
        
        if validate_expense_category(category):
            break

    return category
    

def validate_expense_category(data):
    """
    Inside the try converts data entered into an integer,
    Raises ValueError if the data entered can't be converted
    into an integer, or is not between 1 and 5.
    """
    try:
        int(data) 
        if int(data) < 1 or int(data) > 5:
            raise ValueError(
                f"Expected a number between 1 and 5, you provided {data}"
            )
    except ValueError as e:
        print(f"Invalid category: {e}, please try again.\n")
        return False

    return True

def get_expense_value():
    """
    Get the user to enter the value of the expense.
    """
    while True:
        print(Fore.WHITE + '\nPlease enter the value of the expense:\n')
        print(Fore.BLUE + 'example: 12.34 or 5.00\n')
        
        expense = input(Fore.WHITE + "Enter expense value: ")

        if validate_expense_value(expense):
            break

    return expense

def validate_expense_value(data):
    """
    Inside the try converts data entered into a float,
    Raises ValueError if the data entered can't be converted
    into an ifloat, or does not have exactly 2 decimal places.
    """
    try:
        float_data = float(data) 
        if len(str(float_data).split('.')[1]) != 2:
            raise ValueError(
                f"Please enter a number to 2 decimal places"
            )
    except ValueError as e:
        print(f"Invalid data entered: {e}.\n")
        return False

    return True

def get_expense_date():

    now = datetime.datetime.now()
    date = now.strftime("%x")
    return date



def main():
    category = get_expense_category()
    expense = get_expense_value()
    get_expense_date()

main()
