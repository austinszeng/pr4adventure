# CSCI121 Adventure Final Project: The Ginseng Projects 
## The Ginseng Projects is a text-based adventure game where you are a bandit roaming the neighborhood and your goal is to either acquire all of the stores in the neighborhood to become the Ginseng Projects' leader or to kill all of its inhabitants. Regardless of the path you choose, you will have to pickpocket those that you come across and possibly attack/ kill them for their items and money. However, both of these actions can cause people to either fight back if they're having a rough day or call an enforcer to the neighborhood if you scare them. With the items and money you took from people or found lying on the ground, you can buy items from stores or sell your items for more money.

# Improvements (Total: 40 points):
## "me" command (2 points)
- Added showStats method in Player to show current status and equipment
## "inspect" command (2 points)
- Displays item description using helperStats function in Player, which also shows the stats increased/ decreased if an equippable item is equipped instead of what you currently have in that slot (if anything), the healing effects of food items, and the sell price of all items
## item stacking (2 points)
- Modified showInventory method in Player to use the helperStats function to display the same information as the "inspect" command next to the given inventory item. Prints duplicate items with "xNum" rather than printing the same item more than once.
## limited inventory (2 points)
- Added currInv and maxInv variables to Player that is kept track of by the various methods that add to/ take from the player's inventory 
## "drop" command (2 points)
- Added getItemByName method for the player's inventory (similar to the one in Room) and drop method that removes an item from one's inventory and into the player's current room in Player.
## "wait" command (2 points)
- Makes time pass while not having to move to a different room unless someone is engaged with you in that room.
## regeneration (2 points)
- Adds instance variables maxHealth and regen to Player to regenerate when time passes.
## more monsters (3 points)
- There are normal people, merchants, and enforcers. Both Merchant and Enforcer classes inherit from Person and have altered levels of health, attentiveness, speed, anger, etc. The higher the anger, the more likely the person is to fight back rather than call an enforcer. If their speed is higher than the player's, then the player is more unlikely to be able to run away. Merchants can't move away from their store.
## player attributes (3 points)
- Added damage, speed, and cunning attributes. A higher cunning value increases the success rate of pickpocketing and a higher speed value increases the success rate of running away and allows the player to attack first and be able to have a chance to dodge an opponent's attacks when fighting.
## weapons and armor (4 points)
- Added Weapon, Clothes, Shoes, and Disguise classes that all inherit from item. Respectively, they increase player damage, player health, and player speed when equipped. When an item of the Disguise class is equipped, it allows the player to be able to move freely away from all types of people regardless of if they are engaged, but the Disguise item is used up if used to move away from an Enforcer.
## bigger world (2 points)
- Now contains a world of 13 rooms, 4 of those being stores.
## currency (4 points)
- Added a Store class that inherits from Room that contains buyable items. A player can sell items to stores they either find from rooms or pickpocket from people to make money. A store can also be acquired, which gives ownership of the store to the player and makes all of the store's items pickupable.
## loot (3 points)
- Pickpocketing a person gives loot/ money based on the items the person is carrying (randomly chosen from a list of items in misc.py) and the amount of money the person is carrying. Additionally, killing a person also gives you their loot.
## healing item (2 points)
- Added a Food class that inherits from Item and can be eaten using the "eat" command in Player that restores the health given by that item. 
## introducing monsters during play (2 points)
- An enforcer is added to the map in a random location when a person you pickpocket notices you and gets scared. The enforcer(s) are a lot stronger than normal people and are constantly engaged and looking for the player.
## victory condition (3 points)
- To win, the player can acquire all 4 stores on the map or kill all of the people on the map (including any added enforcers)

# Notes :
- Pickpocketing and attacking both have risks of adding an enforcer to the map during the first encounter if the person notices and gets scared. However, the same person cannot call an enforcer on the map twice. Subsequent pickpockets where the person notices or subsequent attacks cause the person to either stay scared or they have a chance to get mad and be engaged instead. Once engaged, they stay engaged.

# Ideas:
- after all of this, need to balance the game (e.g. running away is way too easy rn)
- maybe make stealing money more complicated and don't make it all go away with one swipe? add money that merchant makes from store to merchant's money?