class Flowers:
    kind = 'plants'

    def __init__(self, name, cost, freshness, size, life_time):
        self.name = name
        self.cost = cost
        self.freshness = freshness
        self.size = size
        self.life_time = life_time


class GardenFlowers(Flowers):
    type = 'garden'
    color = 'red'

    def __init__(self, name, cost, freshness, size, life_time):
        super().__init__(name, cost, freshness, size, life_time)


class WildFlowers(Flowers):
    type = 'wild'
    color = 'green'

    def __init__(self, name,  cost, freshness, size, life_time):
        super().__init__(name, cost, freshness, size, life_time)


class ForestFlowers(Flowers):
    type = 'forest'
    color = 'blue'

    def __init__(self, name,  cost, freshness, size, life_time):
        super().__init__(name, cost, freshness, size, life_time)


class BouquetFlowers:

    list_flowers = []

    def __init__(self, *flower):
        for x in flower:
            BouquetFlowers.list_flowers.append(x)

    @staticmethod
    def wilting_time():
        i = 0
        a = []
        while i < len(BouquetFlowers.list_flowers):
            a.append(BouquetFlowers.list_flowers[i].life_time)
            i += 1
        print(sum(a) / len(BouquetFlowers.list_flowers))

    @staticmethod
    def sort_size():
        i = 0
        a = []
        while i < len(BouquetFlowers.list_flowers):
            a.append(BouquetFlowers.list_flowers[i].size)
            i += 1
        print(sorted(a))

    @staticmethod
    def sort_freshness():
        i = 0
        a = []
        while i < len(BouquetFlowers.list_flowers):
            a.append(BouquetFlowers.list_flowers[i].freshness)
            i += 1
        print(sorted(a))

    @staticmethod
    def sort_cost():
        i = 0
        a = []
        while i < len(BouquetFlowers.list_flowers):
            a.append(BouquetFlowers.list_flowers[i].cost)
            i += 1
        print(sorted(a))

    @staticmethod
    def sort_color():
        i = 0
        a = []
        while i < len(BouquetFlowers.list_flowers):
            a.append(BouquetFlowers.list_flowers[i].color)
            i += 1
        print(sorted(a))

    @staticmethod
    def search_name():
        user_input = input('enter a name\n')
        i = 0
        while i < len(BouquetFlowers.list_flowers):
            if user_input == BouquetFlowers.list_flowers[i].name:
                print(f'{user_input} in bouquet')
            i += 1


flower1 = GardenFlowers('rose', 12, 10, 5, 10)
flower2 = GardenFlowers('dahlias', 4, 6, 7, 10)
flower3 = WildFlowers('chamomile', 22, 11, 10, 15)
flower4 = WildFlowers('clover', 42, 9, 12, 15)
flower5 = ForestFlowers('lily', 2, 15, 15, 17)
flower6 = ForestFlowers('violet', 8, 17, 21, 17)
bouquet1 = BouquetFlowers(flower1, flower4, flower5, flower6)
BouquetFlowers.wilting_time()
BouquetFlowers.sort_size()
BouquetFlowers.sort_cost()
BouquetFlowers.sort_freshness()
BouquetFlowers.sort_color()
BouquetFlowers.search_name()
