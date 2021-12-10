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
        if player.location.acquired == False:
            print("You (" + str(player.health) + "/" + str(player.maxHealth) + ") are in " + player.location.desc + " ($" + str(player.location.acquisition) + ")" + ".")
        else:
            print("You (" + str(player.health) + "/" + str(player.maxHealth) + ") are in " + player.location.desc + ".")
    else:
        print("You (" + str(player.health) + "/" + str(player.maxHealth) + ") are in " + player.location.desc + ".")
    print()
    if player.location.hasPersons():
        print("This room contains the following persons:")
        for m in player.location.persons:
            s = m.name + " (" + str(m.health) + "/" + str(m.maxHealth) + ")"
            if type(m) == Merchant:
                s += " (Merchant)"
            if m.engaged:
                s += " (engaged)"
            elif m.scared:
                s += " (scared)"
        print(s)
        print()
    if player.location.hasItems():
        if type(player.location) == Room:
            print("This room contains the following items:")
            numOccurences = {}
            for item in player.location.items:
                if item in numOccurences:
                    numOccurences[item] += 1
                else:
                    numOccurences[item] = 1
            for item in numOccurences:
                if numOccurences[item] > 1:
                    print(item.name + " (x" + str(numOccurences[item]) + ")")
                else:
                    print(item.name)
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
    winCondition = True
    for i in allRooms:
        if i.persons != []:
            winCondition = False
    if player.acquisitions == 4 or winCondition == True:
        player.win()
    printSituation()
    commandSuccess = False
    timePasses = False
    while not commandSuccess:
        commandSuccess = True
        while True:
            command = input("What now? ")
            try:
                command = str(command)
            except IndexError:
                print("What now? ")
                continue
            if str(command):
                break
        commandWords = command.split()
        if commandWords[0].lower() == "go":   #cannot handle multi-word directions
            hasEnforcer = False
            if player.location.hasPersons():
                # find mad persons in room
                important = []
                for i in player.location.persons:
                    if i in player.engagedWith:
                        important.append(i)
                # check if enforcer is in room
                if important != []:
                    for person in important:
                        if type(person) == Enforcer:
                            hasEnforcer = True
                    if hasEnforcer == True:
                        # disguise is used up if you pass an enforcer
                        if player.disguise != None:
                            clear()
                            print("You walk past enforcer " + person.name + " but your " \
                                + player.disguise.name + " is gone now.")
                            print()
                            input("Press enter to continue...")
                            player.disguise = None
                            player.goDirection(commandWords[1])
                            timePasses = True
                        # if no disguise
                        else:
                            print("You can not do that right now.")
                            commandSuccess = False
                    # if no enforcers
                    else:
                        # disguise protects against normal people
                        if player.disguise != None:
                            player.goDirection(commandWords[1])
                            timePasses = True
                        else:
                            print("You can't do that right now.")
                            commandSuccess = False
                # if no mad people
                else:
                    player.goDirection(commandWords[1])
                    timePasses = True
            else:
                player.goDirection(commandWords[1])
                timePasses = True

        elif commandWords[0].lower() == "pickup":  #can handle multi-word objects
            targetName = command[7:]
            target = player.location.getItemByName(targetName)
            madPerson = False
            if player.location.hasPersons():
                for person in player.location.persons:
                    if person in player.engagedWith:
                        madPerson = True
            if madPerson == False:
                if target != False and player.currInv < player.maxInv:
                    if type(target.loc) == Store:
                        if target.loc.acquired == False:
                            print("You have to buy this item.")
                            commandSuccess = False
                        # if store is acquired, you can pick up
                        else:
                            player.pickup(target)
                            player.currInv += 1
                    else:
                        player.pickup(target)
                        player.currInv += 1
                elif player.currInv >= player.maxInv:
                    print("Backpack full.")
                    commandSuccess = False
                else:
                    print("No such item.")
                    commandSuccess = False
            else:
                print("You can't do that right now.")
                commandSuccess = False
        elif commandWords[0].lower() == "drop":  #can handle multi-word objects
            targetName = command[5:]
            target = player.getItemByName(targetName)
            madPerson = False
            if player.location.hasPersons():
                for person in player.location.persons:
                    if person in player.engagedWith:
                        madPerson = True
            if type(player.location) == Room:
                if madPerson == False:
                    if target != False:
                        player.drop(target)
                    else:
                        print("No such item in inventory.")
                        commandSuccess = False
                else:
                    print("You can't do that right now.")
                    commandSuccess = False
            else:
                print("You can't drop items in a store.")
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
            madPerson = False
            if player.location.hasPersons():
                for person in player.location.persons:
                    if person in player.engagedWith:
                        madPerson = True
            if madPerson == False:
                if target != False:
                    if type(target.loc) == Room:
                        print("You don't need to buy this item.")
                        commandSuccess = False
                    else:
                        if player.currInv < player.maxInv:
                            if target.loc.acquired == True:
                                print("You don't need to buy this item.")
                                commandSuccess = False
                            else:
                                player.buy(target)
                                player.currInv += 1
                        elif player.currInv >= player.maxInv:
                            print("Backpack full.")
                            commandSuccess = False
                else:
                    print("No such item.")
                    commandSuccess = False
            else:
                print("You can't do that right now.")
                commandSuccess = False
        elif commandWords[0].lower() == "acquire":
            if type(player.location) == Store:
                player.acquire()
            else:
                print("This is not a store.")
                commandSuccess = False
        elif commandWords[0].lower() == "sell":
            targetName = command[5:]
            target = player.getItemByName(targetName)
            madPerson = False
            if player.location.hasPersons():
                for person in player.location.persons:
                    if person in player.engagedWith:
                        madPerson = True
            if madPerson == False:
                if target != False:
                    if type(target.loc) == Room:
                        print("This room is not a store.")
                        commandSuccess = False
                    else:
                        if player.location.acquired == False:
                            player.sell(target)
                            player.currInv -= 1
                        else:
                            print("You can't sell items to your own store.")
                            commandSuccess = False
                else:
                    print("No such item in inventory.")
                    commandSuccess = False
            else:
                print("You can't do that right now.")
                commandSuccess = False
        elif commandWords[0].lower() == "inspect":
            targetName = command[8:]
            target = player.location.getItemByName(targetName)
            if target != False:
                player.inspect(target)
            else:
                target = player.getItemByName(targetName)
                if target != False:
                    player.inspect(target)
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
            clear()
            print("Thanks for playing!")
            print()
            player.losingScreen()
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
            if player.location.hasPersons():
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
                # if there are persons in room that are mad at you
                if important != []:
                    if player.disguise != None:
                        print("You have a disguise on, you don't need to run.")
                        commandSuccess = False
                    # if no disguise, try running
                    else:
                        if player.speed > p.speed:
                            clear()
                            print("You have successfully run away!")
                            print()
                            input("Press enter to continue...")
                            player.goDirection(commandWords[1]) 
                            timePasses = True
                        else: 
                            clear()
                            print("You can not run away...")
                            print()
                            input("Press enter to continue...")
                            commandSuccess = False
                else:
                    player.goDirection(commandWords[1])
                    timePasses = True
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