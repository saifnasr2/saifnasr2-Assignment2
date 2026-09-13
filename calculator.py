def calculate(num1 , num2 , operator):
    HandleDivisionByZero(num2,operator)
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        raise ValueError("Invalid Operator")


def HandleDivisionByZero(n , op):
    if (n == 0) and (op == "/"):
        raise ZeroDivisionError("Cannot Divide by Zero")
    

while True:
    print("""=========Choose an Option===========
    1-Make a Calculation
    2-Exit\n\n""")
    choice = input("What is your choice:")

    if choice == "1":
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        operation = input("Enter your operation:")
        result = calculate(num1,num2,operation)
        print(f"The Result is : {result}")
    else:   
        break
  



    



