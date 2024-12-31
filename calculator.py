def calculator_mode():
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


def conversion_mode():
    print("Conversion Mode:")
    print("1. Temperature")
    print("2. Distance")
    category = input("Choose a category: ")

    while category != "1" and category != "2":
        print(f"{category} is not a valid category")
        category = input("Choose a category: ")

    if category == "1":
        print("Mode: Temperature")
        print("1. Celsius to Farenheit")
        print("2. Celsius to Kelvin")
        convert_unit = input("Choose a unit to convert to: ")

        while convert_unit != "1" and convert_unit != "2":
            print(f"{convert_unit} is not a valid unit")
            convert_unit = input("Choose a unit to convert to: ")

        if convert_unit == "1":
            celsius = float(input("Enter the temperature to convert: "))
            fahrenheit = float(celsius) * 9 / 5 + 32
            print(f"{celsius}°C is {round(fahrenheit, 2)}°F")

        elif convert_unit == "2":
            celsius = float(input("Enter the temperature to convert: "))
            kelvin = float(celsius) + 273.15
            print(f"{celsius}°C is {round(kelvin, 2)}°K")

    elif category == "2":
        print("Mode: Distance")
        print("1. Kilometres to Miles")
        print("2. Metres to Feet")
        print("3. Centimetres to Inches")
        convert_unit = input("Choose a unit to convert to: ")

        while convert_unit != "1" and convert_unit != "2" and convert_unit != "3":
            print(f"{convert_unit} is not a valid unit")
            convert_unit = input("Choose a unit to convert to:")

        if convert_unit == "1":
            kilometres = float(input("Enter the distance to convert: "))
            miles = float(kilometres) * 0.6213712
            print(f"{kilometres}km is {round(miles, 2)}mi")

        elif convert_unit == "2":
            metres = float(input("Enter the distance to convert: "))
            feet = float(metres) * 3.28084
            print(f"{metres}m is {round(feet, 2)}ft")

        elif convert_unit == "3":
            centimetres = float(input("Enter the distance to convert: "))
            inches = float(centimetres) * 0.3937008
            print(f"{centimetres}cm is {round(inches, 2)}in")


def initialise():
    print("1. Calculator mode")
    print("2. Conversion mode")
    mode_switcher = input("Please choose a mode: ")
    while mode_switcher not in ["1", "2"]:
        print(f"{mode_switcher} is not a valid mode")
        initialise()
    if mode_switcher == "1":
        calculator_mode()
    elif mode_switcher == "2":
        conversion_mode()


initialise()
