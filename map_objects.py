#import modules
import random
#chest class
class Chest():
    def __init__(self, x, y, item_data, rarity):
        self.items = {
                    'slot_1': [''],
                    'slot_2': [''],
                    'slot_3': [''],
                    'slot_4': [''],
                    'slot_5': [''],
                    }
        #chest data
        if rarity == 'rare':
            num_items = random.randint(3, 5)
            for num in range(num_items):
                #randomly choose a rarity
                item_rarity = random.choices(['common', 'medium', 'rare', 'super_rare'], k=1, weights = (5, 15, 30, 50))
                item = random.choice(item_data[item_rarity[0]])
                self.items[f'slot_{num}'] = [item, 1]
            self.location = [x, y]
        elif rarity == 'common':
            num_items = random.randint(1, 5)
            for num in range(num_items):
                #randomly choose a rarity
                item_rarity = random.choices(['common', 'medium', 'rare', 'super_rare'], k=1, weights = (50, 30, 15, 5))
                item = random.choice(item_data[item_rarity[0]])
                self.items[f'slot_{num}'] = [item, 1]
            self.location = [x, y]
    def display(self):
        print(self.items)
    def change(self, slot_num, item):
        self.items[slot_num] = item
class Enemy():
    def __init__(self, x, y, enemy_type, item_data):
        self.location = [x, y]
        self.type = enemy_type
        match self.type:
            case 'O':
                #Orc
                self.strength = random.randint(8,12)
                self.weapon = random.choices([['Sword', 1], ['Club', 1]], k=random.randint(1,3))
                if 'None' in self.weapon:
                    if len(self.weapon) == 2:
                        if 'None' == self.weapon[0] and self.weapon[1]:
                            self.shield = False
                        else:
                            self.shield = True
                    else:
                        self.shield = False
                else:
                    self.shield = True
                self.other_items = random.choices([['Rotton Meat', random.randint(5, 8)], ['Coin', random.randint(1,3)], ['Gem', 1], ['', 1]], k=random.randint(0,5))
                armour_type = random.choices(['Plate', 'Chainmail', 'Studded_leather'], weights=(20, 25, 20), k=1)
                self.armour = {
                            'Helmet': [[armour_type[0] + ' helmet', 1]],
                            'Chestplate': [[armour_type[0] + ' chestplate', 1]],
                            'leggings': [[armour_type[0] + ' leggings', 1]],
                            'Boots': [[armour_type[0] + ' boots', 1]],
                            }
                self.health = random.randint(60, 80)
                self.action_weight = random.randint(85, 100)
                self.values = {
                            '': 0,
                            'Coin': 13,
                            'Sword': 15,
                            'Club': 15,
                            'Lance': 12,
                            }
                self.surrender_condition = [0, 0]
            case 'G':
                #Goblin
                self.strength = random.randint(6,9)
                self.weapon = random.choices([['Sword', 1], ['Club', 1], ['Dagger', 1],['Bow', 1]], k=1)
                if 'None' in self.weapon:
                    self.shield = False
                else:
                    self.shield = random.choice([True, False])
                self.other_items = random.choices([['Rotten Meat', random.randint(2, 5)], ['Bread', random.randint(2, 3)], ['Coin', random.randint(3,12)], ['Gem', 1], ['', 1], ['', 1]], k=random.randint(0,5))
                helmet_type = random.choices(['Chainmail', 'Studded_leather', ''], weights=(20, 30, 25), k=1)  
                chestplate_type = random.choices(['Chainmail', 'Studded_leather', ''], weights=(20, 30, 25), k=1)  
                legging_type = random.choices(['Chainmail', 'Studded_leather', ''], weights=(20, 30, 25), k=1)  
                boots_type = random.choices(['Chainmail', 'Studded_leather', ''], weights=(20, 30, 25), k=1)  
                self.armour = {
                            'Helmet': [[helmet_type[0] + ' helmet', 1]],
                            'Chestplate': [[chestplate_type[0] + ' chestplate', 1]],
                            'leggings': [[legging_type[0] + ' leggings', 1]],
                            'Boots': [[boots_type[0] + ' boots', 1]],
                            }
                self.health = random.randint(30, 40)
                self.action_weight = random.randint(48, 97)
                self.values = {
                            '': 0,
                            'Coin': 18,
                            'Sword': 12,
                            'Club': 13,
                            'Spear': 12,
                            }
                self.surrender_condition = [15, 20]
            case 'B':
                #Bandit
                self.strength = random.randint(6,8)
                self.weapon = random.choices([['Sword', 1], ['Shield', 1], ['Club', 1], ['Spear', 1], ['Bow', 1]], k=random.randint(1,3))
                if 'Bow' in self.weapon:
                    self.shield = False
                else:
                    self.shield = random.choice([True, False])
                if self.shield:
                    self.weapon.append(['Shield', 1])
                self.other_items = random.choices([['Bread', random.randint(2,3)], ['Coin', random.randint(1,10)], ['Gem', 1], ['', 1], ['', 1]], k=random.randint(0,5))
                helmet_type = random.choices(['Plate', 'Chainmail', 'Studded_leather', ''], weights=(20, 30, 25, 18), k=1)  
                chestplate_type = random.choices(['Plate', 'Chainmail', 'Studded_leather', ''], weights=(20, 30, 25, 20), k=1)  
                legging_type = random.choices(['Plate', 'Chainmail', 'Studded_leather', ''], weights=(20, 30, 28, 25), k=1)  
                boots_type = random.choices(['Plate', 'Chainmail', 'Studded_leather', ''], weights=(20, 30, 25, 18), k=1)  
                self.armour = {
                            'Helmet': [[helmet_type[0] + ' helmet', 1]],
                            'Chestplate': [[chestplate_type[0] + ' chestplate', 1]],
                            'leggings': [[legging_type[0] + ' leggings', 1]],
                            'Boots': [[boots_type[0] + ' boots', 1]],
                            }
                self.health = random.randint(35, 45)
                self.action_weight = random.randint(35, 99)
                self.values = {
                            '': 0,
                            'Coin': 16,
                            'Bread': 12,
                            'Plate Helmet': 15,
                            'Plate Chestplate': 15,
                            'Plate Leggings': 15,
                            'Plate Boots': 15,
                            }
                self.surrender_condition = [12, 25]
            case 'E':
                #Elf
                self.strength = random.randint(7,11)
                self.weapon = random.choices([['Bow', 1], ['Sword', 1]], k=random.randint(1,2))
                if 'Bow' in self.weapon:
                    self.shield = False
                else:
                    self.shield = True
                self.other_items = random.choices([['Bread', random.randint(2,3)], ['Coin', random.randint(1,3)], ['Gem', 1], ['', 1], ['Dagger', 1]], k=random.randint(0,5))
                armour_type = random.choices(['Plate', 'Chainmail', 'Scalemail', 'Studded_leather', ''], weights=(25, 30, 30, 20, 10), k=1)  
                self.armour = {
                            'Helmet': [[armour_type[0] + ' helmet', 1]],
                            'Chestplate': [[armour_type[0] + ' chestplate', 1]],
                            'leggings': [[armour_type[0] + ' leggings', 1]],
                            'Boots': [[armour_type[0] + ' boots', 1]],
                            }
                self.health = random.randint(50, 75)
                self.action_weight = random.randint(60, 100)
                if ['Sword', 1] in self. weapon:
                    self.weapon.append(['Shield', 1])
                self.values = {
                            '': 0,
                            'Coin': 14,
                            'Bow': 14,
                            }
                self.surrender_condition = [1, 5]
            case 'K':
                #Knight
                self.strength = random.randint(8,10)
                self.weapon = random.choices([['Sword', 1], ['Lance', 1], ['Spear', 1]], k=random.randint(1,2))
                self.shield = True
                self.other_items = random.choices([['Healing', 1], ['Coin', random.randint(1,7)], ['Gem', random.randint(1,2)], ['', 1]], k=random.randint(0,5))
                armour_type = random.choices(['Plate', 'Chainmail', 'Scalemail'], weights=(40, 35, 35), k=1)  
                self.armour = {
                            'Helmet': [[armour_type[0] + ' helmet', 1]],
                            'Chestplate': [[armour_type[0] + ' chestplate', 1]],
                            'leggings': [[armour_type[0] + ' leggings', 1]],
                            'Boots': [[armour_type[0] + ' boots', 1]],
                            }
                self.health = random.randint(60, 80)
                self.action_weight = random.randint(50, 100)
                self.weapon.append(['Shield', 1])
                self.values = {
                            '': 0,
                            'Coin': 13,
                            'Bread': 12,
                            'Gem': 15,
                            }
                self.surrender_condition = [5, 5]
        self.defences = ['Dodge']
        self.energy = random.randint(15, 20)
        if self.shield == True:
            self.defences.append('Block')
        self.agility = 6
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
        #set values for any not pre-set items
        for rarity in item_data:
            match rarity:
                case 'common':
                    for item in item_data[rarity]:
                        if item in self.values.values():
                            continue
                        self.values[item] = random.randint(1, 3)
                case 'medium':
                    for item in item_data[rarity]:
                        if item in self.values.values():
                            continue
                        self.values[item] = random.randint(3, 8)
                case 'rare':
                    for item in item_data[rarity]:
                        if item in self.values.values():
                            continue
                        self.values[item] = random.randint(9, 14) 
                case 'super_rare':
                    for item in item_data[rarity]:
                        if item in self.values.values():
                            continue
                        self.values[item] = random.randint(15, 20)
        #set max health
        self.max_health = self.health
    def battle(self, player, data):
        #get attack or defense uing randomly chosen weights for each one
        action_type = random.choices(['attack', 'defence'], k=1, weights=(self.action_weight, 100 - self.action_weight))[0]
        #can only defend with no energy
        if self.energy == 0:
            action_type = 'defence'
        #check surrender condition
        if self.health <= self.surrender_condition[0]:
            #weights in the condition are percentages
            action_type = random.choices(['surrender', action_type], k=1, weights= (self.surrender_condition[1], (100 - self.surrender_condition[1])))
        match action_type:
            case 'attack':
                attack, chance, chosen_type = self.create_attack(player, data)
                return attack, chance, chosen_type
            case 'defence':
                defence, chance, chosen_type = self.choose_defence(player, data)
                return defence, chance, chosen_type
            case 'surrender':
                return 'surrender', 100, 'surrender'
            case _:
                attack, chance, chosen_type = self.create_attack(player, data)
                return attack, chance, chosen_type
    def choose_defence(self, player, data):
        '''This function chooses the defence move'''
        possible_defences = []
        defence_weights = []
        #create every possible combonation of defences
        for weapon_list in self.weapon:
            weapon = weapon_list[0]
            for defence in data[weapon]['defences']:
                #get all player weapons and get average chance between them
                weapon_chance = []
                for item in player.inventory.values():
                    if item[0] in data:
                        for item_defence in data[weapon]['defences']:
                            weapon_chance.append(data[weapon]['defences'][item_defence]['effectivness'][item[0]])
                #get average of the chances 
                num_chances = len(weapon_chance)
                against_player_chance = sum(weapon_chance) / num_chances
                for location in ['head', 'torso', 'legs', 'boots']:
                    defence_command = weapon + ';' + defence + ';' + location 
                    #create chance of succsess by mashing all the numbers together
                    defence_chance = (against_player_chance * (data[weapon]['defences'][defence]['effectivness'][location] / 100)) * 100
                    #add item to list
                    possible_defences.append(defence_command)
                    defence_weights.append(defence_chance)
        #create defences for hand (dodge) as they are not weapons
        #get all player weapons and get average chance between them
        weapon = 'Hand'
        weapon_chance = []
        for item in player.inventory.values():
            if item[0] in data:
                for item_defence in data[weapon]['defences']:
                    weapon_chance.append(data[weapon]['defences'][item_defence]['effectivness'][item[0]])
        #get average of the chances 
        num_chances = len(weapon_chance)
        against_player_chance = sum(weapon_chance) / num_chances
        for location in ['head', 'torso', 'legs', 'boots']:
            defence_command = weapon + ';' + 'Dodge' + ';' + location 
            #create chance of succsess by mashing all the numbers together
            defence_chance = (against_player_chance * (data[weapon]['defences']['Dodge']['effectivness'][location] / 100)) * 100
            #add item to list
            possible_defences.append(defence_command)
            defence_weights.append(defence_chance)
        #randomly choose attack based on chances created before
        chosen_defence = random.choices(possible_defences, k=1, weights=defence_weights)[0] 
        #find what the chance of the chosen defence was
        chosen_chance = defence_weights[possible_defences.index(chosen_defence)]
        return chosen_defence, chosen_chance, 'defence'
    def create_attack(self, player, data):
        '''This function chooses the attack move'''
        possible_attacks = []
        attack_weights = []
        #create every possible combonation of attacks
        for weapon_list in self.weapon:
            weapon = weapon_list[0]
            for attack in data[weapon]['attacks']:
                for location in ['head', 'torso', 'legs', 'boots']:
                    #create attack command
                    attack_command = weapon + ';' + attack + ';' + location 
                    #get player armour
                    match location:
                        case 'head':
                            player_armour = player.armour['helmet'][0].split(' ')[0]
                        case 'torso':
                            player_armour = player.armour['chestplate'][0].split(' ')[0]
                        case 'legs':
                            player_armour = player.armour['leggings'][0].split(' ')[0]
                        case 'boots':
                            player_armour = player.armour['boots'][0].split(' ')[0]
                        case _:
                            player_armour = ''
                    #get energy cost; using 1.1 not 1 so that if it takes all energy it still has a very small chance of being chosen
                    if data[weapon]['attacks'][attack]['energy_cost'] > self.energy:
                        energy_multiplier = 0.0 
                    else:
                        energy_multiplier =  1.1 - (data[weapon]['attacks'][attack]['energy_cost'] / self.energy)
                    #create chance of succsess by mashing all the numbers together
                    attack_chance = abs(((data[weapon]['attacks'][attack]['effectivness'][player_armour] / 100) * (data[weapon]['attacks'][attack]['effectivness'][location] / 100) * energy_multiplier) * 100)
                    #add attack and chance to possible attacks
                    possible_attacks.append(attack_command)
                    attack_weights.append(attack_chance)
        #do a defence if there are no posible attacks
        if len(attack_weights) > 0 and sum(attack_weights) > 0:
            #randomly choose attack based on chances created before
            chosen_attack = random.choices(possible_attacks, k=1, weights=attack_weights)[0]
            #find what the chance of the chosen attack was
            chosen_chance = attack_weights[possible_attacks.index(chosen_attack)]
            #return attack
            return chosen_attack, chosen_chance, 'attack'
        else:
            defence, chance, chosen_type = self.choose_defence(player, data)
            return defence, chance, chosen_type
    def victory(self, player):
        #this runs if player surrenders
        items = []
        item_weights = []
        #add weights of items in player inventory and items to lists
        for item in player.inventory.values():
            items.append(item[0])
            item_weights.append(self.values[item[0]])
        #add weights of items in player armour and items to lists
        for item in player.armour.values():
            items.append(item[0])
            item_weights.append(self.values[item[0]])
        #choose what item to take based on the weights
        chosen_item = random.choices(items, k=1, weights=item_weights)[0]
        #add item to own inventory
        self.other_items.append(chosen_item)
        #remove 1 of item from player inventory
        found_item = False
        for item_key in player.inventory:
            item = player.inventory[item_key][0]
            #check if the item is the selected item
            if item == chosen_item:
                #remvoe 1 item from player inventory
                player.inventory[item_key][1] -= 1
                #if player has no items left, set that slot to be nothing
                if player.inventory[item_key][1] <= 0:
                    player.inventory[item_key][0] = ''
                    player.inventory[item_key][1] = 1
                found_item = True
                break
        #check armour if item was not found in player inventory
        if found_item == False:
            for item_key in player.armour:
                item = player.armour[item_key][0]
                #check if the item is the selected item
                if item == chosen_item:
                    #remvoe 1 item from player inventory
                    player.armour[item_key][1] -= 1
                    #if player has no items left, set that slot to be nothing
                    if player.armour[item_key][1] <= 0:
                        player.armour[item_key][0] = ''
                        player.armour[item_key][1] = 1
                break
        #reset own health
        self.health = self.max_health
        #print what was taken to the screen
        print('Enemy took 1 ' + chosen_item)
        