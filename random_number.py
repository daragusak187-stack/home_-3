import random

number = random.randint(1,10)

print("Вгадай загадане число від 1 до 10")

options = 3

for i in range(options):
    answer = int(input(f"Спроба {i + 1}: Введи число: "))
    if answer == number:
        print("Вітаю, Ви вгадали загадане число!😎")
        break
    elif answer > number:
        print("Думайте далі! Це число менше.")
    else:
        print("Думайте далі! Це число більше.")
else:
    print(f"На жаль, ти не вгадав(ла). Я загадав число {number}.")