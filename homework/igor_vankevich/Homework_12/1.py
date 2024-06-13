class Flowers:
    kind = 'plants'

    def __init__(self, cost, freshness, size, life_time):
        self.cost = cost
        self.freshness = freshness
        self.size = size
        self.life_time = life_time


class GardenFlowers(Flowers):
    type = 'garden'
    color = 'red'

    def __init__(self, cost, freshness, size, life_time, name):
        super().__init__(cost, freshness, size, life_time)
        self.name = name


class WildFlowers(Flowers):
    type = 'wild'
    color = 'green'

    def __init__(self, cost, freshness, size, life_time, name):
        super().__init__(cost, freshness, size, life_time)
        self.name = name


class ForestFlowers(Flowers):
    type = 'forest'
    color = 'blue'

    def __init__(self, cost, freshness, size, life_time, name):
        super().__init__(cost, freshness, size, life_time)
        self.name = name


class BouquetFlowers:

    list_flowers = []

    def __init__(self, flowers1, flowers2, flowers3, flowers4):
        self.flowers1 = flowers1
        self.flowers2 = flowers2
        self.flowers3 = flowers3
        self.flowers4 = flowers4
        list_flowers = [flowers1, flowers2, flowers3, flowers4]
        for x in list_flowers:
            BouquetFlowers.list_flowers.append(x)
        print(f'Cost bouquet = {flowers1.cost + flowers2.cost + flowers3.cost + flowers4.cost}')

    def wilting_time(self):
        wilting = (self.flowers1.life_time + self.flowers2.life_time + self.flowers3.life_time
                   + self.flowers4.life_time) / 4
        return print(f'Wilting = {wilting}')

    def sort_size(self):
        print(', '.join(map(str, sorted([self.flowers1.size, self.flowers2.size, self.flowers3.size,
                                         self.flowers4.size]))))

    def sort_freshness(self):
        print(', '.join(map(str, sorted([self.flowers1.freshness, self.flowers2.freshness, self.flowers3.freshness,
                                         self.flowers4.freshness]))))

    def sort_cost(self):
        print(', '.join(map(str, sorted([self.flowers1.cost, self.flowers2.cost, self.flowers3.cost,
                                         self.flowers4.cost]))))

    def sort_color(self):
        print(', '.join(sorted([self.flowers1.color, self.flowers2.color, self.flowers3.color, self.flowers4.color])))

    def search_name(self):
        user_input = input('enter a name\n')
        if user_input == self.flowers1.name or self.flowers2.name or self.flowers2.name or self.flowers3.name\
                or self.flowers4.name:
            print(f'{user_input} in bouquet')
        else:
            print('the parameter will not find')


flower1 = GardenFlowers(12, 10, 5, 10, 'rose')
flower2 = GardenFlowers(4, 6, 7, 10, 'dahlias')
flower3 = WildFlowers(22, 11, 10, 15, 'chamomile')
flower4 = WildFlowers(42, 9, 12, 15, 'clover')
flower5 = ForestFlowers(2, 15, 15, 17, 'lily')
flower6 = ForestFlowers(8, 17, 21, 17, 'violet')
bouquet1 = BouquetFlowers(flower1, flower4, flower5, flower6)
BouquetFlowers.wilting_time(bouquet1)
BouquetFlowers.sort_size(bouquet1)
BouquetFlowers.sort_cost(bouquet1)
BouquetFlowers.sort_freshness(bouquet1)
BouquetFlowers.sort_color(bouquet1)
BouquetFlowers.search_name(bouquet1)
