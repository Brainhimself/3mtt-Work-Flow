number1 = int(input("Enter your first number: "))
operator = input("Enter your operator (+, -, /, *): ")
number2 = int(input("Enter your second number: "))

if operator == '+' :
    result = number1 + number2
    print(f"The result for {number1} + {number2} is {result}")

elif operator == '-' :
    result = number1 - number2
    print(f"The result for {number1} - {number2} is {result}")

elif operator == '*' :
    result = number1 * number2
    print(f"The result for {number1} * {number2} is {result}")

elif operator == '/' :
    result = number1 / number2
    print(f"The result for {number1} / {number2} is {result}")

else:
    print("Operator nor valid, kindly use either of (*, -, + or /)")