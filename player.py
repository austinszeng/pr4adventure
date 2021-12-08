import os, random
from person import *
from item import *
from misc import *

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self, health, regen, damage, speed, cunning, evasion):
        self.location = None
        self.items = []
        self.alive = True
        self.engaged = False
        self.engagedWith = []
        self.maxHealth = health
        self.health = health
        self.regen = regen
        self.damage = damage
        self.speed = speed
        self.cunning = cunning
        self.evasion = evasion
        self.money = 5
        self.clothes = None
        self.shoes = None
        self.weapon = None
        # self.disguise = None
        # self.disguised = False
        self.maxInv = 5
        self.currInv = 0
        self.acquisitions = 0
    def goDirection(self, direction):
        self.location = self.location.getDestination(direction)
    def pickup(self, item):
        self.items.append(item)
        item.loc = self
        self.location.removeItem(item)
    def drop(self, item):
        item.loc = self.location
        self.items.remove(item)
        self.currInv -= 1
        self.location.addItem(item)
    def buy(self, item):
        clear()
        if self.money >= item.price:
            self.pickup(item)
            self.money -= item.price
            print("You bought " + item.name + "!")
        else:
            print("Not enough money.")
        print()
        input("Press enter to continue...")
    def acquire(self, store):
        clear()
        if self.money >= store.acquisition:
            if store.hasPersons():
                for person in store.persons:
                    if type(person) == Merchant:
                        # drop all of merchant's items so that its pickupable
                        for i in person.items:
                            i.putInRoom(self.location)
                            person.items.remove(i)
                        # remove merchant from game
                        store.removePerson(person)
            self.money -= store.acquisition
            self.acquisitions += 1
            print("You acquired " + store.desc + "for $" + str(store.acquisition) + "!")
        else:
            print("Not enough money.")
        print()
        input("Press enter to continue...")
    def sell(self, item):
        clear()
        self.drop(item)
        self.money += item.sellPrice
        print("You sold " + item.name + " for $" + str(item.sellPrice) + ".")
        print()
        input("Press enter to continue...")
    def showInventory(self):
        clear()
        print("You are currently carrying:")
        print()
        newList = self.items.copy()
        for i in self.items:
            if self.items.count(i) > 1:
                for _ in range(self.items.count(i)):
                    newList.remove(i)
                    print(i.name + "(x" + str(self.items.count(i)) + ")")
        for i in newList:
            print(i.name)
        print()
        print("Space: " + str(self.currInv) + "/" + str(self.maxInv))
        print()
        input("Press enter to continue...")
    def showStats(self):
        clear()
        print("Stats:")
        print()
        print("Health: " + str(self.health) + "/" + str(self.maxHealth))
        print("Regen: " + str(self.regen))
        print("Money: " + str(self.money))
        print("Damage: " + str(self.damage))
        print("Speed: " + str(self.speed))
        print("Cunning: " + str(self.cunning))
        print("Evasion: " + str(self.evasion))
        print()
        print("Equipment:")
        print()
        if self.clothes is not None:
            print("Clothes: " + self.clothes.name)
        else:
            print("Clothes: None")
        if self.shoes is not None:
            print("Shoes: " + self.shoes.name)
        else:
            print("Shoes: None")
        if self.weapon is not None:
            print("Weapon: " + self.weapon.name)
        else:
            print("Weapon: None")
        # if self.disguise is not None:
        #     print("Disguise: " + self.disguise.name)
        # else:
        #     print("Disguise: None")
        print()
        input("Press enter to continue...")
    def losingScreen(self):
        print("Final stats:")
        # show acquisitions and money and equipment and stats
    def winningScreen(self):
        print("You acquired all of the stores and beat the game!")
        print("You now rule over the city!")
        print()
        self.losingScreen()
    def die(self):
        print("You died.")
        print()
        self.losingScreen()
        self.alive = False
    def lose(self):
        print("You lose.")
        print()
        self.losingScreen()
        self.alive = False
    def win(self):
        print("You won!")
        print()
        self.winningScreen()
        self.alive = False
    def attack(self, person):
        variability = 5
        dmg = random.randint(self.damage - variability, self.damage + variability) 
        print("You attack " + person.name + " for " + str(dmg) + " damage.")
        if person.health - dmg > 0:
            person.health -= dmg
        else:
            person.die()
    def attackPerson(self, person):
        self.engaged = True
        if person not in self.engagedWith:
            self.engagedWith.append(person)
        clear()
        print("You (" + str(self.health) + "/" + str(self.maxHealth) + ") are attacking " \
            + person.name + " (" + str(person.health) + "/" + str(person.maxHealth) + ").")
        print()
        # You attack first if faster or person is unaware
        if self.speed > person.speed or person.engaged == False: 
            self.attack(person)
            if person.alive == True:
                person.attack(self)
        # Person attacks first
        else:
            person.attack(self)
            if self.alive == True:
                self.attack(person)
        person.engaged = True
        person.scared = False
        print()
        input("Press enter to continue...")
    def pickpocketPerson(self, person):
        clear()
        print("You are pickpocketing " + person.name)
        print()
        # successful --> steal an item from them
        if random.uniform(0.0,1.0) + ((self.cunning/100)/2) > person.attentive and person.engaged == False:
            # random chance to either steal an item or take their money
            n = random.randint(1,4)
            if person.items != [] and self.currInv < self.maxInv:
                if n != 4:
                    item = random.choice(person.items)
                    person.items.remove(item)
                    self.items.append(item)
                    item.loc = self
                    self.currInv += 1
                    print("You pickpocketed " + item.name + " from " + person.name + "!")
                else:
                    if person.money != 0:
                        print("You took $" + str(person.money) + " from " + person.name + "!")
                        person.money = 0
                    # if no money cuz already pickpocketed, then get $0
                    else:
                        print("You already took " + person.name + "'s money.")
            elif self.currInv >= self.maxInv:
                print("Your backpack is full...")
            else:
                print(person.name + " has nothing...")
            # successful pickpocket regardless of if they have nothing or if backpack full increases cunning
            r = random.randint(3,6)
            self.cunning += r
            print("Your cunning went up by " + str(r) + "!")
            
        else:
            print(person.name + " noticed!")
            print()
            person.engaged = True
            person.scared = False
            if person not in self.engagedWith:
                self.engagedWith.append(person)
            # fighting ensues
            if random.uniform(0.0,1.0) <= person.anger:
                self.engaged = True
                # if their speed is higher
                if self.speed/person.speed < 1.0:
                    person.attack(self)
                else:
                    # percent chance to dodge it or something
                    if random.uniform(0.0,1.0) > person.speed/self.speed:
                        print(person.name + " tries to attack you but you dodge them.")
                    else:
                        person.attack(self)
            # person is scared, an enforcer is added to the map
            else:
                person.scared = True
                person.engaged = False
                print(person.name + " is scared and calls an enforcer to the city.")
                # add an extra enforcer on the map that is constantly engaged
                enforcer = random.choice(allEnforcers)
                enforcer.room.addPerson(enforcer)
                enforcer.onMap = True
        print()
        input("Press enter to continue...")

    def equip(self, item):
        clear()
        if type(item) == Clothes and self.clothes == None:
            self.clothes = item
            self.currInv -= 1
            self.health += item.health
            self.maxHealth += item.health
            self.items.remove(item)
            print("You put on " + item.name + " (+" + str(item.health) + " HP)")
        elif type(item) == Shoes and self.shoes == None:
            self.shoes = item
            self.currInv -= 1
            self.speed += item.speed
            self.items.remove(item)
            print("You put on " + item.name + " (+" + str(item.speed) + " SPD)")
        elif type(item) == Weapon and self.weapon == None:
            self.weapon = item
            self.currInv -= 1
            self.damage += item.damage
            self.items.remove(item)
            print("You put on " + item.name + " (+" + str(item.damage) + " DMG)")
        # elif type(item) == Disguise and self.disguise == None:
        #     self.disguise = item
        #     self.currInv -= 1
        #     self.disguised = True
        #     self.items.remove(item)
        #     print("You put on " + item.name + " and are now disguised.")
        else:
            print("Your item is not equipable or you already have an item equipped in that slot.")
        print()
        input("Press enter to continue...")

    def unequip(self, item):
        clear()
        if self.currInv < self.maxInv:
            if type(item) == Clothes and self.clothes != None:
                self.clothes = None
                self.currInv += 1
                self.health -= item.health
                self.maxHealth -= item.health
                self.items.append(item)
                print("You took off " + item.name + " (-" + str(item.health) + " HP)")
            elif type(item) == Shoes and self.shoes != None:
                self.shoes = None
                self.currInv += 1
                self.speed -= item.speed
                self.items.append(item)
                print("You took off " + item.name + " (-" + str(item.health) + " EVA)")
            elif type(item) == Weapon and self.weapon == None:
                self.weapon = None
                self.currInv += 1
                self.damage -= item.damage
                self.items.append(item)
                print("You took off " + item.name + " (-" + str(item.damage) + " DMG)")
            # elif type(item) == Disguise and self.disguise != None:
            #     self.disguise = None
            #     self.currInv += 1
            #     self.disguised = False
            #     self.items.append(item)
            #     print("You took off " + item.name + " and are now undisguised.")
        else:
            print("Your inventory is full.")
        print()
        input("Press enter to continue...")

    def getItemByName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False

    def getEquippedByName(self, name):
        if name.lower() == self.clothes.name.lower():
            return self.clothes
        elif name.lower() == self.shoes.name.lower():
            return self.shoes
        elif name.lower() == self.disguise.name.lower():
            return self.disguise
        return False

    def eat(self, item):
        clear()
        # can only eat if not in room with engaged person
        if type(item) == Food:
            healthGained = item.healing
            if self.health == self.maxHealth:
                print("Your health is already full!")
            elif self.health + item.healing <= self.maxHealth:
                self.health += item.healing
                self.items.remove(item)
                self.currInv -= 1
                print("You eat " + item.name + " and gain " + str(healthGained) + " health!")
            else:
                healthGained = self.maxHealth - self.health
                self.health = self.maxHealth
                self.items.remove(item)
                self.currInv -= 1
                print("You eat " + item.name + " and gain " + str(healthGained) + " health!")
        else:
            print("Your item is not eatable.")
        print()
        input("Press enter to continue...")