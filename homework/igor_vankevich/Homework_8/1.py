import random

salary = int(input('Inter your salary\n'))
bonys = random.choice([True, False])

if bonys is True:
    print(f'{salary}, {bonys} - ${int(random.random() * 100) + salary}')
else:
    print(f'{salary}, {bonys} - ${salary}')
