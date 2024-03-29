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


class ExpenseSpreadsheet:
    sheet = None

    def __init__(self, spreadsheet_name):
        self.sheet = GSPREAD_CLIENT.open(spreadsheet_name)

    def get_total_left(self, worksheet_name):
        """
        Get the value of the total left after the last expense.
        """
        worksheet = self.sheet.worksheet(worksheet_name)
        last_row = len(worksheet.get_all_values())
        total_left = worksheet.cell(last_row-1, 7).value

        return total_left

    def calculate_category_total(self, worksheet_name, category):
        """
        Calculate the total of the category of the new expense, and
        inform the user how much they have spent for that category
        this month.
        """
        worksheet = self.sheet.worksheet(worksheet_name)
        category_to_total = int(category) + 1
        values_list = worksheet.col_values(category_to_total)
        category_total = 0
        for x in values_list[1:]:
            if x == '':
                continue
            category_total = category_total + float(x)
        return category_total

    def update_total_left(self, total_left, expense, worksheet_name):
        """
        Calculate the total left after this expense was added,
        and update the spreadsheet.
        """
        print(Fore.CYAN + "Calculating total left...")
        new_expense = float(expense)
        last_total_left = float(total_left)
        new_total_left = last_total_left - new_expense
        worksheet = self.sheet.worksheet(worksheet_name)
        last_row = len(worksheet.get_all_values())
        print(Fore.CYAN + "Updating total left...")
        worksheet.update_cell(last_row, 7, new_total_left)
        print(Fore.CYAN + "Total left updated.\n")
        print(Fore.YELLOW +
              f"The total you have left to spend this month is" +
              f" £{round(new_total_left, 2)}\n")
        if new_total_left <= 0:
            print(Fore.RED +
                  f"You have spent more than your budget for this month.")

    def update_sheet(self, worksheet_name, data, category=0):
        """
        Receives the data to insert into the relevant worksheet
        and updates the relevant worksheet with the data.
        """
        worksheet = self.sheet.worksheet(worksheet_name)
        column = int(category) + 1
        if category == 0:
            last_row = len(worksheet.get_all_values())
        else:
            last_row = len(worksheet.get_all_values())-1
        worksheet.update_cell(last_row + 1, column, data)


def get_expense_category():
    """
    Get the user to choose a category for the expense.
    """
    while True:
        print(Fore.WHITE +
              'Please choose a number for one of the following categories:\n')
        print(Fore.BLUE + '1 - Food & Drink \n2 - Entertainment \n3 - Travel')
        print(Fore.BLUE + '4 - Basics and Hygiene\n5 - Other\n')

        category = input(Fore.WHITE + "Enter category number: \n")

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

        expense = input(Fore.WHITE + "Enter expense value: £\n")

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
    Get the name of the month the expense is entered, to choose
    which sheet to add the data to.
    """
    now = datetime.datetime.now()
    month = now.strftime("%B")
    return month


def main():
    """
    Run all program functions. Once all functions have run, gives user
    option to add another expense or to exit.
    """
    answer = "+"
    spreadsheet = ExpenseSpreadsheet("expense-tracker")
    while answer == "+":
        category = get_expense_category()
        expense = get_expense_value()
        date = get_expense_date()
        month = get_month()
        print(Fore.GREEN + "\nAdding expense date...")
        spreadsheet.update_sheet(month, date)
        print(Fore.GREEN + "Expense date added.\n")
        print(Fore.MAGENTA + "Adding expense value...")
        spreadsheet.update_sheet(month, expense, category)
        print(Fore.MAGENTA + "Expense value added.\n")
        total_left = spreadsheet.get_total_left(month)
        spreadsheet.update_total_left(total_left, expense, month)
        category_total = spreadsheet.calculate_category_total(month, category)
        print(Fore.YELLOW +
              f"The total you have spent on this category this month is " +
              f"£{round(category_total, 2)}\n")
        answer = input(Fore.WHITE +
                       'Press + then enter to add another expense,' +
                       ' or press enter to exit:\n')
        if answer == "+":
            continue
        else:
            break


main()
