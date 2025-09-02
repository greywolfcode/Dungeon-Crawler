# Online Python - IDE, Editor, Compiler, Interpreter
#import modules
import random
#import files
import proc_gen
import renderer
import player
import map_objects
import battle
import barter
import data
#define global variables
game_state = 'dungeon'
skip = False
skip_died = False
rare_chest = False
#set up settings
setup = True
setup_point = 1
settings = {}
print('Settings:')
input_value = input('Clear console after move (T/F):')
while setup == True:
    if setup_point == 1:
        #check if value is correct
        if input_value == 'T':
            settings['clear_console'] = 'T'
        elif input_value == 'F':
            settings['clear_console'] = 'F'
        else:
            #skip changing setup point if invalid answer is inputter
            print('Not T or F')
            print('Settings:')
            input_value = input('Clear console after move (T/F):')
            continue
        setup_point += 1 
    else:
        setup = False

#set up dungeon
dungeon = None
render = None
print('')
print('Welcome to Dungeon Crawler!')
#create game
def create_game():
    #acsess globals
    global dungeon
    global render
    global player_class
    global chests
    global enemies
    global merchants
    #generate dungeon
    dungeon = proc_gen.generate()
    render = renderer.Renderer(dungeon, proc_gen.rooms_large)
    render.render_game()
    render.print_window()
    player_class = player.Player()
    chests = []
    enemies = []
    merchants = []
