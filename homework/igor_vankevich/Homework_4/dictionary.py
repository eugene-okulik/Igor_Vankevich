my_dict = {'tuple': '', 'list': '', 'dict': '', 'set': ''}
my_dict['tuple'] = (3, 14, 'blablabla', False, 433)
my_dict['list'] = [21, 33, 93849, 'test', 6.11]
my_dict['dict'] = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
my_dict['set'] = {3.22, 14, 'ololo', 14, 22}
print(my_dict['tuple'][-1])
my_dict['list'].append('last')
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] = 'no, i am a dict'
my_dict['dict'].pop('one')
my_dict['set'].add(123)
my_dict['set'].discard(22)
print(my_dict)
