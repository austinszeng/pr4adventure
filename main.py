from room import Room, Store
from item import *
from person import *
from world import *
import os
import updater

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printSituation():
    clear()
    if type(player.location) == Store:
        print("You (" + str(player.health) + "/" + str(player.maxHealth) + ") are in " + player.location.desc + " ($" + str(player.location.acquisition) + ")" + ".")
    else:
        print("You (" + str(player.health) + "/" + str(player.maxHealth) + ") are in " + player.location.desc + ".")
    print()
    if player.location.hasPersons():
        print("This room contains the following persons:")
        for m in player.location.persons:
            if m.engaged:
                print(m.name + " (" + str(m.health) + "/" + str(m.maxHealth) + ") (engaged)")
            elif m.scared:
                print(m.name + " (" + str(m.health) + "/" + str(m.maxHealth) + ") (scared)")
            else:
                print(m.name + " (" + str(m.health) + "/" + str(m.maxHealth) + ")")
        print()
    if player.location.hasItems():
        if type(player.location) == Room:
            print("This room contains the following items:")
            for i in player.location.items:
                print(i.name)
            print()
        elif type(player.location) == Store:
            player.location.displayItems()
    print("You can go in the following directions:")
    for e in player.location.exitNames():
        print(e)
    print()

def showHelp():
    clear()
    print("go <direction> -- moves you in the given direction")
    print("me -- shows stats")
    print("(i)nventory -- opens your inventory")
    print("pickup <item> -- picks up the item")
    print("drop <item> -- drop item from inventory")
    print("equip <item> -- equip an equippable item from inventory")
    print("unequip <item> -- unequip equipped item")
    print("run <direction> -- if engaged")
    print("buy <item> -- buy item from store")
    print("acquire -- buy store")
    print("sell <item> -- sell item to store")
    print("wait -- wait a turn in same location")
    print("eat <item> -- eat a eatable item to gain health")
    print("pickpocket <person> -- chance to successfully steal an item")
    print("attack <person> -- attack")
    print()
    input("Press enter to continue...")

clear()
print("Welcome to Blah blah!")
print()
input("Press enter to continue...")
clear()
print("1. Balance")
print("2. Speed")
print("3. Brawn")
acceptableInputs = ["1","2","3"]
choice = input("Which bandit would you like to be (1, 2, 3)? ")
while choice not in acceptableInputs:
    choice = input("Which bandit would you like to be (1, 2, 3)? ")
player = charChoice(choice)
clear()
createWorld(player)
playing = True
while playing and player.alive:
    if player.acquisitions == 4:
        player.win()
    printSituation()
    commandSuccess = False
    timePasses = False
    while not commandSuccess:
        commandSuccess = True
        command = input("What now? ")
        commandWords = command.split()
        if commandWords[0].lower() == "go":   #cannot handle multi-word directions
            if player.engaged == True:
                print("You can not do that right now.")
                commandSuccess = False
            else:
                player.goDirection(commandWords[1]) 
                timePasses = True
        elif commandWords[0].lower() == "pickup":  #can handle multi-word objects
            targetName = command[7:]
            target = player.location.getItemByName(targetName)
            if target != False and player.currInv < player.maxInv:
                if type(target.loc) == Merchant:
                    print("You have to buy this item.")
                    commandSuccess = False
                else:
                    player.pickup(target)
                    player.currInv += 1
            elif player.currInv >= player.maxInv:
                print("Backpack full.")
                commandSuccess = False
            else:
                print("No such item.")
                commandSuccess = False
        elif commandWords[0].lower() == "drop":  #can handle multi-word objects
            targetName = command[5:]
            target = player.getItemByName(targetName)
            if target != False:
                player.drop(target)
            else:
                print("No such item in inventory.")
                commandSuccess = False
        elif commandWords[0].lower() == "eat":
            targetName = command[4:]
            target = player.getItemByName(targetName)
            if target != False:
                player.eat(target)
            else:
                print("No such item in inventory.")
                commandSuccess = False
        elif commandWords[0].lower() == "buy":
            targetName = command[4:]
            target = player.location.getItemByName(targetName)
            if type(target.loc) == Room or type(target.loc) == Store:
                print("You don't need to buy this item.")
                commandSuccess = False
            elif target != False and player.currInv < player.maxInv:
                player.buy(target)
                player.currInv += 1
            elif player.currInv >= player.maxInv:
                print("Backpack full.")
                commandSuccess = False
            else:
                print("No such item.")
                commandSuccess = False
        elif commandWords[0].lower() == "acquire":
            if type(target.loc) == Store:
                player.acquire()
            else:
                print("This is not a store.")
                commandSuccess = False
        elif commandWords[0].lower() == "sell":
            targetName = command[5:]
            target = player.getItemByName(targetName)
            if target != False:
                player.sell(target)
                player.currInv -= 1
            else:
                print("No such item in inventory.")
                commandSuccess = False
        elif commandWords[0].lower() == "inspect":
            targetName = command[8:]
            target = player.location.getItemByName(targetName)
            if target != False:
                target.describe()
            else:
                target = player.getItemByName(targetName)
                if target != False:
                    target.describe()
                else:
                    print("No such item.")
                    commandSuccess = False
        elif commandWords[0].lower() == "inventory" or commandWords[0].lower() == "i":
            player.showInventory()        
        elif commandWords[0].lower() == "me":
            player.showStats()
        elif commandWords[0].lower() == "help":
            showHelp()
        elif commandWords[0].lower() == "exit":
            playing = False
        elif commandWords[0].lower() == "attack":
            targetName = command[7:]
            target = player.location.getPersonByName(targetName)
            if target != False:
                player.attackPerson(target)
            else:
                print("No such person.")
                commandSuccess = False
        elif commandWords[0].lower() == "pickpocket":
            targetName = command[11:]
            target = player.location.getPersonByName(targetName)
            if target != False:
                player.pickpocketPerson(target)
            else:
                print("No such person.")
                commandSuccess = False
        elif commandWords[0].lower() == "equip":
            targetName = command[6:]
            target = player.getItemByName(targetName)
            if target != False:
                player.equip(target)
            else:
                print("No such item in inventory.")
                commandSuccess = False
        elif commandWords[0].lower() == "unequip":
            targetName = command[8:]
            target = player.getEquippedByName(targetName)
            if target != False:
                player.unequip(target)
            else:
                print("No such item equipped.")
                commandSuccess = False
        elif commandWords[0].lower() == "run":
            if player.engaged == True:
                # find persons in room
                important = []
                for i in player.location.persons:
                    if i in player.engagedWith:
                        important.append(i)
                # find max speed of person(s) mad at you
                max, p = 0, None
                for person in important:
                    if person.speed > max:
                        max = person.speed
                        p = person
                if player.speed > p.speed:
                    clear()
                    print("You have successfully run away!")
                    print()
                    input("Press enter to continue...")
                    player.goDirection(commandWords[1]) 
                    # player.engaged = False
                    timePasses = True
                else: 
                    clear()
                    print("You can not run away...")
                    print()
                    input("Press enter to continue...")
                    commandSuccess = False
            # same as "go (direction)"
            else:
                player.goDirection(commandWords[1])
                timePasses = True
        elif commandWords[0].lower() == "wait" or commandWords[0].lower() == "w":
            timePasses = True   
        else:
            print("Not a valid command")
            commandSuccess = False
    if timePasses == True:
        if player.health + player.regen <= player.maxHealth:
            player.health += player.regen
        else:
            player.health = player.maxHealth
        updater.updateAll()