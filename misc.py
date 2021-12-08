from room import *
from item import *
from person import *
import random

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

person_items = [w0,w1,i1,i2,i3,c0,c1,c2,c3,c4,s0,s1,s2,s3,f0,f1]
enforcer_items = [w0,w1,i1,i2,i3,c0,c1,c2,c3,c4,s0,s1,s2,s3,f0,f1]
merchant_items = [w0,w1,i1,i2,i3,c0,c1,c2,c3,c4,s0,s1,s2,s3,f0,f1]

# used to call a random enforcer to room when caught pickpocketing
enforcer1 = Enforcer("Cait", random.choice(allRooms), random.sample(enforcer_items, random.randint(1,3)))
allEnforcers = [enforcer1]