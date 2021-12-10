import os, random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, name, desc, price):
        self.name = name
        self.desc = desc
        r = round(random.uniform(price - price/5, price + price/5))
        self.price = r
        self.sellPrice = round(r * 0.75, 2)
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
        r = round(random.uniform(damage - damage/5, damage + damage/5))
        self.damage = r

class Clothes(Item):
    def __init__(self, name, desc, price, health):
        Item.__init__(self, name, desc, price)
        r = round(random.uniform(health - health/5, health + health/5))
        self.health = r

class Shoes(Item):
    def __init__(self, name, desc, price, speed):
        Item.__init__(self, name, desc, price)
        r = round(random.uniform(speed - speed/5, speed + speed/5))
        self.speed = r

class Food(Item):
    def __init__(self, name, desc, price, healing):
        Item.__init__(self, name, desc, price)
        r = round(random.uniform(healing - healing/5, healing + healing/5))
        self.healing = r

class Disguise(Item):
    used = False