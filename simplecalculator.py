#first number then operator then second number then an output else gives an error
try:
    num1 = int(input("Enter first number: "))
    operator = input("Enter operator ( +, -, *, /): ")
    num2 = int(input("Enter second number: "))

    if operator == "+":
        print("Answer is",num1 + num2)
    elif operator == "-":
        print("Answer is",num1 - num2)
    elif operator == "*":
        print("Answer is",num1 * num2)
    elif operator == "/":
        print("Answer is",num1 / num2)

except:
    print("Invalid input")
