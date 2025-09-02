#import modules
import random
import math
#battle rendering function
class Battle():
    def __init__(self, item_data):
        self.item_data = item_data
    def render_battle(self, player, enemy):
        #print battle stuff to the screen
        print('')
        print('Your Health: ' + str(player.health), 'Your Energy: ' + str(player.energy))
        print('Enemy Health: ' + str(enemy.health), 'Enemy Energy: ' + str(enemy.energy))
        print('Enemy Stats:')
        print(enemy.armour)
        print(enemy.weapon)
        print('Your Stats:')
        print(player.armour)
        print('Your Attacks:')
        self.assemble_player_attacks(player)
        print('Your Defences:')
        self.assemble_player_defences(player)
    def assemble_player_attacks(self, player):
        '''This function creates the chart of player attacks'''
        #2d list holding player items & moves
        self.player_attacks_chart = [[], [], []]
        #assemble chart from player weapons
        count = 1
        for item in player.weapons:
            self.player_attacks_chart[0].append(item)
            #add attacks to list
            for attack in self.item_data[item]['attacks']:
                self.player_attacks_chart[count].append(attack)
                count += 1 
            #add spaces for proper spacing if item has only 1 attack
            if count == 2:
                self.player_attacks_chart[count].append('   ')
            count = 1
        #print chart to screen
        for row in self.player_attacks_chart:
            print(row)
    def assemble_player_defences(self, player):
        '''This function creates the chart of player attacks'''
        #2d list holding player items & moves
        self.player_defences_chart = [[], []]
        #assemble chart from player weapons
        count = 1
        for item in player.weapons:
            self.player_defences_chart[0].append(item)
            #add attacks to list
            for defence in self.item_data[item]['defences']:
                self.player_defences_chart[count].append(defence)
                count += 1 
            #add spaces for proper spacing if item has only 1 attack
            if count == 1:
                self.player_defences_chart[count].append('   ')
            count = 1
        #print chart to screen
        for row in self.player_defences_chart:
            print(row)
    #function to actully run the battle events
    def battle_round(self, player, enemy, action):
        #check syntax
        if ';' in action:
            action_parts = action.split(';')
            #make sure that it split into the right number of action_parts
            if len(action_parts) != 3:
                return 'Invalid Syntax'
            #check if an avalible weapon is used
            if action_parts[0]  not in player.weapons:
                return 'Invalid Weapon'
            #check if correct target is listed
            if action_parts[2]  not in ['head', 'Head', 'torso', 'Torso', 'legs', 'Legs', 'boots', 'Boots']:
                return 'Invalid Location'
            action_parts[2] = action_parts[2].lower()
            #get player and enemy moves
            if action_parts[1] in self.player_attacks_chart[1]:
                player_move = action_parts[1]
                player_move_type = 'attack'
                move_slot = 1
            elif action_parts[1] in self.player_attacks_chart[2]:
                player_move = action_parts[1]
                player_move_type = 'attack'
                move_slot = 2
            elif action_parts[1] in self.player_defences_chart[1]:
                player_move = action_parts[1]
                player_move_type = 'defence'
            else:
                return 'Invalid Move'
            #get player attack
            if player_move_type == 'attack':
                player_item_list = self.item_data[action_parts[0]]['attacks'][player_move]
                player_damage = player_item_list['defult_damage']
                player_energy_cost = player_item_list['energy_cost']
                #make sure that the player has enough energy
                if player_energy_cost > player.energy:
                    return 'Invalid Move: Not Enough Energy'
            else:
                player_item_list = self.item_data[action_parts[0]]['defences'][player_move]
                #negative energy so you gain it
                player_energy_cost = -3
            #get enemy attack
            enemy_move_string, enemy_chance, enemy_move_type = enemy.battle(player, self.item_data)
            print('Enemy Move: ' + enemy_move_string)
            #check if enemy surrendered
            if enemy_move_string == 'surrender':
                return 'enemy_surrender'
            #get enemy damage/defence
            enemy_move = enemy_move_string.split(';')
            if enemy_move_type == 'attack':
                enemy_item_list = self.item_data[enemy_move[0]]['attacks'][enemy_move[1]]
                enemy_damage = enemy_item_list['defult_damage']
                enemy_energy_cost = enemy_item_list['energy_cost']
            else:
                enemy_item_list = self.item_data[enemy_move[0]]['defences'][enemy_move[1]]
                #negative energy so you gain it
                enemy_energy_cost = -3
            #get enemy armour for attacking Location
            match action_parts[2].lower():
                case 'head':
                    enemy_armour = enemy.armour['Helmet'][0][0].split(' ')[0]
                case 'torso':
                    enemy_armour = enemy.armour['Chestplate'][0][0].split(' ')[0]
                case 'legs':
                    enemy_armour = enemy.armour['leggings'][0][0].split(' ')[0]
                case 'boots':
                    enemy_armour = enemy.armour['Boots'][0][0].split(' ')[0]
                case _:
                    enemy_armour = ''
            #run the battle calculations
            if player_move_type == 'attack':
                player_chance = ((player_item_list['effectivness'][enemy_armour] / 100) * (player_item_list['effectivness'][action_parts[2].lower()] / 100))
                player_range = [player_damage - (player.energy / 3), player_damage + (player.energy / 3)]
                if player_range[0] < 0:
                    player_range[0] = 0
                while player_chance > 1:
                    player_chance /= 10
                player_damage_decimal = random.binomialvariate(n=1, p=player_chance)
                player_damage = (player_range[1] - player_range[0]) * player_damage_decimal
                player_defend = 0
                player_defence = 1
            else:
                player_damage = 0
                weapon_chance = []
                #create player enemy_chance
                for item in enemy.weapon:
                    if item[0] in self.item_data:
                        weapon_chance.append(player_item_list['effectivness'][item[0]])
                #get average of the chances 
                num_chances = len(weapon_chance)
                against_enemy_chance = sum(weapon_chance) / num_chances
                #get chance
                defence_chance = (against_enemy_chance * (player_item_list['effectivness'][action_parts[2]]))
                while defence_chance > 1:
                    defence_chance /= 10
                player_defence_decimal = random.binomialvariate(n=1, p=defence_chance)
                #make it so that larger succsess have a smaller output value
                player_defence = 1.1 - player_defence_decimal
            if enemy_move_type == 'attack':
                enemy_range = [player_damage - (player.energy / 3), player_damage + (player.energy / 3)]
                if enemy_range[0] < 0:
                    enemy_range[0] = 0
                while enemy_chance > 1:
                    enemy_chance /= 10
                enemy_damage_decimal = random.binomialvariate(n=1, p=enemy_chance)
                enemy_damage = (enemy_range[1] - enemy_range[0]) * enemy_damage_decimal
                enemy_defend = 0
                enemy_defence = 1
            else:
                while enemy_chance > 1:
                    enemy_chance /= 10
                enemy_defence_decimal = random.binomialvariate(n=1, p=enemy_chance)
                #make it so that larger succsess have a smaller output value
                enemy_defence = 1.1 - enemy_defence_decimal
                enemy_damage = 0
            #take damage and energy to each opponent
            enemy.health -= int(player_damage * enemy_defence)
            player.health -= int(enemy_damage * player_defence)
            player.energy -= int(player_energy_cost)
            enemy.energy -= int(enemy_energy_cost)
            #check if player or enemy are dead
            if player.health <= 0:
                return 'player_dead'
            elif enemy.health <= 0:
                return 'enemy_dead'
            #it expects a string to be reeturnes
            return 'The Battle Continues'
        elif action == 'surrender' or action == 'Surrender':
            return 'surrender'
        else:
            return 'Invalid Syntax'
