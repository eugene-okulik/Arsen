prise_list = 'тетрадь 50р, книга 200р, ручка 100р, карандаш 70р, альбом 120р, пенал 300р, рюкзак 500р'
nwe_list = prise_list.split(', ')
my_dict = {items.split()[0]: int(items.split()[1].strip('р')) for items in nwe_list}

print(my_dict)
