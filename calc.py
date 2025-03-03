# Calculator
# A simple calculator in Python
# author: G. Guilhermino Neto
# last update: 2025.03.03

import os

# Opens the calculator
def open_calculator():
    print("==========================")
    print("Welcome to the calculator")
    print("==========================\n")
    print("Choose by the number the operation you want to be done.\n")
    print("1 - Summation")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Exponentiation")

# Lets the user choose the operation
def choose_operation():
    operation = int(input())
    operations = ['Summation', 'Subtraction', 'Multiplication', 'Division', 'Exponentiation']
    print(">>> You chose {}.".format(operations[operation-1]))
    return(operation)

# Lets the user choose two numbers
def choose_numbers():
    print("\nWhich will be the first number?")
    num_1 = float(input())
    print("\nWhich will be the second number?")
    num_2 = float(input())
    return([num_1, num_2])

# Does the math
def calculations(operation, numbers):

    num_1 = numbers[0]
    num_2 = numbers[1]
    
    if operation == 1:
        print("\n{} + {} = {}".format(num_1, num_2, num_1 + num_2))
    
    elif operation == 2:
        print("\n{} - {} = {}".format(num_1, num_2, num_1 - num_2))
    
    elif operation == 3:
        print("\n{} * {} = {}".format(num_1, num_2, num_1 * num_2))
    
    elif operation == 4:
        print("\n{} / {} = {}".format(num_1, num_2, num_1 / num_2))
    
    else:
        print("\n{} ** {} = {}".format(num_1, num_2, num_1 ** num_2))

# Runs the calculator by using the above functions
open_calculator()
operation = choose_operation()
numbers = choose_numbers()
calculations(operation, numbers)

# Lets user choose if he/she wants to do another operation and stops if not
print("\nDo you want to do another operation? 1 - Yes, 0 - No")
yn = int(input())

while yn == 1:
    os.system('cls')
    open_calculator()
    operation = choose_operation()
    numbers = choose_numbers()
    calculations(operation, numbers)
    print("\nDo you want to do another operation? 1 - Yes, 0 - No\n")
    yn = int(input())