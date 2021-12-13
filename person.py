import random
import updater

class Person:
    def __init__(self, name, room, items):
        self.name = name
        self.alive = True
        r = random.randint(75,120)
        self.health = r
        self.maxHealth = r
        self.attentive = random.uniform(0.15,0.35)
        self.damage = random.randint(8,13)
        self.speed = random.randint(30,56)
        self.anger = random.uniform(0.40, 0.70) # so on average, there's a higher chance to fight
        self.engaged = False
        self.scared = False
        self.room = room
        room.addPerson(self)
        self.items = items
        self.money = random.randint(1,75)
        updater.register(self)
    def update(self):
        if random.random() < .5:
            self.moveTo(self.room.randomNeighbor())
    def moveTo(self, room):
        self.room.removePerson(self)
        self.room = room
        room.addPerson(self)
    def die(self):
        print(self.name + " has been killed...their items and blood are spilled on the ground.")
        print("You quickly pick up their $" + str(self.money) + " before it gets soaked.")
        for i in self.items:
            self.room.addItem(i)       
        self.room.removePerson(self)
        self.alive = False
        updater.deregister(self)
    def attack(self, player):
        self.engaged = True
        variability = self.damage // 5
        dmg = random.randint(self.damage - variability, self.damage + variability) 
        print(self.name + " attacks you for " + str(dmg) + " damage.")
        if player.health - dmg > 0:
            player.health -= dmg
        else:
            player.health = 0
            player.die()

class Enforcer(Person):
    # needed to change whole init so room doesn't automatically addPerson
    def __init__(self, name, room, items):
        self.name = name
        self.alive = True
        r = random.randint(125,190)
        self.health = r
        self.maxHealth = r
        self.attentive = random.uniform(0.4,0.75)
        self.damage = random.randint(15,23)
        self.speed = random.randint(47,67)
        self.anger = 1.0 # Enforcer always will attack you if you try to pickpocket and fail
        self.money = random.randint(50,125)
        self.engaged = True
        self.scared = False
        self.room = room
        self.items = items
    def update(self):
        if random.random() < .5:
            self.moveTo(self.room.randomNeighbor())

class Merchant(Person):
    def __init__(self, name, room, items):
        Person.__init__(self, name, room, items)
        self.attentive = random.uniform(0.3,0.6)
        for i in items:
            i.putInRoom(self.room) # put in room so items can be displayed
        self.items = []
    def sell(self, item):
        self.room.items.remove(item)
    def update(self):
        # don't move from shop
        pass
