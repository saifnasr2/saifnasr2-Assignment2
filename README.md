# saifnasr2-Assignment2
Assignment repo for assignment/1-2 (Assignment2)

# Calculator

A simple console-based calculator built with Python.

This project was created as a practice project to improve understanding of **functions, conditional statements, user input, and exception handling**.

## Features

* Addition (`+`)
* Subtraction (`-`)
* Multiplication (`*`)
* Division (`/`)
* Division-by-zero handling
* Invalid operator handling
* Interactive console menu
* Option to perform multiple calculations or exit

## How It Works

The program provides two options:

```text
=========Choose an Option===========
1-Make a Calculation
2-Exit
```

When choosing **Make a Calculation**, the program asks for:

1. First number
2. Second number
3. Operation

It then performs the requested calculation and displays the result.

## Exception Handling

The project handles invalid operations using Python exceptions.

### Division by Zero

If the user tries to divide by zero:

```python
raise ZeroDivisionError("Cannot Divide by Zero")
```

### Invalid Operator

If the user enters an unsupported operator:

```python
raise ValueError("Invalid Operator")
```

## Technologies

* Python 3
* Console Application

## Example

```text
=========Choose an Option===========
1-Make a Calculation
2-Exit

What is your choice: 1
Enter the first number: 10
Enter the second number: 5
Enter your operation: /
The Result is : 2.0
```

## Purpose

This project is part of my programming practice and is designed to strengthen my understanding of fundamental programming concepts before moving further into **C# and .NET development**.

