"""
Simple Calculator with User History
=====================================
A command-line calculator that performs basic arithmetic operations
and keeps a running history of all calculations.

Features:
- Addition, subtraction, multiplication, division
- Division-by-zero error handling
- History stored as a list
- Loop until user chooses to exit

Example Usage:
  python calculator.py

  1. Add
  2. Subtract
  3. Multiply
  4. Divide
  5. View History
  6. Exit

  Enter your choice: 1
  Enter first number: 10
  Enter second number: 5
  Result: 10.0 + 5.0 = 15.0

Limitations:
- Only accepts numbers (integers or decimals)
- History is lost when you close the program
"""


# ------------------------------------------------
# Basic arithmetic functions
# ------------------------------------------------

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # We can't divide by zero, so we check for that first
    if b == 0:
        print("Error: You can't divide by zero!")
        return None

    return a / b


# ------------------------------------------------
# History functions
# ------------------------------------------------

def add_to_history(history, operation, a, b, result):
    # Each calculation is saved as a dictionary
    entry = {
        "operation": operation,
        "first_number": a,
        "second_number": b,
        "result": result
    }
    history.append(entry)


def show_history(history):
    # If no calculations have been done yet
    if len(history) == 0:
        print("No calculations yet.")
        return

    print("\n--- Calculation History ---")

    # Map each operation name to its symbol
    symbols = {
        "add":      "+",
        "subtract": "-",
        "multiply": "*",
        "divide":   "/"
    }

    # Loop through each saved calculation and print it
    count = 1
    for entry in history:
        op     = entry["operation"]
        a      = entry["first_number"]
        b      = entry["second_number"]
        result = entry["result"]
        symbol = symbols[op]

        print(str(count) + ". " + str(a) + " " + symbol + " " + str(b) + " = " + str(result))
        count = count + 1

    print("--------------------------")


# ------------------------------------------------
# Input helper functions
# ------------------------------------------------

def get_number(prompt):
    user_input = input(prompt)

    # Try to convert what the user typed into a number
    try:
        number = float(user_input)
        return number
    except:
        print("That's not a valid number. Please try again.")
        return None


def get_two_numbers():
    a = get_number("Enter first number: ")
    if a is None:
        return None, None

    b = get_number("Enter second number: ")
    if b is None:
        return None, None

    return a, b


# ------------------------------------------------
# Menu
# ------------------------------------------------

def show_menu():
    print("")
    print("==========================")
    print("    Simple Calculator")
    print("==========================")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. View History")
    print("6. Exit")
    print("==========================")


# ------------------------------------------------
# Main calculator loop
# ------------------------------------------------

def run_calculator():
    # This list will store all our past calculations
    history = []

    print("Welcome to the Simple Calculator!")

    # Keep running until the user picks Exit
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            a, b = get_two_numbers()
            if a is not None and b is not None:
                result = add(a, b)
                print("Result: " + str(a) + " + " + str(b) + " = " + str(result))
                add_to_history(history, "add", a, b, result)

        elif choice == "2":
            a, b = get_two_numbers()
            if a is not None and b is not None:
                result = subtract(a, b)
                print("Result: " + str(a) + " - " + str(b) + " = " + str(result))
                add_to_history(history, "subtract", a, b, result)

        elif choice == "3":
            a, b = get_two_numbers()
            if a is not None and b is not None:
                result = multiply(a, b)
                print("Result: " + str(a) + " * " + str(b) + " = " + str(result))
                add_to_history(history, "multiply", a, b, result)

        elif choice == "4":
            a, b = get_two_numbers()
            if a is not None and b is not None:
                result = divide(a, b)
                if result is not None:
                    print("Result: " + str(a) + " / " + str(b) + " = " + str(result))
                    add_to_history(history, "divide", a, b, result)

        elif choice == "5":
            show_history(history)

        elif choice == "6":
            print("Goodbye! You did " + str(len(history)) + " calculation(s).")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


# ------------------------------------------------
# Start the program
# ------------------------------------------------

run_calculator()