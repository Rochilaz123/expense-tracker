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
    print(Fore.WHITE + 'Please choose a number for one of the following categories:\n')
    print(Fore.BLUE + '1 - Food & Drink \n2 - Entertainment \n3 - Travel \n4 - Basics and Hygiene \n5 - Extras\n')
    category = input(Fore.WHITE + "Enter category number:" )
    return category

def main():
    get_expense_category()

main()