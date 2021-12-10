import random

class Room:
    def __init__(self, description):
        self.desc = description
        self.persons = []
        self.exits = []
        self.items = []
    def addExit(self, exitName, destination):
        self.exits.append([exitName, destination])
    def getDestination(self, direction):
        for e in self.exits:
            if e[0] == direction:
                return e[1]
    def connectRooms(room1, dir1, room2, dir2):
        #creates "dir1" exit from room1 to room2 and vice versa
        room1.addExit(dir1, room2)
        room2.addExit(dir2, room1)
    def exitNames(self):
        return [x[0] for x in self.exits]
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def addPerson(self, person):
        self.persons.append(person)
    def removePerson(self, person):
        self.persons.remove(person)
    def hasItems(self):
        return self.items != []
    def getItemByName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False
    def hasPersons(self):
        return self.persons != []
    def getPersonByName(self, name):
        for i in self.persons:
            if i.name.lower() == name.lower():
                return i
        return False
    def randomNeighbor(self):
        return random.choice(self.exits)[1]

class Store(Room):
    def __init__(self, description, acquisition):
        Room.__init__(self, description)
        r = round(random.uniform(acquisition - acquisition/4, acquisition + acquisition/4))
        self.acquisition = r
        self.acquired = False
    def displayItems(self):
        # acquired store displays normally
        if self.acquired == True:
            print("This room contains the following items:")
            numOccurences = {}
            for item in self.items:
                if item in numOccurences:
                    numOccurences[item] += 1
                else:
                    numOccurences[item] = 1
            for item in numOccurences:
                if numOccurences[item] > 1:
                    print(item.name + " (x" + str(numOccurences[item]) + ")")
                else:
                    print(item.name)
        else:
            print("You can buy the following items:")
            numOccurences = {}
            for item in self.items:
                if item in numOccurences:
                    numOccurences[item] += 1
                else:
                    numOccurences[item] = 1
            for item in numOccurences:
                if numOccurences[item] > 1:
                    print(item.name + " ($" + str(item.price) + ")" + " x" + str(numOccurences[item]))
                else:
                    print(item.name + " ($" + str(item.price) + ")")
        print()
