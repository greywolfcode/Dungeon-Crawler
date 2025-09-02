#import modules
import random
#random.seed(80)
import renderer
#Possible room Configurations. door directions follow WASD
rooms_small = {
    1:([
        ['## ##'],
        ['#   #'],
        ['#   #'],
        ['#   #'],
        ['#####'],
      ], (True, False, False, False)),
    2:([
        ['#####'],
        ['#   #'],
        ['#   #'],
        ['#   #'],
        ['## ##'],
      ], (False, False, True, False)),
    3:([
        ['#####'],
        ['#   #'],
        ['    #'],
        ['#   #'],
        ['#####'],
      ], (False, True, False, False)),
    4:([
        ['#####'],
        ['#   #'],
        ['#    '],
        ['#   #'],
        ['#####'],
      ], (False, False, False, True)),
    5:([
        ['#####'],
        ['#   #'],
        ['     '],
        ['#   #'],
        ['#####'],
      ], (False, True, False, True)),
    6:([
        ['## ##'],
        ['#   #'],
        ['#   #'],
        ['#   #'],
        ['## ##'],
      ], (True, False, True, False)),
    7:([
        ['## ##'],
        ['#   #'],
        ['     '],
        ['#   #'],
        ['## ##'],
      ], (True, True, True, True)),
    8:([
        ['## ##'],
        ['#   #'],
        ['    #'],
        ['#   #'],
        ['#####'],
      ], (True, True, False, False)),
    9:([
        ['## ##'],
        ['#   #'],
        ['#    '],
        ['#   #'],
        ['#####'],
      ], (True, False, False, True)),
    10:([
        ['#####'],
        ['#   #'],
        ['    #'],
        ['#   #'],
        ['## ##'],
      ], (False, True, True, False)),
    11:([
        ['#####'],
        ['#   #'],
        ['#    '],
        ['#   #'],
        ['## ##'],
      ], (False, False, True, True)),
    12:([
        ['## ##'],
        ['#   #'],
        ['     '],
        ['#   #'],
        ['#####'],
      ], (True, True, False, True)),
    13:([
        ['#####'],
        ['#   #'],
        ['     '],
        ['#   #'],
        ['## ##'],
      ], (False, True, True, True)),
    14:([
        ['## ##'],
        ['#   #'],
        ['    #'],
        ['#   #'],
        ['## ##'],
      ], (True, True, True, False)),
    15:([
        ['## ##'],
        ['#   #'],
        ['#    '],
        ['#   #'],
        ['## ##'],
      ], (True, False, True, True)),
    16:([
        ['#####'],
        ['#   #'],
        ['#1 6#'],
        ['#   #'],
        ['#####'],
      ], (False, False, False, False)),
}
rooms_large = {
    1:([
        ['### ###'],
        ['#     #'],
        ['#     #'],
        ['#     #'],
        ['#     #'],
        ['#     #'],
        ['#######'],
      ], (True, False, False, False)),
    2:([
        ['#######'],
        ['#     #'],
        ['#     #'],
        ['#     #'],
        ['#     #'],
        ['#     #'],
        ['### ###'],
      ], (False, False, True, False)),
    3:([
        ['#######'],
        ['#     #'],
        ['#     #'],
        ['      #'],
        ['#     #'],
        ['#     #'],
        ['#######'],
      ], (False, True, False, False)),
    4:([
        ['#######'],
        ['#     #'],
        ['#     #'],
        ['#      '],
        ['#     #'],
        ['#     #'],
        ['#######'],
      ], (False, False, False, True)),
    5:([
        ['#######'],
        ['#     #'],
        ['#     #'],
        ['       '],
        ['#     #'],
        ['#     #'],
        ['#######'],
      ], (False, True, False, True)),
    6:([
        ['### ###'],
        ['#     #'],
        ['#     #'],
        ['#     #'],
        ['#     #'],
        ['#     #'],
        ['### ###'],
      ], (True, False, True, False)),
    7:([
        ['### ###'],
        ['#     #'],
        ['#     #'],
        ['       '],
        ['#     #'],
        ['#     #'],
        ['### ###'],
      ], (True, True, True, True)),
    8:([
        ['### ###'],
        ['#     #'],
        ['#     #'],
        ['      #'],
        ['#     #'],
        ['#     #'],
        ['#######'],
      ], (True, True, False, False)),
    9:([
        ['### ###'],
        ['#     #'],
        ['#     #'],
        ['#      '],
        ['#     #'],
        ['#     #'],
        ['#######'],
      ], (True, False, False, True)),
    10:([
        ['#######'],
        ['#     #'],
        ['#     #'],
        ['      #'],
        ['#     #'],
        ['#     #'],
        ['### ###'],
      ], (False, True, True, False)),
    11:([
        ['#######'],
        ['#     #'],
        ['#     #'],
        ['#      '],
        ['#     #'],
        ['#     #'],
        ['### ###'],
      ], (False, False, True, True)),
    12:([
        ['### ###'],
        ['#     #'],
        ['#     #'],
        ['       '],
        ['#     #'],
        ['#     #'],
        ['#######'],
      ], (True, True, False, True)),
    13:([
        ['#######'],
        ['#     #'],
        ['#     #'],
        ['       '],
        ['#     #'],
        ['#     #'],
        ['### ###'],
      ], (False, True, True, True)),
    14:([
        ['### ###'],
        ['#     #'],
        ['#     #'],
        ['      #'],
        ['#     #'],
        ['#     #'],
        ['### ###'],
      ], (True, True, True, False)),
    15:([
        ['### ###'],
        ['#     #'],
        ['#     #'],
        ['#      '],
        ['#     #'],
        ['#     #'],
        ['### ###'],
      ], (True, False, True, True)),
    16:([
        ['#######'],
        ['#     #'],
        ['#     #'],
        ['# 1 6 #'],
        ['#     #'],
        ['#     #'],
        ['#######'],
      ], (False, False, False, False)),
}
#function to generate layout
def generate(rooms=rooms_large):
    #get number of iterations
    got_iterations = False
    #need to use loop so code deosnt break if a non number is enterd
    while not got_iterations:
        limit = input('Enter number of iterations.')
        if limit.isnumeric():
            limit = int(limit)
            got_iterations = True
            break
        else:
            print('Not a Number')
    print("Generating Dungeon...")
    #start room is a random room
    start_room = random.choice(list(rooms.items()))
    start_room_id = start_room[0]
    #stops generation after it hits the limit
    count = 0 
    #room values: coords, type of room, connecting room nums, number of avalible connections 
    #rooms that still have open doorways
    active_rooms = {
                    0: [(0,0), start_room_id, 0, rooms[start_room_id][1].count(True), 0],
                   }
    #rooms that have all doorways closed
    completed_rooms = {}
    #rooms that have just been created
    temp_rooms = {}
    #loop to generate rooms
    room_id = 0
    def room_generation(direction, final, coords):
        #get variables from outer function
        nonlocal room_id
        nonlocal active_rooms
        nonlocal temp_rooms
        nonlocal completed_rooms
        nonlocal count
        #recursive helper function to generate all combinations
        def generate_combinations(w=None, a=None, s=None, d=None):
            #helper function to generate combinations
            def generate_combos(values, current_combo):
                #getout clause; exit if all of wasd have been used (if values arg. is empty) 
                #and add the combination to the list of all combinations
                if len(values) == 0:
                    combinations.append(tuple(current_combo))
                    return
                current_value = values[0]
                if current_value is None:
                    #call self using values with the just added value removed (eg. wasd -> asd)
                    #do one for each of True/False as no value is selected
                    generate_combos(values[1:], current_combo + [True])
                    generate_combos(values[1:], current_combo + [False])
                else:
                    #call self using values with the just added value removed (eg. wasd > asd)
                    generate_combos(values[1:], current_combo + [current_value])
            combinations = []
            values = [w, a, s, d]
            #call helper function
            generate_combos(values, [])
            #return final list of combinations
            return combinations
        #set up lists & arrays
        specified_directions = {}
        #ensure the room doesn't exist already; exit function if it does
        match direction:
            case "w":
                if [key for key, value in active_rooms.items() if (coords[0], coords[1] + 1) in value] != []:
                    return 
                elif [key for key, value in temp_rooms.items() if (coords[0], coords[1] + 1) in value] != []:
                    return 
                elif [key for key, value in completed_rooms.items() if (coords[0], coords[1] + 1) in value] != []:
                    return 
            case "a":
                if [key for key, value in active_rooms.items() if (coords[0] - 1, coords[1]) in value] != []:
                    return
                elif [key for key, value in temp_rooms.items() if (coords[0] - 1, coords[1]) in value] != []:
                    return 
                elif [key for key, value in completed_rooms.items() if (coords[0] - 1, coords[1]) in value] != []:
                    return 
            case "s":
                if [key for key, value in active_rooms.items() if (coords[0], coords[1] - 1) in value] != []:
                    return 
                elif [key for key, value in temp_rooms.items() if (coords[0], coords[1] - 1) in value] != []:
                    return
                elif [key for key, value in completed_rooms.items() if (coords[0], coords[1] - 1) in value] != []:
                    return
            case "d":
                if [key for key, value in active_rooms.items() if (coords[0], coords[1] - 1) in value] != []:
                    return
                elif [key for key, value in temp_rooms.items() if (coords[0], coords[1] - 1) in value] != []:
                    return
                elif [key for key, value in completed_rooms.items() if (coords[0], coords[1] - 1) in value] != []:
                    return
        #check rooms around to figure out what piece is required
        match direction:
            case "w" | "a" | "d":
                up_key = [key for key, value in active_rooms.items() if (coords[0], coords[1] + 2) in value]
                if up_key == []:
                    up_key = [key for key, value in temp_rooms.items() if (coords[0] + 1, coords[1] + 2) in value]
            case "w" | "a" | "s":
                left_key = [key for key, value in active_rooms.items() if (coords[0] - 1, coords[1] + 1) in value]
                if left_key == []:
                    left_key = [key for key, value in temp_rooms.items() if (coords[0] - 1, coords[1] +1) in value]
            case "a" | "s" | "d":
                down_key = [key for key, value in active_rooms.items() if (coords[0] - 1, coords[1] - 1) in value]
                if down_key == []:
                    down_key = [key for key, value in temp_rooms.items() if (coords[0] -1, coords[1] - 1) in value]
            case "w" | "s" | "d":
               right_key = [key for key, value in active_rooms.items() if (coords[0] + 1, coords[1] + 1) in value]
               if right_key == []:
                   right_key = [key for key, value in temp_rooms.items() if (coords[0] + 1, coords[1] + 1) in value]
        #specify where doors must be based on what rooms are found
        #note that for the up direction, the down door is the one to check, and vice versa
        match direction:
            case "w":
                specified_directions['s'] = True
            case "a":
                specified_directions['d'] = True
            case "s":
                specified_directions['w'] = True
            case "d":
                specified_directions['a'] = True
        #set true or false for the directions found. check active and temp rooms
        match direction:
            case "w" | "a" | "d":
                if up_key != []:
                    try:
                        if rooms[active_rooms[up_key[0]][1]][1][2]:
                            specified_directions['w'] = True
                        else:
                            specified_directions['w'] = False
                    except:
                        if rooms[temp_rooms[up_key[0]][1]][1][2]:
                            specified_directions['w'] = True
                        else:
                            specified_directions['w'] = False
            case "w" | "a" | "s":
                if left_key != []:
                    try:
                        if rooms[active_rooms[left_key[0]][1]][1][3]:
                            specified_directions['a'] = True
                        else:   
                            specified_directions['a'] = False
                    except:
                        if rooms[temp_rooms[left_key[0]][1]][1][3]:
                            specified_directions['a'] = True
                        else:   
                            specified_directions['a'] = False
            case "a" | "s" | "d":
                if down_key != []:
                    try:
                        if rooms[active_rooms[down_key[0]][1]][1][1]:
                            specified_directions['s'] = True
                        else:
                            specified_directions['s'] = False
                    except:
                        if rooms[temp_rooms[down_key[0]][1]][1][1]:
                            specified_directions['s'] = True
                        else:
                            specified_directions['s'] = False
            case "w" | "s" | "d":
                if right_key != []:
                    try:
                        if rooms[active_rooms[right_key[0]][1]][1][1]:
                            specified_directions['d'] = True
                        else:
                            specified_directions['d'] = False
                    except:
                        if rooms[temp_rooms[right_key[0]][1]][1][1]:
                            specified_directions['d'] = True
                        else:
                            specified_directions['d'] = False
        #if this fucntion is being run to close any open doors, any not specified doors need to be false
        if final == False:
            if 'w' not in specified_directions:
                specified_directions['w'] = None
            if 'a' not in specified_directions:
                specified_directions['a'] = None
            if 's' not in specified_directions:
                specified_directions['s'] = None
            if 'd' not in specified_directions:
                specified_directions['d'] = None
        else:
            if 'w' not in specified_directions:
                specified_directions['w'] = False
            if 'a' not in specified_directions:
                specified_directions['a'] = False
            if 's' not in specified_directions:
                specified_directions['s'] = False
            if 'd' not in specified_directions:
                specified_directions['d'] = False
        #create all possible combinations of doors and no doors. If door/wall is not specified, there are two options generated
        if final == False:
            #combonation for all specified direction possobilities
            for num in range(0, 5 - len(specified_directions)):
                possible_combonations = generate_combinations(specified_directions['w'], specified_directions['a'], specified_directions['s'], specified_directions['d'])
        else:
            #final rooms have all combonations specified
            possible_combonations = [(specified_directions['w'], specified_directions['a'], specified_directions['s'], specified_directions['d'])]
        #based on door locations, create list of possible rooms
        possible_rooms = []
        for temp_room in rooms:
            if rooms[temp_room][1] in possible_combonations:
                possible_rooms.append(temp_room)
        new_room = random.choice(possible_rooms)
        room_id += 1
        #find number of connections for newly created room
        connections = 1
        match direction:
            case "w" | "a" | "d":
                if up_key != []:
                    connections += 1
            case "w" | "a" | "s":
                if left_key != []:
                    connections += 1
            case "a" | "s" | "d":
                if down_key != []:
                    connections += 1
            case "w" | "s" | "d":
                if right_key != []:
                    connections += 1
        #add to temp rooms
        match direction:
            case "w":
                temp_rooms[room_id] = [(coords[0], coords[1] + 1), new_room, connections, rooms[new_room][1].count(True), count]
            case "a":
                temp_rooms[room_id] = [(coords[0] - 1, coords[1]), new_room, connections, rooms[new_room][1].count(True), count]
            case "s":
                temp_rooms[room_id] = [(coords[0], coords[1] - 1), new_room, connections, rooms[new_room][1].count(True), count]
            case "d":
                temp_rooms[room_id] = [(coords[0] + 1, coords[1]), new_room, connections, rooms[new_room][1].count(True), count]
        #increase number of connections for each ajoining room
        match direction:
            case "w" | "a" | "d":
                if up_key != []:
                    try:
                        active_rooms[up_key[0]][2] += 1
                    except:
                        temp_rooms[up_key[0]][2] += 1
            case "w" | "a" | "s":
                if left_key != []:
                    try:
                        active_rooms[left_key[0]][2] += 1
                    except:
                        temp_rooms[left_key[0]][2] += 1
            case "a" | "s" | "d":
                try:
                    active_rooms[down_key[0]][2] += 1
                except:
                    temp_rooms[down_key[0]][2] += 1
            case "w" | "s" | "d":
                try:
                    active_rooms[right_key[0]][2] += 1
                except:
                    temp_rooms[right_key[0]][2] += 1
        #increase number of connections for seed room
        active_rooms[room][2] += 1
    #room generation while loop
    while count < limit:
        if len(active_rooms) == 0:
            print("break")
            break
        else:
            for room in active_rooms:
                #get coord of room
                coords = active_rooms[room][0]
                #add rooms for each open doorway
                if rooms[active_rooms[room][1]][1][0]:
                   room_generation("w", False, coords)
                if rooms[active_rooms[room][1]][1][1]:
                    room_generation("a", False, coords)
                if rooms[active_rooms[room][1]][1][2]:
                    room_generation("s", False, coords)
                if rooms[active_rooms[room][1]][1][3]:
                   room_generation("d", False, coords)
        #move any completed active rooms to completed rooms
        rooms_to_pop = []
        for room in active_rooms:
            if active_rooms[room][2] == active_rooms[room][3]:
                completed_rooms[room] = active_rooms[room]
                rooms_to_pop.append(room)
        for room in rooms_to_pop:
            active_rooms.pop(room)
        #move any completed temp rooms to completed rooms, otherwise move to temp rooms
        for room in temp_rooms:
            if temp_rooms[room][2] == temp_rooms[room][3]:
                completed_rooms[room] = temp_rooms[room]
            else:
                active_rooms[room] = temp_rooms[room]
        temp_rooms = {}
        count += 1        
    #complete any remaining rooms
    for room in active_rooms:
        #get coord of room
        coords = active_rooms[room][0]
        #add rooms for each open doorway
        if rooms[active_rooms[room][1]][1][0]:
           room_generation("w", True, coords)
        if rooms[active_rooms[room][1]][1][1]:
            room_generation("a", True, coords)
        if rooms[active_rooms[room][1]][1][2]:
            room_generation("s", True, coords)
        if rooms[active_rooms[room][1]][1][3]:
           room_generation("d", True, coords)
    rooms_to_move = []
    for room in active_rooms:
        rooms_to_move.append(room)
    for room in rooms_to_move:
        completed_rooms[room] = active_rooms.pop(room)
    rooms_to_move = []
    for room in temp_rooms:
        rooms_to_move.append(room)
    for room in rooms_to_move:
        completed_rooms[room] = temp_rooms.pop(room)
    #generate items in rooms
    for room in completed_rooms:
        num_objects = random.randint(0, 5)
        #nothing, wall, chest, danger, chance
        objects = [' ', '#', 'C', 'D', 'X', 'M']
        #orc, goblin, bandit,, elf, knight, wizard, snowman (wizard varient)
        enemies = ['O', 'G', 'B', 'E', 'K', 'W', '⛇']
        object_list = []
        possible_row = [1, 2, 3, 4, 5]
        possible_column = [1, 2, 3, 4, 5]
        for num in range(num_objects):
            #choose location; check if it already exists
            in_list = True
            while in_list == True:
                row = random.choice(possible_row)
                column = random.choice(possible_column)
                #if blocking a door, move skip checing if it is allowed
                if (row, column) in [(3, 1), (1, 3), (5, 3), (3, 5)]:
                    continue
                in_list = any((row, column) in item for item in object_list)
            #choose object
            chosen_object = random.choices(objects, weights = (10, 15, 15, 30, 20, 10), k=1)
            if chosen_object[0] == 'D':
                chosen_object = random.choices(enemies, weights = (35, 30, 30, 25, 35, 20, 15), k=1)
            item = chosen_object[0]
            #add location, object to list
            object_list.append(((row, column), item))
        #add the full objects list to the room
        completed_rooms[room].append(object_list)
    return completed_rooms
    