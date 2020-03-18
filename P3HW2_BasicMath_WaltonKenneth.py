#This program is a calculator
#It performs basic math operations
#CTI - 110
#P3HW2 - BasicMath
#Kenneth Walton
#17 March 2020

def add(number1, number2):
    return number1 + number2
def subtract(number1, number2):
    return number1 - number2
def multiply(number1, number2):
    return number1 * number2
print('Menu')
print('1. Add Numbers');
print('2. Multiply Numbers');
print('3. Subtract Numbers');
print('4. Exit')

number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))

operation = input(('''Enter the operation you would like to perform:
                   1 for addition
                   2 for multiplication
                   3 for subratction
                   '''))

if operation == '1':
    print('number1 + number2 = ', add(number1, number2))

elif operation == '2':
    print('number1 * number2 = ', multiply(number1, number2))

elif operation == '3':
    print('number1 - number2 = ', subtract(number1, number2))
    print('number1 - number2')

elif operation == '4':
    exit('Program will terminate')

else:
    print('Error, you have not chosen a valid operation. Please try again')

        
