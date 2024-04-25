result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'
index_int_result_1 = result_1.index('42')
print(int(result_1[index_int_result_1:]) + 10)
index_int_result_2 = result_2.index('514')
print(int(result_2[index_int_result_2:]) + 10)
index_int_result_3 = result_3.index('9')
print(int(result_3[index_int_result_3:]) + 10)
