from room import *
from item import *
from person import *
from player import Player
import random

def charChoice(choice):
    # Player (health, regen, damage, speed, cunning, evasion):
    player = None
    player1 = Player(100, 5, 15, 50, 10, 50) # balance
    player2 = Player(75, 5, 10, 60, 15, 60) # focus more on speed and cunning
    player3 = Player(150, 10, 25, 25, 5, 40) # brute
    if choice == "1":
        player = player1
    elif choice == "2":
        player = player2
    elif choice == "3":
        player = player3
    return player

a = Room("Central Fountain")
b = Room("room b")
c = Room("room c")
d = Room("room d")
e = Room("room e")
f = Store("store f", 200)
g = Room("room g")
h = Room("room h")
i = Store("store i", 200)
j = Store("store j", 200)
k = Room("room k")
l = Store("store l", 200)
m = Room("room m")
allRooms = [a,b,c,d,e,f,g,h,i,j,k,l,m]

def createWorld(player):
    # add multiple rooms for variability 

    Room.connectRooms(a, "right", b, "left")
    Room.connectRooms(c, "right", d, "left")
    Room.connectRooms(a, "up", c, "down")
    Room.connectRooms(b, "up", d, "down")
    Room.connectRooms(d, "up", e, "down")
    Room.connectRooms(e, "right", f, "left")
    Room.connectRooms(f, "down", g, "up")
    Room.connectRooms(g, "down", h, "up")
    Room.connectRooms(h, "right", i, "left")
    Room.connectRooms(h, "left", b, "right")
    Room.connectRooms(a, "down", j, "up")
    Room.connectRooms(a, "left", m, "right")
    Room.connectRooms(m, "left", l, "right")
    Room.connectRooms(l, "down", k, "up")
    Room.connectRooms(k, "right", j, "left")

    i0 = Item("Rock", "This is just a rock.", 0)
    i0.putInRoom(a)
    player.location = a

    w0 = Weapon("Wrench", "A somewhat rusty wrench.", 5, 2)
    w1 = Weapon("Toothpick", "A used toothpick.", 1, 1)
    i1 = Item("iPhone 5s", "Pretty old, but probably still worth quite a bit.", 35)
    i2 = Item("Nokia", "A Nokia", 15)
    i3 = Item("iPhone 6", "Cracked screen", 60)
    c0 = Clothes("Apron", "Has some mysterious stains on it.", 5, 5)
    c1 = Clothes("Handkerchief", "Protect yourself when eating", 3, 3)
    c2 = Clothes("Jersey", "A basketball jersey", 15, 7)
    c3 = Clothes("Shirt", "A slightly smelly t-shirt", 10, 7)
    c4 = Clothes("Shirt", "A striped long-sleeve.", 20, 10)
    s0 = Shoes("Jordans", "Uncreased.", 60, 3)
    s1 = Shoes("Running Shoes", "A pair of new running shoes.", 50, 10)
    s2 = Shoes("Jordans", "Creased.", 30, 2)
    s3 = Shoes("Running Shoes", "Probably worn for at least 3 marathons.", 25, 6)
    f0 = Food("Pizza", "Slice of pizza.", 2, 10)
    f1 = Food("Kombucha", "Might be a little old.", 2, 10)

    # For testing
    w0.putInRoom(a)
    i1.putInRoom(a)
    c0.putInRoom(a)
    s0.putInRoom(a)
    f0.putInRoom(a)

    person_items = [w0,w1,i1,i2,i3,c0,c1,c2,c3,c4,s0,s1,s2,s3,f0,f1]
    enforcer_items = []
    merchant_items = [w0,w1,i1,i2,i3,c0,c1,c2,c3,c4,s0,s1,s2,s3,f0,f1]

    Person("Bob", random.choice(allRooms), random.sample(person_items, random.randint(1,3)))
    Person("Jeffrey", random.choice(allRooms), random.sample(person_items, random.randint(1,3)))
    Person("Jacobson", random.choice(allRooms), random.sample(person_items, random.randint(1,3)))
    Person("Mozart", random.choice(allRooms), random.sample(person_items, random.randint(1,3)))
    Person("Bobson", random.choice(allRooms), random.sample(person_items, random.randint(1,3)))
    Person("Tiffany", random.choice(allRooms), random.sample(person_items, random.randint(1,3)))
    Person("Jennifer", random.choice(allRooms), random.sample(person_items, random.randint(1,3)))
    Person("Shelly", random.choice(allRooms), random.sample(person_items, random.randint(1,3)))
    Person("Bobby", random.choice(allRooms), random.sample(person_items, random.randint(1,3)))
    Person("Kelly", random.choice(allRooms), random.sample(person_items, random.randint(1,3)))

    storeRooms = [f,i,j,l]
    r = random.choice(storeRooms)
    Merchant("Clark", r, random.sample(merchant_items, random.randint(3,6)))
    storeRooms.remove(r)
    r = random.choice(storeRooms)
    Merchant("Clerk", r, random.sample(merchant_items, random.randint(3,6)))
    storeRooms.remove(r)
    r = random.choice(storeRooms)
    Merchant("Cassy", r, random.sample(merchant_items, random.randint(3,6)))
    storeRooms.remove(r)
    r = random.choice(storeRooms)
    Merchant("Cuphead", r, random.sample(merchant_items, random.randint(3,6)))
    storeRooms.remove(r)

    # used to call a random enforcer to room when caught pickpocketing
    allEnforcers = []
    Enforcer("Cait", b, [])