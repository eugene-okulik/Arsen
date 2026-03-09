class Flower:
    def __init__(self, flower, petals, price, time_of_life, stem_len, color):
        self.flower = flower
        self.petals = petals
        self.time_of_life = time_of_life
        self.price = price
        self.stem_len = stem_len
        self.color = color


class Roses(Flower):
    def __init__(self, flower, petals, price, time_of_life, stem_len, color, variety, thorns):
        super().__init__(flower, petals, price, time_of_life, stem_len, color)
        self.thorns = thorns
        self.variety = variety


class Pions(Flower):
    def __init__(self, flower, petals, price, time_of_life, stem_len, color, gibrid, variety):
        super().__init__(flower, petals, price, time_of_life, stem_len, color)
        self.gibrid = gibrid
        self.variety = variety


rose = Roses(True, True, 120, 10, 80, 'Red',
             'Koko Loko', True,)
rose_yellow = Roses(True, True, 150, 5, 80, 'yellow',
                    'yellow', True,)
pion = Pions(True, True, 180, 12, 60, 'pinc', True,
             'sarah_bernhardt')
buket = [rose, rose_yellow, pion]
select_mod = (input('выбирите способ фильтрации '))


class Buqet:
    def __init__(self, buket):
        self.buket = buket

    def buqet(self):
        total = 0
        for x in self.buket:
            total += x.time_of_life
        average = total / len(self.buket)
        return print(f'среднее время жизни букета : {int(average)} дней')

    def price(self):
        price = sorted(self.buket, key=lambda x: x.price)
        return [f"{x.variety}: {x.price} руб." for x in price]

    def stems_len(self):
        stens = sorted(self.buket, key=lambda x: x.stem_len)
        return [f"{x.variety}: {x.stem_len} см." for x in stens]

    def flower_color(self):
        f_color = sorted(self.buket, key=lambda x: x.color)
        return [f"{x.variety}: {x.color} цвет" for x in f_color]

    def choose(self, choice):
        if choice == 'время':
            return self.buket()
        if choice == 'цена':
            return self.price()
        if choice == 'длинна':
            return self.stems_len()
        if choice == 'цвет':
            return self.flower_color()
        else:
            return None


my_bouquet = Buqet(buket)
print(f'{my_bouquet.choose(select_mod)}')
