#import modules
import random
#create player class
class Player():
    def __init__(self):
        self.health = random.randint(48, 80)
        self.strength = random.randint(6, 10)
        self.max_health = self.health
        self.inventory = {
                        'slot_1': ['Sword', 1],
                        'slot_2': ['Bread', 1],
                        'slot_3': ['Coin', 3],
                        'slot_4': ['', 1],
                        'slot_5': ['', 1],
                        'slot_6': ['', 1],
                        'slot_7': ['', 1],
                        'slot_8': ['', 1],
                        'slot_9': ['', 1],
                        'slot_10': ['', 1],
                        }
        self.armour = {
                        'helmet': ['', 1],
                        'chestplate': ['', 1],
                        'leggings': ['', 1],
                        'boots': ['', 1],
                        }
        self.score = 0
        self.energy = random.randint(10, 20)
    #function for taking damage
    def damage(self, damage_amount):
        self.health -= damage_amount
    #function to run every round
    def idle(self):
        if self.health != self.max_health:
            heal = random.choice([True, False])
            if heal == True:
                self.health += 1
    def prep_battle(self):
        #set agility based on armour values
        self.agility =  5
        for armour in self.armour.values():
            if 'Plate' in armour[0]:
                    self.agility -= 2
            elif 'Chainmail' in armour[0]:
                    self.agility -= 1
            elif 'Scalemail' in armour[0]:
                    self.agility -= 1 
            elif 'Studded Leather' in armour[0]: 
                    self.agility += 0.5
            else:
                    self.agility += 2
        self.weapons = ['Hand']
        #add all weapons to a list
        for item in self.inventory.values():
            if item[0] in ['Sword', 'Bow', 'Shield', 'Dagger', 'Club', 'Lance', 'Spear']:
                self.weapons.append(item[0])
            
                    