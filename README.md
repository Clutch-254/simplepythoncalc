# Python Calculator

## Description
This is a simple yet versatile command-line calculator built in Python. It offers various mathematical operations ranging from basic arithmetic to more advanced functions like logarithms. The calculator provides a user-friendly interface with error handling for invalid inputs.

## Features
- Basic arithmetic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division (with division by zero protection)
  - Modulus (remainder)
- Advanced operations:
  - Square (x²)
  - Cube (x³)
  - Logarithm (base 10)
- Input validation and error handling
- Interactive menu-based interface

## How to Use
1. Run the program: `python calculator.py`
2. Select an operation from the menu by entering a number from 1-9
3. Enter the required number(s) as prompted
4. View the result
5. Continue with more calculations or select option 9 to exit

## Example Usage
```
Python Calculator
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Square
7. Cube
8. Logarithm (base 10)
9. Exit

Select an operation (1-9): 1
Enter the first number: 5.2
Enter the second number: 3.8
Result: 9.0
```

## Input Handling
- The calculator accepts both integers and floating-point numbers
- Error messages are displayed for:
  - Invalid menu selections
  - Non-numeric inputs
  - Division by zero
  - Attempting to calculate logarithms of non-positive numbers

## Requirements
- Python 3.x
- Math module (included in Python standard library)

