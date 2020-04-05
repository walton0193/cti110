#CTI-110
#P4HW1 - Expenses
#Kenneth Walton
# 3 April 2020
#
#This program is an expenses calculator.

expense = 0.0
starting_amt = 0.0
remaining_amt = 0.0
total_expense = 0.0
keep_going = 'y'

#Get the starting amount
starting_amt = int(input('Enter the starting amount in account'))


#determine more variables
while keep_going == 'y':
    #Get the expense
    expense = float(input('Enter expense: '))
    total_expense = total_expense + expense
    keep_going = input('Do you want to enter another expense? (y/n)')
    

#Display the starting amount
print('The amount in account before expense subraction is', starting_amt)

#Display number of expenses
print('Number of expenses entered:')

#Find the total
remaining_amt = starting_amt - total_expense
print('Amount in account AFTER expenses subtracted is', remaining_amt)
    

