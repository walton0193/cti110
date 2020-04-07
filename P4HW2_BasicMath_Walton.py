#CTI-110
#P4HW2 - BasicMath
#Kenneth Walton
#April 6 2020
#
#Call main fuction
#Display menu
def main():
    print('-------MENU------')
    print('1) Add numbers')
    print('2) Multiply numbers')
    print('3) Subtract numbers')
    print('4) Exit')
    print('-----------------')

#Add numbers
def Add(num1, num2):
    return num1 + num2

#Multiply numbers
def Multiply(num1, num2):
    return num1 * num2

#Subtract numbers
def Subtract(num1, num2):
    return num1 - num2



#get numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#Enter choice
print('Choose your operation')
operation = input("Enter operation")


#Perform operation

if operation == '1':
    result = num1 + num2
    print(num1,"+",num2,"=",result)

elif operation == '2':
    result = num1 * num2
    print(num1,"*",num2,"=",result)

elif operation == '3':
    result = num1 - num2
    print(num1,"-",num2,"=",result)

elif operation == '4':
    exit()

else:
    print('Error: Please enter a choice from the menu')
    main()

