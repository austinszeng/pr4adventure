from room import *
from item import *
from person import *
from player import Player
from misc import *
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

def createWorld(player):
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

    # For testing
    w0.putInRoom(a)
    i1.putInRoom(a)
    c0.putInRoom(a)
    s0.putInRoom(a)
    f0.putInRoom(a)

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