# Blah Blah
## Blah Blah is a game where you are a bandit roaming the streets and pickpocket items/ money from people or stores and sell these stolen goods to stores to make money to buy items and acquire stores. To win the game, acquire all the stores. However, each time you pickpocket, there comes a risk of being seen or caught. You may have to deal with the police and/ or being attacked. 

# Improvements/ Changes (Current: 40 points):
## "me" command (2 points)
- Added showStats method in Player to show current status
## "inspect" command (2 points)
- Displays item description using describe method in Item
## limited inventory (2 points)
- Added an inventory size variable to Player that is kept track of by the pickup and drop methods. 
## "drop" command (2 points)
- Added getItemByName method for the player's inventory (similar to the one in Room) and drop method that removes an item from one's inventory and into the room in Player.
## "wait" command (2 points)
- Makes time pass while not having to move to a different room.
## regeneration (2 points)
- Adds instance variables maxHealth and regen to Player to regenerate when time passes.
## more monsters (3 points)
- Normal people and police and merchants with different levels of attentiveness, speed, and anger. The higher the anger, the more likely the person is to fight back rather than call an enforcer. If speed is higher than yours, then you're unable to run away. If an enforcer's cunning and speed and damage are higher than yours the more likely you are to get arrested and lose if you catch their attention.
- pickpocketPerson
- change attackPerson
## player attributes (3 points)
- Added speed and cunning which affects interactions with people
- Every successful pickpocket increases cunning
## weapons (2 points)
- Added a Weapon class that inherits from Item which will add a damage attribute to the item and can be used to fight/ attack people.
## armor (2 points)
- Clothes increase health
- Shoes increase evasion
- Hats are a disguise where people who are mad at you can't see you if you have it on
    - if you have a disguise on when they fight you, it's ineffective and goes away
## item stacking (2 points)
- Modified showInventory method in Player to print duplicate items first with "(xNum)"
## bigger world (2 points)
## "run" command 
## currency (4 points)
- Store class to buy/ sell items
## loot (3 points)
- pickpocketing gives loot and also when killing the person lol
## healing item (2 points)
- food
## introducing monsters during play (2 points)
- enforcer
## victory condition (3 points)
- acquire all 4 stores (this will be the final implementation)

## Bugs:
- Enforcers are all over the map now prespawned lol
    - try just redoing inheritance? this happened after i readded inheritance cuz I forgot about it
- test "go" with disguise mechanics with enforcers
- Make another win condition be if you kill everyone on the map and acquisition all (haven't tested yet)
- test - make it so you can't wait when there's an engaged person in the room
- error when pickpocketing:
    -  File "C:\Users\etcje\Desktop\CSCI121\pr4adventure\main.py", line 327, in <module>
            player.pickpocketPerson(target)
        File "C:\Users\etcje\Desktop\CSCI121\pr4adventure\player.py", line 287, in pickpocketPerson
            item = random.choice(self.location.items)
        File "C:\Users\etcje\AppData\Local\Programs\Python\Python39\lib\random.py", line 347, in choice
            return seq[self._randbelow(len(seq))]
        IndexError: list index out of range
- final stats message press enter twice when die

## Ideas:
- make it so you can't pickpocket when someone is engaged in the room?
- limit amount of items in room
- running away is way too easy rn
- after all of this, need to balance the game
- function for locating people in room would've been useful, maybe implement that if enough time just for organization sake