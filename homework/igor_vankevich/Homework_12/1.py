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

    def __init__(self, name, cost, freshness, size, life_time):
        super().__init__(name, cost, freshness, size, life_time)


class ForestFlowers(Flowers):
    type = 'forest'
    color = 'blue'

    def __init__(self, name, cost, freshness, size, life_time):
        super().__init__(name, cost, freshness, size, life_time)


class BouquetFlowers:

    def __init__(self, *flower):
        self.list_flowers = list(flower)

    def wilting_time(self):
        a = []
        for flower in self.list_flowers:
            a.append(flower.life_time)
        print(sum(a) / len(self.list_flowers))

    def sort_size(self):
        a = []
        for flower in self.list_flowers:
            a.append(flower.size)
        print(sorted(a))

    def sort_freshness(self):
        a = []
        for flower in self.list_flowers:
            a.append(flower.freshness)
        print(sorted(a))

    def sort_cost(self):
        a = []
        for flower in self.list_flowers:
            a.append(flower.cost)
        print(sorted(a))

    def sort_color(self):
        a = []
        for flower in self.list_flowers:
            a.append(flower.color)
        print(sorted(a))

    def search_name(self):
        user_input = input('enter a name\n')
        i = 0
        while i < len(self.list_flowers):
            if user_input == self.list_flowers[i].name:
                print(f'{user_input} in bouquet')
            i += 1


flower1 = GardenFlowers('rose', 12, 10, 5, 10)
flower2 = GardenFlowers('dahlias', 4, 6, 7, 10)
flower3 = WildFlowers('chamomile', 22, 11, 10, 15)
flower4 = WildFlowers('clover', 42, 9, 12, 15)
flower5 = ForestFlowers('lily', 2, 15, 15, 17)
flower6 = ForestFlowers('violet', 8, 17, 21, 17)
bouquet1 = BouquetFlowers(flower1, flower4, flower5, flower6)
BouquetFlowers.wilting_time(bouquet1)
BouquetFlowers.sort_size(bouquet1)
BouquetFlowers.sort_cost(bouquet1)
BouquetFlowers.sort_freshness(bouquet1)
BouquetFlowers.sort_color(bouquet1)
BouquetFlowers.search_name(bouquet1)
