from room import *
from item import *
from person import *
from player import Player
from misc import *
import random

def charChoice(choice):
    # Player (health, regen, damage, speed, cunning):
    player = None
    player1 = Player(125, 5, 20, 50, 10) # balance
    player2 = Player(100, 5, 15, 60, 15) # focus more on speed and cunning
    player3 = Player(150, 10, 25, 40, 5) # brute
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

    player.location = a 

    r = random.randint(1,4)
    if r == 1 or r == 4:
        a0.putInRoom(a)
    if r == 2:
        b0.putInRoom(b)
    if r == 1:
        c0.putInRoom(c)
    if r == 2:
        c1.putInRoom(c)
    if r == 3:
        c2.putInRoom(c)
    if r == 3:
        h0.putInRoom(h)
    if r == 2 or r == 4:
        m0.putInRoom(m)

    r = random.randint(10,15)
    ind = 0
    while ind < r:
        random.shuffle(room_items)
        room_items[ind].putInRoom(random.choice(nonStoreRooms))
        ind += 1

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
    Person("Karl", random.choice(allRooms), random.sample(person_items, random.randint(1,3)))
    Person("John", random.choice(allRooms), random.sample(person_items, random.randint(1,3)))
    Person("Johnson", random.choice(allRooms), random.sample(person_items, random.randint(1,3)))
    Person("Johnny", random.choice(allRooms), random.sample(person_items, random.randint(1,3)))
    Person("Barbara", random.choice(allRooms), random.sample(person_items, random.randint(1,3)))
    Person("Barbie", random.choice(allRooms), random.sample(person_items, random.randint(1,3)))

    storeRooms = [f,i,j,l]
    r = random.choice(storeRooms)
    Merchant("Clark", r, random.sample(merchant_items, random.randint(4,6)))
    storeRooms.remove(r)
    r = random.choice(storeRooms)
    Merchant("Clerk", r, random.sample(merchant_items, random.randint(4,6)))
    storeRooms.remove(r)
    r = random.choice(storeRooms)
    Merchant("Cassy", r, random.sample(merchant_items, random.randint(4,6)))
    storeRooms.remove(r)
    r = random.choice(storeRooms)
    Merchant("Cuphead", r, random.sample(merchant_items, random.randint(4,6)))
    storeRooms.remove(r)