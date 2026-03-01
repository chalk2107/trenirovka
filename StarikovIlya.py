# Конвертер валют в рубли

print("Конвертер валют")

# Список валют
USD = 76.73
EUR = 90.35
CNY = 11.11
JPY = 0.49
BYN = 26.68

while True:
    try:
        value = float(input("\nВведите сумму в валюте: "))

        print("Список валют:\n" "1: USD\n" "2: EUR\n" "3: CNY\n" "4: JPY\n" "5: BYN\n")


        currency = int(input("Введите необходимую вам валюту: "))

        if(currency == 1):
            print(f"{value} долларов = {value*USD} рублей")
        elif(currency == 2):
            print(f"{value} евро = {value*EUR} рублей")
        elif(currency == 3):
            print(f"{value} юань = {value*CNY} рублей")
        elif(currency == 4):
            print(f"{rubles} рублей = {rubles/JPY} йен")
        elif(currency == 5):
            print(f"{rubles} рублей = {rubles/BYN} белорусских рублей")
        else:
            print("Ошибка!!! Такой валюты нет!")
    
    # Обработка ошибок
    except ValueError:
        print("Ошибка. Нужно вводить числа")