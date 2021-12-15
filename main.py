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
            elif type(m) == Enforcer:
                s += " (Enforcer)"
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
    print("me -- shows current stats and equipment")
    print("(i)nventory -- opens your inventory")
    print("pickup <item> -- picks up an item in your room")
    print("drop <item> -- drop an item from your inventory")
    print("equip <item> -- equip an item from your inventory")
    print("unequip <item> -- unequip an equipped item")
    print("inspect <item> -- displays an item's description, its given attribute compared to your equipment, and its sell price.")
    print("run <direction> -- attempts to run away from the fastest engaged person in your room")
    print("buy <item> -- buy an item from a store")
    print("acquire -- acquire the store in your location")
    print("sell <item> -- sell an item from your inventory to the store")
    print("wait -- wait a turn in same location")
    print("eat <item> -- eat an \"eatable\" item to gain health")
    print("pickpocket <person> -- chance to successfully steal money/ an item from a person")
    print("attack <person> -- attack a person")
    print("exit -- to exit the game early :(")
    print()
    input("Press enter to continue...")

clear()
print("Welcome to The Ginseng Projects!")
print()
print("The Ginseng Projects is a small neighborhood where you are a bandit and your goal" + "\n" \
    "is to either acquire all of the stores in the neighborhood to become the neighborhood's " + "\n" \
    "leader or to kill all of its inhabitants. Regardless of the path you choose, you will" + "\n" \
    "have to pickpocket those you come across and possibly attack/ kill them for their items" + "\n" \
    "and money. However, both of these actions can cause people to either fight back if" + "\n" \
    "they're having a rough day or call an enforcer to the neighborhood if you scare them." + "\n" \
    "With the items and money you find in rooms or pickpocket from people, you can buy items" + "\n" \
    "(or pickpocket them) from stores or sell your items to make money. Good luck!")
print()
input("Press enter to continue...")
clear()
print("1. Balance (Healthy balance of all traits)")
print("2. Speed (Prioritize speed and cunning)")
print("3. Brawn (Prioritize health and damage)")
print()
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
    for room in allRooms:
        if room.hasPersons():
            winCondition = False
    if player.acquisitions == 4 or winCondition == True:
        player.win()
        break
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
            if player.testGoDirection == False:
                print("Enter a valid direction.")
                commandSuccess = False
            else:
                if player.location.hasPersons():
                    # find mad persons in room
                    important = []
                    for i in player.location.persons:
                        if i in player.engagedWith:
                            important.append(i)
                    # check if enforcer is in room
                    if important != []:
                        hasEnforcer = False
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
                    else:
                        player.pickup(target)
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
                    if type(player.location) == Store:
                        if player.location.acquired == False:
                            player.sell(target)
                        else:
                            print("You can't sell items to your own store.")
                            commandSuccess = False
                    else:
                        print("This room is not a store.")
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
        elif commandWords[0].lower() == "inventory" or commandWords[0].lower() == "i" or \
            commandWords[0].lower == "inv":
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
            go = player.testGoDirection(commandWords[1])
            if go == False:
                print("Enter a valid direction")
                commandSuccess = False
            else:
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
                                # high percent chance to run based on how much faster you are
                                if random.random() > p.speed/player.speed:
                                    player.runSuccess(p)
                                    # don't need to check if valid cuz already did at beginning of function
                                    player.goDirection(commandWords[1])
                                    timePasses = True
                                else:
                                    player.runFail(p)
                            else: 
                                # the greater the difference in your speed, the less chance
                                if random.random() > player.speed/p.speed:
                                    player.runFail(p)
                                else:
                                    player.runSuccess(p)
                                    player.goDirection(commandWords[1])
                                    timePasses = True
                    else:
                        player.goDirection(commandWords[1])
                        timePasses = True
                # same as "go (direction)"
                else:
                    player.goDirection(commandWords[1])
                    timePasses = True
        elif commandWords[0].lower() == "wait":
            if player.location.hasPersons():
                canWait = True
                for person in player.location.persons:
                    if person in player.engagedWith:
                        print("You can't wait right now.")
                        commandSuccess = False
                        canWait = False
                if canWait == True:
                    timePasses = True
            else:
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