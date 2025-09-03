# Dungeon-Crawler
A text-based dungeon crawler game with procedural generation.
## Setup
Download and place all python files in the same folder
## Play
Run the main file. It will prompt you if you want it to leave history or wipe screen after every action. It will then prompt you for how long you want it to run for before it stops generation. 4 to 5 is reccomended for a deacent sized dungeon.

To move input w, a, s, or d, and then press enter. All commands are case sensitive.

Objects on the map:
```
☺︎ = Player
# = Wall
c = Chest
O = Orc
G = Goblin
B = Bandit
E = Elf
K = Knight
W = Wizard (Not functional yet)
⛇ = Snowman Spellcaster (Not functional yet)
X = Chance: Good Chest or Powerful Enemy
M = Merchant
```
### Chests
To swap items:
```
inventorySlotNumber;chestSlotNumber (use 11-14 for armour slots)
```
### Inventory
To swap items:
```
slot1;slot2 (use 11-14 for armour slots)
```
### Battle
You will see your health and energy, as well as your oponents health and energy
You cannot do an attack if you do not have enough energy, and defending increases energy
Attack/Defend Commands: Type a wepon attack and location (head, torso, legs, boots), such as:
```
Sword;Stab;Legs
```
The weapons and atacks in the table are case sensitive for commands
### Bartering
To make an offer:
```
merchantItemName;merchantItemAmount;itemYouAreGiving;amountYouAreGiving
```
Slot numbers go across, then down for the merchant
If the merchant values the item the same or more them the offer, the trade will be given. Otherwise, the merchant will give you an example of what he might want
