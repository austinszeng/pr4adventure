import os, random
from person import *
from item import *
from misc import *

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self, health, regen, damage, speed, cunning):
        self.location = None
        self.items = []
        self.alive = True
        self.engagedWith = []
        self.maxHealth = health
        self.health = health
        self.regen = regen
        self.damage = damage
        self.speed = speed
        self.cunning = cunning
        self.money = 5
        self.clothes = None
        self.shoes = None
        self.weapon = None
        self.disguise = None
        self.maxInv = 5
        self.currInv = 0
        self.acquisitions = 0
    def goDirection(self, direction):
        loc = self.location.getDestination(direction)
        if loc != False:
            self.location = loc
        else:
            return False
    def testGoDirection(self, direction):
        loc = self.location.getDestination(direction)
        if loc != False:
            return True
        else:
            return False
    def pickup(self, item):
        self.items.append(item)
        self.currInv += 1
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
            self.currInv += 1
            print("You bought " + item.name + "!")
        else:
            print("Not enough money.")
        print()
        input("Press enter to continue...")
    def acquire(self):
        clear()
        if self.money >= self.location.acquisition:
            if self.location.hasPersons():
                for person in self.location.persons:
                    if type(person) == Merchant:
                        # remove merchant from game
                        self.location.removePerson(person)
            self.money -= self.location.acquisition
            self.acquisitions += 1
            self.location.acquired = True
            print("You acquired " + self.location.desc + " for $" + str(self.location.acquisition) + "!")
        else:
            print("Not enough money.")
        print()
        input("Press enter to continue...")
    def sell(self, item):
        clear()
        self.drop(item)
        self.money += item.sellPrice
        print("You sold " + item.name + " for $" + str(item.sellPrice) + ".")
        item.sellPrice = round(item.price * 0.75, 2)
        print()
        input("Press enter to continue...")

    def helperStats(self, item, name):
        # show stats increased/ decreased if equipped instead 
        # displays name for inventory info
        if name == True:
            s = item.name 
        # name == False displays description rather than name (for inspect command)
        else:
            s = item.desc
        if type(item) == Weapon:
            if self.weapon != None:
                diff = item.damage - self.weapon.damage
                if diff > 0:
                    s += " (+" + str(diff)
                else:
                    s += " (-" + str(diff) 
            else:
                s += " (+" + str(item.damage) 
            s += " DMG)"
        elif type(item) == Clothes:
            if self.clothes != None:
                diff = item.health - self.clothes.health
                if diff > 0:
                    s += " (+" + str(diff)
                else:
                    s += " (-" + str(diff)
            else:
                s += " (+" + str(item.health) 
            s += " HP)"
        elif type(item) == Shoes:
            if self.shoes != None:
                diff = item.speed - self.shoes.speed
                if diff > 0:
                    s += " (+" + str(diff)
                else:
                    s += " (-" + str(diff)
            else:
                s += " (+" + str(item.speed)
            s += " SPD)"
        elif type(item) == Food:
            s += " (Heal " + str(item.healing) + " HP)"
        elif type(item) == Disguise:
            s += " (Disguise)"
        s += " [$" + str(item.sellPrice) + "]"
        return s

    def showInventory(self):
        clear()
        print("You are currently carrying:")
        print()
        numOccurences = {}
        for item in self.items:
            if item in numOccurences:
                numOccurences[item] += 1
            else:
                numOccurences[item] = 1
        for item in numOccurences:
            if numOccurences[item] > 1:
                s = self.helperStats(item, True)
                s += " x" + str(numOccurences[item])
                print(s)
            else:
                s = self.helperStats(item, True)
                print(s)
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
        print("Money: $" + str(self.money))
        print("Damage: " + str(self.damage))
        print("Speed: " + str(self.speed))
        print("Cunning: " + str(self.cunning))
        print()
        print("Equipment:")
        print()
        if self.clothes is not None:
            print("Clothes: " + self.clothes.name)
        else:
            print("Clothes: ")
        if self.shoes is not None:
            print("Shoes: " + self.shoes.name)
        else:
            print("Shoes: ")
        if self.weapon is not None:
            print("Weapon: " + self.weapon.name)
        else:
            print("Weapon: ")
        if self.disguise is not None:
            print("Disguise: " + self.disguise.name)
        else:
            print("Disguise: ")
        print()
        input("Press enter to continue...")
    def inspect(self, item):
        s = self.helperStats(item, False)
        clear()
        print(s)
        print()
        input("Press enter to continue...")
    def losingScreen(self):
        print("Final stats:")
        print()
        print("Acquisitions: " + str(self.acquisitions) + "/" + str(4))
        peopleLeft = 0
        for room in allRooms:
            if room.hasPersons():
                peopleLeft += len(room.persons)
        # since there are always 20 people + len(enforcersAdded)
        print("People left: " + str(peopleLeft) + "/" + str(20 + len(enforcersAdded)) )
        print()
        print("Health: " + str(self.health) + "/" + str(self.maxHealth))
        print("Regen: " + str(self.regen))
        print("Money: $" + str(self.money))
        print("Damage: " + str(self.damage))
        print("Speed: " + str(self.speed))
        print("Cunning: " + str(self.cunning))
        print()
        print("Equipment:")
        print()
        if self.clothes is not None:
            print("Clothes: " + self.clothes.name)
        else:
            print("Clothes: ")
        if self.shoes is not None:
            print("Shoes: " + self.shoes.name)
        else:
            print("Shoes: ")
        if self.weapon is not None:
            print("Weapon: " + self.weapon.name)
        else:
            print("Weapon: ")
        if self.disguise is not None:
            print("Disguise: " + self.disguise.name)
        else:
            print("Disguise: ")
        print()
        input("Press enter to exit the game...")
    def winningScreen(self):
        clear()
        print("You acquired all of the stores and beat the game!")
        print("You now rule the city!")
        print()
        self.losingScreen()
    def die(self):
        print()
        print("You died.")
        print()
        input("Press enter to continue...")
        clear()
        self.losingScreen()
        self.alive = False
    def win(self):
        print()
        print("You won!")
        print()
        input("Press enter to continue...")
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
    def chanceDodge(self, person):
        # percent chance to dodge based on speed
        if random.random() > person.speed/self.speed:
            print(person.name + " tries to attack you but you dodge them.")
        else:
            person.attack(self)
    def personChanceDodge(self, person):
        # percent chance to dodge based on speed
        if random.random() > self.speed/person.speed:
            print("You try to attack " + person.name + " but they dodge you.")
        else:
            self.attack(person)
    def personMad(self, person):
        person.engaged = True
        person.scared = False
        if person not in self.engagedWith:
            print(person.name + " is mad and gets ready to fight you.")
            self.engagedWith.append(person)
    def personScared(self, person):
        person.scared = True
        person.engaged = False
        print(person.name + " is scared and calls an enforcer to the city.")
        # add an extra enforcer on the map that is constantly engaged
        if allEnforcers != []:
            enforcer = random.choice(allEnforcers)
            allEnforcers.remove(enforcer)
        else:
            enforcer = Enforcer("Trooper", random.choice(allRooms), random.sample(enforcer_items, random.randint(1,3)))
        # enforcer.room.addPerson(enforcer)
        # for testing
        enforcersAdded.append(enforcer)
        enforcer.room = self.location
        self.location.addPerson(enforcer)
        updater.register(enforcer)
        self.engagedWith.append(enforcer)
    def attackPerson(self, person):
        clear()
        print("You (" + str(self.health) + "/" + str(self.maxHealth) + ") are attacking " \
            + person.name + " (" + str(person.health) + "/" + str(person.maxHealth) + ").")
        print()
        # if person unaware, free attack
        if person.engaged == False and person.scared == False:
            self.attack(person)
            if random.random() <= person.anger:
                self.personMad(person)
            # chance for person to call an enforcer 
            else:
                self.personScared(person)
        # chance for scared person to get mad
        elif person.scared == True:
            self.attack(person)
            if random.random() <= person.anger:
                self.personMad(person)
        # last two happen if person is engaged
        # You attack first if faster 
        elif self.speed > person.speed: 
            self.attack(person)
            if person.alive == True:
                self.chanceDodge(person)
        # if person is faster, attack first
        else:
            # no chance dodging since person.speed/self.speed > 1.0
            person.attack(self)
            if self.alive == True:
                self.personChanceDodge(person)
        print()
        input("Press enter to continue...")
    def increaseCunning(self):
        r = random.randint(3,6)
        self.cunning += r
        print("Your cunning went up by " + str(r) + "!")
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
                    self.increaseCunning()
                else:
                    if person.money != 0:
                        print("You took $" + str(person.money) + " from " + person.name + "!")
                        person.money = 0
                        self.increaseCunning()
                    # if no money cuz already pickpocketed, then get $0
                    else:
                        print("You already took " + person.name + "'s money.")
            # if merchant (technically carries no items), then just steal an item from the shop
            elif type(person) == Merchant and self.location.items != [] and self.currInv < self.maxInv:
                if n != 4:
                    item = random.choice(self.location.items)
                    self.location.items.remove(item)
                    self.items.append(item)
                    item.loc = self
                    self.currInv += 1
                    print("You pickpocketed " + item.name + " from " + person.name + "!")
                    self.increaseCunning()
                else:
                    if person.money != 0:
                        print("You took $" + str(person.money) + " from " + person.name + "!")
                        person.money = 0
                        self.increaseCunning()
                    # if no money cuz already pickpocketed, then get $0
                    else:
                        print("You already took " + person.name + "'s money.")
            elif self.currInv >= self.maxInv:
                print("Your backpack is full...")
            else:
                print(person.name + " has nothing...")
            
        else:
            print(person.name + " noticed!")
            print()
            # first encounter
            if person.engaged == False and person.scared == False:
                # fighting ensues
                if random.random() <= person.anger:
                    self.personMad(person)
                    # if their speed is higher
                    if person.speed > self.speed:
                        person.attack(self)
                    else:
                        self.chanceDodge(person)
                # person is scared, an enforcer is added to the map
                else:
                    self.personScared(person)
            # chance for scared person to get mad or stay scared
            elif person.scared == True:
                if random.random() <= person.anger:
                    self.personMad(person)
                else:
                    print(person.name + " is still scared of you.")
            # they attack you if they notice and are already engaged
            elif person.engaged == True:
                # if their speed is higher
                if person.speed > self.speed:
                    person.attack(self)
                else:
                    self.chanceDodge(person)
        print()
        input("Press enter to continue...")

    def runSuccess(self, p):
        clear()
        print("You have successfully run away from " + p.name + "!")
        print()
        input("Press enter to continue...")
    
    def runFail(self, p):
        clear()
        print("You can not run away...")
        print()
        if p.speed > self.speed:
            p.attack(self)
        else:
            self.chanceDodge(p)
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
        elif type(item) == Disguise and self.disguise == None:
            self.disguise = item
            self.currInv -= 1
            self.items.remove(item)
            print("You put on " + item.name + " and are now disguised.")
        else:
            print("Your item is not equipable or you already have an item equipped in that slot.")
        print()
        input("Press enter to continue...")

    def unequip(self, item):
        clear()
        if self.currInv < self.maxInv:
            if type(item) == Clothes:
                self.clothes = None
                self.currInv += 1
                self.health -= item.health
                self.maxHealth -= item.health
                self.items.append(item)
                print("You took off " + item.name + " (-" + str(item.health) + " HP)")
            elif type(item) == Shoes:
                self.shoes = None
                self.currInv += 1
                self.speed -= item.speed
                self.items.append(item)
                print("You took off " + item.name + " (-" + str(item.speed) + " EVA)")
            elif type(item) == Weapon:
                self.weapon = None
                self.currInv += 1
                self.damage -= item.damage
                self.items.append(item)
                print("You took off " + item.name + " (-" + str(item.damage) + " DMG)")
            elif type(item) == Disguise:
                self.disguise = None
                self.currInv += 1
                self.items.append(item)
                print("You took off " + item.name + " and are now undisguised.")
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
        if self.clothes != None:
            if name.lower() == self.clothes.name.lower():
                return self.clothes
        if self.shoes != None:
            if name.lower() == self.shoes.name.lower():
                return self.shoes
        if self.disguise != None:
            if name.lower() == self.disguise.name.lower():
                return self.disguise
        if self.weapon != None:
            if name.lower() == self.weapon.name.lower():
                return self.weapon
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