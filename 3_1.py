number1 = float(input("Введіть перше число: "))

operation = input("Введіть операцію (+, -, *, /): ")

number2 = float(input("Введіть друге число: "))

def calculate(number1, operation, number2):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    elif operation == '/':
        if number2 == 0:
            return "Помилка: Дільник не може дорівнювати 0!"
        return number1 / number2

result = calculate(number1,operation,number2)

print(f"Результат: {result}")