create_game()
#battle class never needs to be reset 
battle_class = battle.Battle(data.battle_data)
print('Type help for help.')
action = input('What would you like to do?')
#main game loop
run = True
alive = True
#loop for respawning
while run == True:
    #game loop
    while alive == True:
        if action in ('quit', 'Quit', 'exit', 'Exit'):
            alive = False
            run = False
            skip_died = True
            skip = True
        elif action in ('settings', 'Settings'):
            #record previous game state and change to settings
            previous_game_state = game_state
            game_state = 'settings'
        elif action in ('end game' , 'End game' , 'End Game'):
            break
        #clear console if that setting is enabled
        if settings['clear_console'] == 'T':
            print('\x1bc')
        if game_state == 'dungeon':
            player_class.idle()
            match action:
                case 'w' | 'W'| 'a' | 'A' | 's' | 'S' | 'd'| 'D' :
                    game_state = render.move(action)
                    #skip input if using a worker state
                    if game_state == 'chest_worker':
                        skip = True
                    elif game_state == 'battle_worker':
                        skip = True
                    elif game_state == 'chance':
                        skip = True
                    elif game_state == 'merchant_worker':
                        skip = True
                case 'help' | 'Help':
                    print('Use wasd to move.')
                    print('Type quit to quit.')
                    print('Type new game for a new game')
                case 'new game' | 'New Game' | 'new map' | 'New Map':
                    create_game()
                case 'end game' | 'End game' | 'End Game':
                    break
                case 'inventory' | 'Inventory':
                    game_state = 'inventory'
                    skip = True
                case 'stats' | 'Stats':
                    game_state = 'stats'
                    skip = True
                case _:
                    print('Invalid move')
                    #render map so the map show up if invalid input is give
                    render.print_window()
        elif game_state == 'settings':
            match action:
                case 'help' | 'Help':
                    print('Type back to go back')
                    print('Type a setting name to change the setting')
                case 'back' | 'Back':
                    game_state = previous_game_state
                    skip = True
                case _:
                    if action in settings.keys():
                        setting = action
                        game_state = 'change_setting'
                        skip = True
                    else:
                        print('Invalid setting')
            for setting in settings:
                print(setting + ': ', settings[setting])
        elif game_state == 'change_setting':
            skip_selection = False
            match action:
                case 'back' | 'Back':
                    skip_selection = True
                    game_state == 'settings'
            if skip_selection == True:
                skip = True
            else:
                match setting:
                    case 'clear_console':
                        print('Clear console after move (T/F):')
                        if action == 'T':
                            settings['clear_console'] = 'T'
                            skip = True
                            game_state = 'settings'
                        elif action == 'F':
                            settings['clear_console'] = 'F'
                            skip = True
                            game_state = 'settings'
                        else:
                            #skip changing setup point if invalid answer is inputter
                            print('Not T or F')
        elif game_state == 'inventory':
            render.print_window()
            #state to view inventory
            match action:
                case 'back' | 'Back' :
                    game_state = 'dungeon'
                    render.print_window()
                case 'help' | 'Help':
                    print('Type back to go back')
                    print('To move items: \n slot 1 number;slot 2 number \n use 11-13 for armour slots')
                case _:
                    #check if given a command to move slots
                    if ';' in action:
                        #split slot numbers
                        slots = action.split(';')
                        if int(slots[0]) <=14 and int(slots[1]) <= 14 and int(slots[0]) >= 1 and int(slots[1]) >= 1:
                            #swap slots, have to make to make it longer because armour doesn't use numbers for id
                            if int(slots[0]) <= 10:
                                item_1 = player_class.inventory[f'slot_' + slots[0]]
                            else:
                                match slots[0]:
                                    case '11':    
                                        item_1 = player_class.armour['helmet']
                                    case '12':
                                        item_1 = player_class.armour['chestplate']
                                    case '13':
                                        item_1 = player_class.armour['leggings']
                                    case '14':
                                        item_1 = player_class.armour['boots']
                            if int(slots[1]) <= 10:
                                item_2 = player_class.inventory[f'slot_' + slots[1]]
                            else:
                                match slots[1]:
                                    case '11':    
                                        item_2 = player_class.armour['helmet']
                                    case '12':
                                        item_2 = player_class.armour['chestplate']
                                    case '13':
                                        item_2 = player_class.armour['leggings']
                                    case '14':
                                        item_2 = player_class.armour['boots']
                            #check if items can stack
                            if item_1[0] == item_2[0]:
                                #set first slot to nothing
                                if int(slots[0]) <= 10:
                                    player_class.inventory[f'slot_' + slots[0]] = ['', 1]
                                else:
                                    match slots[0]:
                                        case '11':    
                                            player_class.armour['helmet'] = ['', 1]
                                        case '12':
                                            player_class.armour['chestplate'] = ['', 1]
                                        case '13':
                                            player_class.armour['leggings'] = ['', 1]
                                        case '14':
                                            player_class.armour['boots'] = ['', 1]
                                if int(slots[1]) <= 10:
                                    #combined stacks to 2nd slot
                                    player_class.inventory[f'slot_' + slots[1]] = [item_1[0], item_2[1] + item_1[1]]
                                else:
                                    match slots[1]:
                                        case '11':    
                                            player_class.armour['helmet'] = [item_1[0], item_2[1] + item_1[1]]
                                        case '12':
                                            player_class.armour['chestplate'] = [item_1[0], item_2[1] + item_1[1]]
                                        case '13':
                                            player_class.armour['leggings'] = [item_1[0], item_2[1] + item_1[1]]
                                        case '14':
                                            player_class.armour['boots'] = [item_1[0], item_2[1] + item_1[1]]
                            #just swap items if they cannot stack
                            else:
                                if int(slots[0]) <= 10:
                                    player_class.inventory[f'slot_' + slots[0]] = item_2
                                else:
                                    match slots[0]:
                                        case '11':    
                                            player_class.armour['helmet'] = item_2
                                        case '12':
                                            player_class.armour['chestplate'] = item_2
                                        case '13':
                                            player_class.armour['leggings'] = item_2
                                        case '14':
                                            player_class.armour['boots'] = item_2
                                if int(slots[1]) <= 10:
                                    player_class.inventory[f'slot_' + slots[1]] = item_1
                                else:
                                    match slots[1]:
                                        case '11':    
                                            player_class.armour['helmet'] = item_1
                                        case '12':
                                            player_class.armour['chestplate'] = item_1
                                        case '13':
                                            player_class.armour['leggings'] = item_1
                                        case '14':
                                            player_class.armour['boots'] = item_1
                        else:
                            print('Invalid Slot')
                    print('Inventory:')
                    print(player_class.inventory)
                    print(player_class.armour)
        elif game_state == 'stats':
            render.print_window()
            #state to view player stats
            match action:
                case 'back' | 'Back' :
                    game_state = 'dungeon'
                    render.print_window()
                case 'help' | 'Help':
                    print('Type back to go back')
                case _:
                    print('Stats:')
                    print('Max Health: ' + str(player_class.max_health))
                    print('Current Health: ' + str(player_class.health))
                    print('Strength: ' + str(player_class.strength))
        elif game_state == 'chest_worker':
            current_chest = None
            #check if a chest has already been generated at this position
            for chest in chests:
                if chest.location == render.player_pos:
                    current_chest = chests.index(chest)
                    break 
            if current_chest == None:
                #create new chest using player location
                current_chest = len(chests)
                #this allows for the chance spots to have rarer items
                if rare_chest == True:
                    chests.append(map_objects.Chest(render.player_pos[0], render.player_pos[1], data.items, 'rare'))
                    rare_chest = False
                else:
                    chests.append(map_objects.Chest(render.player_pos[0], render.player_pos[1], data.items, 'common'))
            game_state = 'chest'
            print(chests[current_chest].items)
            print(player_class.inventory)
            skip = True
        elif game_state == 'chest':
            render.print_window()
            match action:
                #go back if you press back
                case 'back' | 'Back':
                    game_state = 'dungeon'
                    render.print_window()
                case 'help' | 'help':
                    print('Type back to go back')
                    print('To move items type: \n chest slot number;inventory slot number')
                case _:
                    if ';' in action:
                        slots = action.split(';')
                        #ensure slots are numbers and in range
                        if slots[0].isnumeric() and slots[1].isnumeric():
                            if int(slots[0]) <=5 and int(slots[1]) <= 10:
                                #swap slots
                                player_item = player_class.inventory[f'slot_' + slots[1]]
                                chest_item = chests[current_chest].items[f'slot_' + slots[0]]
                                #check if items can stack
                                if player_item[0] == chest_item[0]:
                                    #set chest slot to nothing
                                    chests[current_chest].items[f'slot_' + slots[0]] = ['', 1]
                                    #combined stacks to player slot
                                    player_class.inventory[f'slot_' + slots[1]] = [player_item[0], player_item[1] + chest_item[1]]
                                #just swap items if they cannot stack
                                else:
                                    player_class.inventory[f'slot_' + slots[1]] = chest_item
                                    chests[current_chest].items[f'slot_' + slots[0]] = player_item  
                                
                            else:
                                print('Invalid Slot')
                        else:
                            print('Invalid Slot')
                    print(chests[current_chest].items)
                    print(player_class.inventory)
        elif game_state == 'battle_worker':
            current_enemy = None
            player_class.prep_battle()
            #check if an enemy has already been generated at this position
            if render.player_on in ['O' , 'G' , 'B' , 'E' , 'K']:
                for enemy in enemies:
                    if enemy.location == render.player_pos:
                        current_enemy = enemies.index(enemy)
                        break 
                if current_enemy == None:
                    #create new chest using player location
                    current_enemy = len(enemies)
                    enemies.append(map_objects.Enemy(render.player_pos[0], render.player_pos[1], render.player_on, data.items))
                game_state = 'battle'
                battle_class.render_battle(player_class, enemies[current_enemy])
            else:
                #change this once wizards are made
                game_state = 'dungeon'
        elif game_state == 'battle':
            render.print_window()
            if action == 'help':
                print('Type a weapon, attack and location (head, torso, legs, boots) to attack \n For Example: Sword;Stab;Legs')
                print('Type surrender to surrender')
                print('Type quit to quit')
            else:
                move = battle_class.battle_round(player_class, enemies[current_enemy], action)
                battle_class.render_battle(player_class, enemies[current_enemy])
                #take action based on move if required
                if 'Invalid' in move:
                    #print error message if something in the input was wrong
                    print(move)
                elif move == 'surrender':
                    game_state = 'surrender'
                    skip = True
                elif move == 'player_dead':
                    alive = False
                    skip = True
                elif move == 'enemy_dead':
                    game_state = 'enemy_dead'
                    skip = True
                elif move == 'enemy_surrender':
                    game_state = 'enemy_surrender_worker'
                    #print items to console
                    skip = True
        elif game_state == 'enemy_dead':
            print('Victory!')
            render.change_pos(render.player_pos, ' ')
            game_state = 'get_loot'
            #convert armour dict to list so all enemy items can be combined
            enemy_armour = []
            for item in enemies[current_enemy].armour.values():
                enemy_armour.append(item[0])
                #combined all enemy items into 1 list
            enemy_slots = enemies[current_enemy].other_items + enemies[current_enemy].weapon + enemy_armour
            #print items to console
            print(enemy_slots)
            print('')
            print(player_class.inventory)
            print(player_class.armour)
        elif game_state == 'enemy_surrender_worker':
            print('Your enemy Surrendered.')
            print('As an honourable warriour, you will only claim one item from them \n in return to spare their life.')
            render.change_pos(render.player_pos, ' ')
            game_state = 'enemy_surrender'
            #convert armour enemy_surrender to list so all enemy items can be combined
            enemy_armour = []
            for item in enemies[current_enemy].armour.values():
                enemy_armour.append(item[0])
                #combined all enemy items into 1 list
            enemy_slots = enemies[current_enemy].other_items + enemies[current_enemy].weapon + enemy_armour
            #print items to console
            print(enemy_slots)
            print('')
            print(player_class.inventory)
            print(player_class.armour)
        elif game_state == 'enemy_surrender':
            render.print_window()
            match action:
                case 'done' | 'Done':
                    #send back to dungeon if done
                    game_state = 'dungeon'
                    render.render_game()
                    render.print_window()
                case 'help':
                    print('Type done to return to the dungeon')
                    print('To move items: \n slot 1 number;slot 2 number \n use 11-13 for armour slots')
                    print('To get enemy slot number, start counting up from 1')
                case _:
                    if ';' in action:
                        slots = action.split(';')
                        if slots[0].isnumeric() and slots[1].isnumeric():
                            if int(slots[0]) <= len(enemy_slots) and int(slots[1]) <= 14:
                                #get player slot, more complicated to involve armour. See inventory state
                                if int(slots[1]) <= 10:
                                    item_1 = player_class.inventory[f'slot_' + slots[1]]
                                else:
                                    match slots[1]:
                                        case '11':    
                                            item_1 = player_class.armour['helmet']
                                        case '12':
                                            item_1 = player_class.armour['chestplate']
                                        case '13':
                                            item_1 = player_class.armour['leggings']
                                        case '14':
                                            item_1 = player_class.armour['boots']
                                #get enemy item to swap
                                item_2 = enemy_slots[int(slots[0]) - 1]
                                #check if items can stack
                                if item_1[0] == item_2[0]:
                                    #set enemy slot to nothing
                                    enemy_slots[int(slots[0]) - 1] = ['', 1]
                                        #combined stacks to player slot
                                    if int(slots[0]) <= 10:
                                        player_class.inventory[f'slot_' + slots[1]] = [item_1[0], item_2[1] + item_1[1]]
                                    else:
                                        match slots[1]:
                                            case '11':    
                                                player_class.armour['helmet'] = [item_1[0], item_2[1] + item_1[1]]
                                            case '12':
                                                player_class.armour['chestplate'] = [item_1[0], item_2[1] + item_1[1]]
                                            case '13':
                                                player_class.armour['leggings'] = [item_1[0], item_2[1] + item_1[1]]
                                            case '14':
                                                player_class.armour['boots'] = [item_1[0], item_2[1] + item_1[1]]
                                #just swap items if they cannot stack
                                else:
                                    if int(slots[1]) <= 10:
                                            player_class.inventory[f'slot_' + slots[1]] = item_2
                                    else:
                                        match slots[1]:
                                            case '11':    
                                                player_class.armour['helmet'] = item_2
                                            case '12':
                                                player_class.armour['chestplate'] = item_2
                                            case '13':
                                                player_class.armour['leggings'] = item_2
                                            case '14':
                                                player_class.armour['boots'] = item_2
                                    enemy_slots[int(slots[0]) - 1] = item_1
                                #send back to dungeon once item is taken
                                game_state = 'dungeon'
                                render.render_game()
                                render.print_window()
                        else:
                            print('Invalid Slot')
                            print(enemy_slots)
                            print('')
                            print(player_class.inventory)
                            print(player_class.armour)
                    else:
                        print('Invalid Slot')
                        print(enemy_slots)
                        print('')
                        print(player_class.inventory)
                        print(player_class.armour)
        elif game_state == 'get_loot':
            render.print_window()
            match action:
                case 'done' | 'Done':
                    #send back to dungeon if done
                    game_state = 'dungeon'
                    render.render_game()
                    render.print_window()
                case 'help':
                    print('Type done to return to the dungeon')
                    print('To move items: \n slot 1 number;slot 2 number \n use 11-13 for armour slots')
                    print('To get enemy slot number, start counting up from 1')
                case _:
                    if ';' in action:
                        slots = action.split(';')
                        if slots[0].isnumeric() and slots[1].isnumeric():
                            if int(slots[0]) <= len(enemy_slots) and int(slots[1]) <= 14:
                                #get player slot, more complicated to involve armour. See inventory state
                                if int(slots[1]) <= 10:
                                    item_1 = player_class.inventory[f'slot_' + slots[1]]
                                else:
                                    match slots[1]:
                                        case '11':    
                                            item_1 = player_class.armour['helmet']
                                        case '12':
                                            item_1 = player_class.armour['chestplate']
                                        case '13':
                                            item_1 = player_class.armour['leggings']
                                        case '14':
                                            item_1 = player_class.armour['boots']
                                #get enemy item to swap
                                item_2 = enemy_slots[int(slots[0]) - 1]
                                #check if items can stack
                                if item_1[0] == item_2[0]:
                                    #set enemy slot to nothing
                                    enemy_slots[int(slots[0]) - 1] = ['', 1]
                                        #combined stacks to player slot
                                    if int(slots[0]) <= 10:
                                        player_class.inventory[f'slot_' + slots[1]] = [item_1[0], item_2[1] + item_1[1]]
                                    else:
                                        match slots[1]:
                                            case '11':    
                                                player_class.armour['helmet'] = [item_1[0], item_2[1] + item_1[1]]
                                            case '12':
                                                player_class.armour['chestplate'] = [item_1[0], item_2[1] + item_1[1]]
                                            case '13':
                                                player_class.armour['leggings'] = [item_1[0], item_2[1] + item_1[1]]
                                            case '14':
                                                player_class.armour['boots'] = [item_1[0], item_2[1] + item_1[1]]
                                #just swap items if they cannot stack
                                else:
                                    if int(slots[1]) <= 10:
                                            player_class.inventory[f'slot_' + slots[1]] = item_2
                                    else:
                                        match slots[1]:
                                            case '11':    
                                                player_class.armour['helmet'] = item_2
                                            case '12':
                                                player_class.armour['chestplate'] = item_2
                                            case '13':
                                                player_class.armour['leggings'] = item_2
                                            case '14':
                                                player_class.armour['boots'] = item_2
                                    enemy_slots[int(slots[0]) - 1] = item_1
                        else:
                            print('Invalid Slot')
                    else:
                        print('Invalid Slot')
                    #print items to console
                    print(enemy_slots)
                    print('')
                    print(player_class.inventory)
                    print(player_class.armour)
        elif game_state == 'surrender':
            render.print_window()
            #allow enemy to take item(s), then move to dungon state
            enemies[current_enemy].victory(player_class)
            game_state = 'dungeon'
            skip = True
        elif game_state == 'chance':
            #choose chest or enemy, chagne map to have correct icon, and move to that worker state
            object_type = random.choice(['chest', 'enemy'])
            if object_type == 'chest':
                render.change_pos(render.player_pos, 'C')
                game_state = 'chest_worker'
                rare_chest = True
                skip = True
            elif object_type == 'enemy':
                render.change_pos(render.player_pos, 'B')
                render.player_on = 'B'
                game_state = 'battle_worker'
                skip = True
        elif game_state == 'merchant_worker':
            current_merchant = None
            #check if a merchant has already been generated at this position
            for merchant in merchants:
                if merchant.location == render.player_pos:
                    current_merchant = merchants.index(merchant)
                    break 
            if current_merchant == None:
                #create new chest using player location
                current_merchant = len(merchants)
                merchants.append(barter.Merchant(render.player_pos[0], render.player_pos[1], data.items))
            game_state = 'merchant'
            skip = True
        elif game_state == 'merchant':
            render.print_window()
            match action:
                #go back if you press back
                case 'back' | 'Back':
                    game_state = 'dungeon'
                    render.print_window()
                case 'help' | 'Help':
                    print('type back to go back')
                    print("to make an offer type: \n offer merchant item num;merchant item amount;your item name;num you're giving")
                    print('For example: offer 1;1;Bread;1')
                    print('Slot Numbers increase going across')
                case _:
                    print('Merchant items:')
                    merchants[current_merchant].print_barter_list()
                    print('Your inventory:')
                    print(player_class.inventory)
                    #offer 1;1;sword;1
                    if 'offer' in action:
                        offer = action.split(' ')
                        #error handling in case player dosen't put a space between offer and number (i.e. offer1;1 etc.)
                        try:
                         offer_parts = offer[1].split(';')
                        except:
                            print('Invalid Syntax')
                        else:
                            #error handling
                            if len(offer_parts) == 4:
                                #make sure all parts of offer are right
                                if offer_parts[0].isnumeric() and offer_parts[1].isnumeric() and offer_parts[3].isnumeric():
                                    #check if you have the item
                                    item_type = offer_parts[2]
                                    completed_trade = False
                                    not_enough = False
                                    #find the right item
                                    for item in player_class.inventory.values():
                                        if item[0] == item_type:
                                            #check if you have enough of the item
                                            if item[1] >= int(offer_parts[3]):
                                                trade_state = merchants[current_merchant].barter(offer_parts)
                                                if trade_state == 'not_enough_of_item_error':
                                                    print('Merchant does not have enough of requested item')
                                                    break
                                                elif trade_state == True:
                                                    #find slot with selected item in the inventory
                                                    for item_slot in merchants[current_merchant].inventory:
                                                        #get the item name of the item the player wants
                                                        offer_item = merchants[current_merchant].inventory['slot_' + offer_parts[0]][0]
                                                        if merchants[current_merchant].inventory[item_slot][0] == offer_item:
                                                            #iterate through all player items to find where to put the slot
                                                            found_slot = False
                                                            for item_key in player_class.inventory:
                                                                #check if slot has same item as one selected in offer 
                                                                if player_class.inventory[item_key][0] == offer_item:
                                                                    player_class.inventory[item_key][1] += int(offer_parts[1])
                                                                    found_slot = True
                                                                    break
                                                            #if player has none of the same item, iterate trhough slots to find an empty slot
                                                            if found_slot == False:
                                                                for item_key in player_class.inventory:
                                                                    if player_class.inventory[item_key][0] == '':
                                                                        player_class.inventory[item_key][0] = offer_item
                                                                        player_class.inventory[item_key][1] = int(offer_parts[1])
                                                                        found_slot = True
                                                                        break
                                                            #cancel trade if player has no slots
                                                            if found_slot == False:
                                                                print('You have no space for this item')
                                                                continue
                                                            #remove the amount specified to trade
                                                            merchants[current_merchant].inventory[item_slot][1] -= int(offer_parts[0])
                                                            #if there are no items left just remove the slot
                                                            if merchants[current_merchant].inventory[item_slot][1] <= 0:
                                                                merchants[current_merchant].inventory[item_slot][0] = ''
                                                                merchants[current_merchant].inventory[item_slot][1] = 0
                                                            break
                                                    #add item to merchnt's inventory. Seperated from above so that it can be cancelled if the player doesn't have the item
                                                    found_slot = False
                                                    for item_slot in merchants[current_merchant].inventory:
                                                        if merchants[current_merchant].inventory[item_slot][0] == offer_parts[2]:
                                                            #currently a string, need to change that
                                                            merchants[current_merchant].inventory[item_slot][1] += int(offer_parts[3])
                                                            found_slot = True
                                                            break
                                                    #add a new slot if the merchant has none of the item already.
                                                    if found_slot == False:
                                                        #get last slot number
                                                        last_key = list(merchants[current_merchant].inventory)[-1]
                                                        #get key number
                                                        key_number = int(last_key[5:])
                                                        #add item to merchant inventory
                                                        merchants[current_merchant].inventory[f'slot_{key_number + 1}'] = [offer_parts[2],int(offer_parts[3])]
                                                    #remove item from player inventory
                                                    for slot in player_class.inventory:
                                                        if player_class.inventory[slot][0] == offer_parts[2]:
                                                            #remove paid amount of item from inventory
                                                            player_class.inventory[slot][1] -= int(offer_parts[3])
                                                            #set slot to empty if total is now 0 
                                                            if player_class.inventory[slot][1] <= 0:
                                                                player_class.inventory[slot][0] = ''
                                                                player_class.inventory[slot][1] = 1
                                                            break
                                                    print('Trade Complete')
                                                    completed_trade = True
                                                    #print stuff agian; just skipping input makes the for action run twice
                                                    print('Merchant items:')
                                                    merchants[current_merchant].print_barter_list()
                                                    print('Your inventory:')
                                                    print(player_class.inventory)
                                                else:
                                                    print('No Deal')
                                                    print(merchants[current_merchant].counter_offer)
                                                    break 
                                            else:
                                                not_enough = True
                                        if completed_trade == True:
                                            break
                                    if completed_trade == False:
                                        if not_enough == True:
                                            print('You do not have enough of that item')
                                        else:
                                            print('You do not have that item')
                                else:
                                    print('Invalid Syntax')
                            else:
                                print('Invalid Offer')
                    else:
                        print('Invalid Syntax')
        #this allows worker functions to skip unnessecary inputs
        if skip == False:
            action = input('What would you like to do?')
        else:
            skip = False
            print('')
    #if you are not alive, this code will run
    if skip_died == False:
        print('You Died')
        print('')
        print('Type New Game for new game, type Quit to quit, or type Show Map to see the map ')
        action = input('What would you like to do?')
        match action:
            case 'new game' | 'New game' | 'New Game': 
                #clear console
                if settings['clear_console'] == 'T':
                    print('\x1bc')
                create_game()
                game_state = 'dungeon'
                alive = True
            case 'show map' | 'Show Map':
                #clear console
                if settings['clear_console'] == 'T':
                    print('\x1bc')
                render.print_game_map()
                alive = False
            case 'help' | 'Help':
                #clear console
                if settings['clear_console'] == 'T':
                    print('\x1bc')
                print('Type New Game for new game, type Quit to quit, or type Show Map to see the map ')
            case 'quit' | 'Quit' | 'exit' | 'Exit':
                break
                    