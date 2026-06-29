# Simple Calculator with User History

A beginner Python project that runs in the terminal and lets you do basic math with a history of all your calculations.

---

## How to Run

Make sure you have Python installed, then run:

```
python calculator.py
```

---

## Features

- Addition, subtraction, multiplication, division
- Catches invalid input (letters, symbols) without crashing
- Catches division by zero
- Keeps a history of all calculations in the current session

---

## How to Use

When you run the program, you'll see this menu:

```
==========================
    Simple Calculator
==========================
1. Add
2. Subtract
3. Multiply
4. Divide
5. View History
6. Exit
==========================
Enter your choice:
```

- Type a number from **1 to 4** to pick an operation
- Enter two numbers when asked
- The result is shown immediately
- Type **5** to see all past calculations
- Type **6** to exit

---

## Example

```
Enter your choice: 1
Enter first number: 10
Enter second number: 5
Result: 10.0 + 5.0 = 15.0

Enter your choice: 5

--- Calculation History ---
1. 10.0 + 5.0 = 15.0
--------------------------
```

---

## Limitations

- History is lost when you close the program
- Only accepts plain numbers (integers or decimals)
- Does not support expressions like `2 + 3 * 4`
