import os, random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, name, desc, price):
        self.name = name
        self.desc = desc
        r = round(random.uniform(price - price/2, price + price/2), 2)
        self.price = r
        self.sellPrice = round(price * 0.75, 2)
        self.loc = None
    def describe(self):
        clear()
        print(self.desc)
        print()
        input("Press enter to continue...")
    def putInRoom(self, room):
        self.loc = room
        room.addItem(self)

class Weapon(Item):
    def __init__(self, name, desc, price, damage):
        Item.__init__(self, name, desc, price)
        self.damage = damage

class Clothes(Item):
    def __init__(self, name, desc, price, health):
        Item.__init__(self, name, desc, price)
        self.health = health

class Shoes(Item):
    def __init__(self, name, desc, price, speed):
        Item.__init__(self, name, desc, price)
        self.speed = speed

class Food(Item):
    def __init__(self, name, desc, price, healing):
        Item.__init__(self, name, desc, price)
        self.healing = healing


# class Disguise(Item):
#     used = False