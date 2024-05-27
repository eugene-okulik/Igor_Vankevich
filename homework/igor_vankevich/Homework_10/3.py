user_num1, user_num2 = input('Enter two numbers separated by a space\n').split()
user_num1 = int(user_num1)
user_num2 = int(user_num2)


def operation_calc(func):

    def wrapper(num1, num2):
        if num1 == num2:
            return func(num1, num2, operation='+')
        elif num1 > num2:
            return func(num2, num1, operation='-')
        elif num1 < num2:
            return func(num1, num2, operation='/')
        elif num1 or num2 < 0:
            return func(num1, num2, operation='*')
    return wrapper


@operation_calc
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


print(calc(user_num1, user_num2))
