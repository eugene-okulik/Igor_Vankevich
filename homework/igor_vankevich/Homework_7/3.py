result_1 = 'результат операции: 42'
result_2 = 'результат операции: 54'
result_3 = 'результат работы программы: 209'
result_4 = 'результат: 2'


def adding_to_the_result(result):
    result = result.split()
    print(int(result[-1]) + 10)


adding_to_the_result(result_1)
adding_to_the_result(result_2)
adding_to_the_result(result_3)
adding_to_the_result(result_4)
