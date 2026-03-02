
# НАДО РАЗОБРАТЬСЯ
# ЖОСКО РАЗОБРАТЬСЯ

firstNumber = int(input("Введите первое число: "))

secondNumber = int(input("Введите второе число: "))

operation = int(input("Введите номер операции:\n"
                      "1. +\n"
                      "2. -\n"
                      "3. *\n"
                      "4. /\n"
                      "Операция: "))

match operation:
    case 1:
        result = firstNumber + secondNumber
    case 2:
        result = firstNumber - secondNumber
    case 3:
        result = firstNumber * secondNumber
    case 4:
        if (secondNumber == 0):
            print("Деление на ноль запрещено!")
            result = "Ошибка!"
        else:
            result = firstNumber / secondNumber
    case _:
        print("Операция не выбрана, выберите операцию")
        result = "Ошибка!"

print(f"Результат операции: {result}")

# СЛОЖНАЯ ПРОГА