import sys
sys.set_int_max_str_digits(0)


def fibonacci(numbers):
    n_1 = 1
    n_2 = 0
    n_3 = 0
    count = 0
    while count < numbers:
        yield n_3
        n_3 = n_1 + n_2
        n_1 = n_2
        n_2 = n_3
        count += 1


def position_fibonacci(position):
    count_1 = 0
    for num in fibonacci(100**100):
        if count_1 == position:
            print(num)
            break
        count_1 += 1


position_fibonacci(5)
position_fibonacci(200)
position_fibonacci(1000)
position_fibonacci(100000)
