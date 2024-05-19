temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29,
                31, 33, 31, 30, 32, 30, 28, 24, 23]

new_temperature = list(filter(lambda x: x > 28, temperatures))
print(f'The highest temperature: {max(new_temperature)}')
print(f'The lowest temperature: {min(new_temperature)}')
print(f'Average temperature: {round((sum(new_temperature) / len(new_temperature)), )}')
