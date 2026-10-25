# zad_3
class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (
            f'Nieruchomość o powierzchni {self.area}, '
            f'ilość pokojów {self.rooms}, '
            f'w cenie {self.price}, znajdująca się w {self.address}'
        )


class House(Property):
    def __init__(self, area, rooms, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'Dom na działce {self.plot}'


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Mieszkanie na {self.floor} piętrze'


house1 = House(100, 4, 200000, '30-220 Chicago 42', 3000)
flat1 = Flat(42, 2, 500000, '34-234 Los Angeles 20', 4)

print(house1)
print(flat1)
