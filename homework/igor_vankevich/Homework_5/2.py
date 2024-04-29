result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'
index_result_1 = result_1.index(':')
print(int(result_1[index_result_1 + 1:]) + 10)
index_result_2 = result_2.index(':')
print(int(result_2[index_result_2 + 1:]) + 10)
index_result_3 = result_3.index(':')
print(int(result_3[index_result_3 + 1:]) + 10)
