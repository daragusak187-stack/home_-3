a = float(input("Введіть перше число:"))
b = float(input("Введіть друге число:"))
mark = input("Виберіть дію (+, -, *, /, ^):")

if mark == '+':
    print(f"Результат: {a} + {b} = {a + b}")
elif mark == '-':
    print(f"Результат: {a} - {b} = {a - b}")
if mark == '*':
    print(f"Результат: {a} * {b} = {a * b}")
elif mark == '/':
    if b == 0:
        print("Помилка: Ділення на нуль!!!")
    else:
        print(f"Результат: {a} / {b} = {a / b}")
elif mark == '^':
    print(f"Результат: {a}^{b} = {a ** b}")
else:
    print("Цю дію не знайдено. Доступні лише (+, -, *, /)!")