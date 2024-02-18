# Expense Tracker

This Expense tracker is perfect for anyone on a monthly budget who wants to keep track of their spending.

It is very easy to use, requiring the user to input a number for one of the category options, and the value of the expense.

The program adds the expense to a spreadsheet for the relevant month dated for the day you add it, and then advises the user how much money they have left to spend that month, and how much they have spent on that particular category that month.

![Here is the live link to my website]()

![Devices Mock-up](image link)

## Features

![Screenshot]()

### Existing Features

- User gets prompted to enter the required information to add the expense.
- Input validation to handle an invalid response and displaying to the user a relevant error message and requesting another input with the correct data.
- After the user adds an expense, they get asked if they would like to add another expense or exit the program.
- If the user spends more than their monthly budget, they get notified after adding an expense.

### Future Features

- Allow user an option of entering a different date for the expense.
- Give the user the option of adding more spending money for the month.
- Give the user the option of adding another category.

## Structure

- I have decided to use a class to access my spreadsheet. Any instances where the program interacts with the spreadsheet, it utilises methods of the ExpenseSpreadsheet class.
- I have used a main function to call all the funtions to run the program, and to give the user continuous feed back of what the program is doing.

## Testing

I have tested my code by doing the following:
- Passed the code through a PEP8 linter and ensured there are no problems.
- Given invalid inputs: letters instead of numbers, invalid numbers, empty inputs.
- Tested in my local terminal (and in the Heroku terminl to ensure it functions correctly.)

## Bugs

### Solved Bugs

- During testing, the functions that were accessing data from the spreadsheet were returning errors. I realised it was because i had formatted the spreadsheet to  include a currency sign. After removing that, the functions al worked.
- The input requesting the value of the expense didn't register any zeros after the decimal point and gave an error. After changing the wording of the if statement, the validation started working correctly.

### Remaining  Bugs

- No bugs remaining

### Validator Testing

- PEP8
    - No errors returned from https://pep8ci.herokuapp.com/

## Deployment

This project was deployed using Code Institutes mock terminal for Heroku.

Steps for deployment:
 - 