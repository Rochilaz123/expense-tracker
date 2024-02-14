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
        print(Fore.WHITE + 
              'Please choose a number for one of the following categories:\n')
        print(Fore.BLUE + '1 - Food & Drink \n2 - Entertainment \n3 - Travel')
        print(Fore.BLUE + '4 - Basics and Hygiene\n5 - Other\n')
        
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
                Fore.RED + 
                f"Expected a number between 1 and 5, you provided {data}"
            )
    except ValueError as e:
        print(Fore.RED + f"Invalid category: {e}, please try again.\n")
        return False

    return True

def get_expense_value():
    """
    Get the user to enter the value of the expense.
    """
    while True:
        print(Fore.WHITE + '\nPlease enter the value of the expense:\n')
        print(Fore.BLUE + 'example: 12.34 or 5.00\n')
        
        expense = input(Fore.WHITE + "Enter expense value: £")

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
        decimal_part = str(float_data).split('.')
        if (len(decimal_part) == 1 or 
           (len(decimal_part) == 2 and len(decimal_part[1]) > 2)):
            raise ValueError(
                Fore.RED + 
                f"Please enter a number with exactly 2 decimal places"
            )
    except ValueError as e:
        print(Fore.RED + f"Invalid data entered: {e}.\n")
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

def update_total_left(total_left,expense,worksheet):
    """
    Calculate the total left after this expense was added,
    and update the spreadsheet.
    """
    print(Fore.CYAN + "Calculating total left...")
    new_expense = float(expense)
    last_total_left = float(total_left)
    new_total_left = last_total_left - new_expense
    worksheet_to_update = SHEET.worksheet(worksheet)
    last_row = len(worksheet_to_update.get_all_values())
    print(Fore.CYAN + "Updating total left...")
    worksheet_to_update.update_cell(last_row, 7, new_total_left)
    print(Fore.CYAN + "Total left updated.\n")
    print(Fore.YELLOW + 
        f"The total you have left to spend this month is £{round(new_total_left,2)}\n")
    if new_total_left <= 0:
        print(Fore.RED + f"You have spent more than your budget for this month.")


def calculate_category_total(worksheet,category):
    """
    Calculate the total of the category of the new expense, and inform the
    user how much they have spent for that category this month.
    """
    sheet = SHEET.worksheet(worksheet)
    category_to_total = int(category) + 1
    values_list = sheet.col_values(category_to_total)
    category_total = 0
    for x in values_list[1:]:
        if x == '':
            continue
        category_total = category_total + float(x)
    
        
    print(Fore.YELLOW +
     f"The total you have spent on this category")
    print(f"this month is £{round(category_total,2)}\n")


"""def user_exit_option():
    answer = input("Would you like to add another expense?(y/n) ")
    lower(answer)"""



"""def validate_user_exit_option():
    try:
        if answer == "y"
            return True

    except ValueError as e:
        print(Fore.RED + f"Invalid data entered: {e}.\n")
        return False"""

def main():
    """
    Run all program functions. Once all functions have run, gives user 
    option to add another expense or to exit.
    """
    answer = "+"
    while answer == "+":
        category = get_expense_category()
        expense = get_expense_value()
        date = get_expense_date()
        month = get_month()
        print(Fore.GREEN + "\nAdding expense date...")
        update_sheet(month,date)
        print(Fore.GREEN + "Expense date added.\n")
        print(Fore.MAGENTA + "Adding expense value...")
        update_sheet(month,expense,category)
        print(Fore.MAGENTA + "Expense value added.\n")
        total_left = get_total_left(month)
        update_total_left(total_left,expense,month)
        calculate_category_total(month, category)
        answer = input('Press + to add another expense, press enter to exit:')
        if answer == "+":
            continue
        else:
            break


main()
