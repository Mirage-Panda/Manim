print("Calculator Mode:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
operator = input("Enter an operator (+ - * /): ")

while operator != "+" and operator != "-" and operator != "*" and operator != "/":
    print(f"{operator} is not a valid operator")
    operator = input("Enter an operator (+ - * /): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2

print(round(result, 5))
