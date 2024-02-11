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
    """
    Get the date the expense is entered.
    """
    now = datetime.datetime.now()
    date = now.strftime("%x")
    return date


def get_month():
    """
    Get the name of the month the expense is entered, to choose which sheet 
    to add the data to.
    """
    now = datetime.datetime.now()
    month = now.strftime("%B")
    return month


def update_sheet(worksheet,data,category=0):
    """
    Receives the data to insert into the relevant worksheet
    and updates the relevant worksheet with the data.
    """
    worksheet_to_update = SHEET.worksheet(worksheet)
    column = int(category) + 1
    if category == 0:
        last_row = len(worksheet_to_update.get_all_values())
    else:
        last_row = len(worksheet_to_update.get_all_values())-1
    worksheet_to_update.update_cell(last_row + 1, column, data)
    

def get_total_left(sheet):
    """
    Get the value of the total left after the last expense.
    """
    worksheet = SHEET.worksheet(sheet)
    last_row = len(worksheet.get_all_values())
    total_left = worksheet.cell(last_row-1,7).value

    return total_left

def main():
    category = get_expense_category()
    expense = get_expense_value()
    date = get_expense_date()
    month = get_month()
    print("Adding expense date...")
    update_sheet(month,date)
    print("Expense date added.\n")
    print("Adding expense value...")
    update_sheet(month,expense,category)
    print("Expense value added.\n")
    total_left = get_total_left(month)

main()

