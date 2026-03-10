class Flower:
    def __init__(self, flower, petals, price, time_of_life, stem_len, color, variety):
        self.flower = flower
        self.petals = petals
        self.time_of_life = time_of_life
        self.price = price
        self.stem_len = stem_len
        self.color = color
        self.variety = variety

    def __repr__(self):
        return f'{self.variety}' #{self.color}, {self.price}, {self.stem_len}]'

    def __str__(self):
        return self.__repr__()

class Roses(Flower):
    def __init__(self, flower, petals, price, time_of_life, stem_len, color, variety, thorns):
        super().__init__(flower, petals, price, time_of_life, stem_len, color, variety)
        self.thorns = thorns



class Pions(Flower):
    def __init__(self, flower, petals, price, time_of_life, stem_len, color, variety, gibrid ):
        super().__init__(flower, petals, price, time_of_life, stem_len, color, variety)
        self.gibrid = gibrid









rose = Roses(True, True, 120, 10, 80, 'Red',
             'Koko Loko', True,)
rose_yellow = Roses(True, True, 150, 5, 80, 'yellow',
                    'yellow', True,)
pion = Pions(True, True, 180, 12, 60, 'pinc', 'sarah_bernhardt',
             True)
buket = [rose, rose_yellow, pion]


class Buqet:
    def __init__(self, buket):
        self.buket = buket

    def average_life(self):
        total = 0
        for x in self.buket:
            total += x.time_of_life
        average = total / len(self.buket)
        return average

    def price(self):
        return sorted(self.buket, key=lambda x: x.price)


    def stems_len(self):
        return sorted(self.buket, key=lambda x: x.stem_len)


    def flower_color(self):
        return  sorted(self.buket, key=lambda x: x.color)

    def find_flower(self, s_len=None, colors=None, min_price=None ):
        result = []
        for flower in self.buket:
            if (colors is None or flower.color == colors) and (min_price is None or flower.price <= min_price) \
                and (s_len is None or flower.stem_len <= s_len):
                result.append(flower)
        return result

my_buqet = Buqet(buket)

print(my_buqet.find_flower(colors='Red'))
