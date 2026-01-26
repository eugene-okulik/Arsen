my_dict = {list: [1, 5 , 'text', 5.5, 'text2'], tuple: (12, 2.3, 'text3', None, 'alfa'),
           set:{4, 'two', 4, 12, 12.3 },dict: {'a': 1, 'b': 2, 'c': 3, 'one': 'value1', 'two': 'value2'}}
#tuple
print(my_dict[tuple][-1])
print(my_dict[list])
#list
my_dict[list].pop(-1)
my_dict[list].append(2.1)
print(my_dict[list])
#dict
my_dict[dict].pop('a')
my_dict[dict]['i_am_a_tuple'] = 22
print(my_dict[dict])
#set
my_dict[set].add(2.25)
my_dict[set].discard(4)
print(my_dict[set])