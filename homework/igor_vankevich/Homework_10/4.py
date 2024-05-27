PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_price = {x[0:x.index(' ')]: int(x[x.index(' '):-1]) for x in PRICE_LIST.split('\n')}

print(new_price)
