num = 46

while True:
    user_input = input("Введите число от 0 до 100\n")
    if user_input.isnumeric():
        user_input = int(user_input)
        if user_input == num:
            print("Поздравляю! Вы угадали!")
            break
        else:
            print("Попробуйте снова")
