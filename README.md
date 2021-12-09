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
## separate file for createWorld function (world.py)
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
- make it so you can't pickup, drop, buy, sell when there's an engaged person in the room
- merchant's still move around?
- is player.engaged even used?
- change so "run" takes into account disguise and tells player to not run if disguise on
- test "go" with disguise mechanics
- run is probably still buggy if the direction is spelled wrong
- make it so you can't pickup in a store room unless they're items dropped by players?
- stealing an item from a merchant doesn't remove it from shop

## Ideas:
- redo how attacking works since player can't dodge rn and also maybe add for the possibility of the enemy to dodge too
- still need to add disguise mechanics sigh
- having a disguise on makes it easier to run away
- disguise is useless if person catches you and is discarded; however, if put on a disguise, you can run away but your disguise is discarded. If no disguise, then need to wait like 5 turns for them to not be engaged anymore
- alternative commands (1 point): maybe 3 points if make it abbreviate in a consistent clean way?
- if person is still engaged and you run into them again, youre back engagedWith them unless you have on a disguise
- if in the room with someone who's engaged then you're also engaged
- implement something so it shows the amount of damage you increase if you equip a weapon based on your current damage if no wepDamage, else do it based on wepDamage
- display stats increased from inventory 
- maybe make the mechanic of disguise just avoiding them for a few turns then they'll lose you
- once you acquire a shop, eveyrthing in it is yours and you can't buy/ sell from it anymore?
- Show item attributes while in inventory 
- randomly put stores in store locations
- make an exit message like keith
- dropping an item in a store gives it back to the store and you have to buy it again