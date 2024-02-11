import gspread
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
    print(Fore.WHITE + 'Please choose a number for one of the following categories:\n')
    print(Fore.BLUE + '1 - Food & Drink \n2 - Entertainment \n3 - Travel \n4 - Basics and Hygiene \n5 - Extras\n')
    category = input(Fore.WHITE + "Enter category number:" )
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


def main():
    category = get_expense_category()
    validate_expense_category(category)

main()