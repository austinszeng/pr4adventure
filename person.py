import random
import updater

class Person:
    def __init__(self, name, room, items):
        self.name = name
        self.alive = True
        r = random.randint(75,125)
        self.health = r
        self.maxHealth = r
        self.attentive = random.uniform(0.1,0.3)
        self.damage = random.randint(10,15)
        self.speed = random.randint(30,60)
        self.anger = random.uniform(0.25, 0.75)
        self.engaged = False
        self.scared = False
        self.room = room
        room.addPerson(self)
        self.items = items
        self.money = random.randint(1,50)
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
        for i in self.items:
            self.room.addItem(i)       
        self.room.removePerson(self)
        self.alive = False
        updater.deregister(self)
    def attack(self, player):
        self.engaged = True
        variability = 5
        dmg = random.randint(self.damage - variability, self.damage + variability) 
        print(self.name + " attacks you for " + str(dmg) + " damage.")
        if player.health - dmg > 0:
            player.health -= dmg
        else:
            player.die()

class Enforcer(Person):
    # needed to change whole init so room doesn't automatically addPerson
    def __init__(self, name, room, items):
        self.name = name
        self.alive = True
        r = random.randint(125,250)
        self.health = r
        self.maxHealth = r
        self.attentive = random.uniform(0.4,0.8)
        self.damage = random.randint(20,50)
        self.speed = random.randint(50,80)
        self.cunning = random.randint(5,15) # additional attribute
        self.anger = random.uniform(0.25, 0.75)
        self.room = room
        self.items = items
        self.money = random.randint(1,50)
        self.engaged = True
        self.onMap = False
        updater.register(self)

    def update(self):
        if self.onMap and random.random() < .5:
            self.moveTo(self.room.randomNeighbor())

class Merchant(Person):
    def __init__(self, name, room, items):
        Person.__init__(self, name, room, items)
        self.attentive = random.uniform(0.25,0.5)
        for i in items:
            i.putInRoom(self.room) # put in room so items can be displayed
        self.items = []
    def sell(self, item):
        self.room.items.remove(item)
    def update(self):
        # don't move from shop
        pass
