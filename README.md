# Expense Tracker

This Expense tracker is perfect for anyone on a monthly budget who wants to keep track of their spending.

It is very easy to use, requiring the user to input a number for one of the category options, and the value of the expense.

The program adds the expense to a spreadsheet for the relevant month dated for the day you add it, and then advises the user how much money they have left to spend that month, and how much they have spent on that particular category that month.

[Here is the live link to my website](https://expense-tracker-1-05b15e017258.herokuapp.com/)

![Devices Mock-up](/readme-assets/devices-mockup.PNG)

## Features

![screen print](/readme-assets/screenprint1.png)

- Prompts user to enter the expense category, and then the expense value.
    - Clear instructions
    - Colored text for clear diferentiation between sections

![screen print](/readme-assets/screenshot2.PNG)

- Gives user constant clear feedback
- Different colors seperates between different sections and makes it clearer for the user

![screen print](/readme-assets/screenshot3.PNG)

- Informs the user how much of their budget they have left to spend that month
- Informs the user how much they have spent on the category of their latest expense
- Informs the user if they have exceeded their monthly budget
- Gives the user the option to add another expense

![screen print](/readme-assets/spreadsheet-image.PNG)

- Keeps track of your expenses, subtracting them from the monthly budget as the user adds them.
- Each expense is dated, and in the correct category so the user can see what they are spending on.
- Each month's expenses are on a seperate spreadsheet as this is for a user working with a monthly budget and it keeps each month seperate.

### Existing Features

- User gets prompted to enter the required information to add the expense.
- Input validation to handle an invalid response and displaying to the user a relevant error message and requesting another input with the correct data.
- After the user adds an expense, they get asked if they would like to add another expense or exit the program.
- If the user spends more than their monthly budget, they get notified after adding an expense.

### Future Features

- Allow user an option of entering a different date for the expense.
- Give the user the option of adding more spending money for the month.
- Give the user the option of adding another category.
- Give the user the option to delete an expense.

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

## Validator Testing

- PEP8
    - No errors returned from https://pep8ci.herokuapp.com/

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

Steps for deployment:

 - The project was deployed using Code Institute's mock terminal for Heroku.

 - Steps for deployment:
    - Create new app on Heroku
    - Add config vars
    - Set the buildpack to Python and NodeJS, in that order
    - Link the Heroku app to my GitHub repository
    - Click on Deploy