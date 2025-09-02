class Renderer():
    def __init__(self, dungeon, rooms):
        self.base_dungeon = dungeon
        self.rooms_dict = rooms
        self.game_map, self.player_pos = self.convert_dungeon()
        self.player_start_pos = self.player_pos
        self.print_array = [''] *7
        self.player_on = ' '
    def convert_dungeon_small(self):
        print("Rendering Map...")
        rooms = list(self.base_dungeon.values())
        game_map = []
        coords_list = []
        x_values = []
        y_values = []
        for room in rooms:
            #append coords and room_num
            coords_list.append([room[0], room[1]])
            #create lists of x/y values
            x_values.append(room[0][0])
            y_values.append(room[0][1])
        min_x = min(x_values)
        max_x = max(x_values)
        min_y = min(y_values)
        max_y = max(y_values)
        #helper function to add rows to game map
        def add_row_to_map(rooms_dict, row):
            #get variables from above function & define other variables
            nonlocal game_map
            nonlocal min_x
            nonlocal max_x
            nonlocal room_row
            empty_string = '     '
            #create row in game map
            game_map.append('')
            current_x = min_x
            #loop for the length of the number of x values
            for num in range(min_x, max_x+ 1):
                #check if there is a room in the row with the current x coord
                found = False
                for room in row:
                    if room[0][0] == current_x:
                        found = True
                        room_index = row.index(room)
                        break
                #either add the row of the room to game map or empty string
                if found:
                    game_map[-1] += rooms_dict[row[room_index][1]][0][room_row][0]
                else:
                    game_map[-1] += empty_string
                current_x += 1
        #2d list of rooms based on coords
        organised_room_list = []
        for num in range(min_y, max_y + 1):
            #set current y value
            current_y_value = num
            #add new row to organised rooms list
            organised_room_list.append([])
            #set rooms to pop to empty list
            rooms_to_pop = []
            #add any rooms with the right y value to the current row and add them to the rooms to pop list
            for room in coords_list:
                if (room[0][1] == current_y_value):
                    organised_room_list[-1].append(room)
                    rooms_to_pop.append(room)
            #remove already sorted rooms from list 
            for room in rooms_to_pop:
                index = coords_list.index(room)
                coords_list.pop(index )
            #organise row by x value
            organised_room_list[-1].sort(key=lambda sublist: sublist[0][0])
        #reverse the list as sorting puts the bottom at the top but doesn't reverse orientation
        organised_room_list.reverse()
        #get player pos
        found_start_room = False
        for row in organised_room_list:
            for room in row:
                if (0, 0) in room:
                    #have to add offset because the index doesn't account for rooms that dont exist in the row
                    #have to change offset because rooms are 5x5
                    #have to add 7 to offset buffer spaces that are added later
                    player_pos = [(row.index(room) + 3) + 7, (organised_room_list.index(row) + 3) + 7]
                    found_start_room = True
                    break
            if found_start_room == True:
                break
        for row in organised_room_list:
            row_num = min_y + organised_room_list.index(row)
            room_row = 0
            #have to run this code 5 times; one for each row of the room
            for num in range(0, 5):
                room_row = num
                add_row_to_map(self.rooms_dict, row)
        #insert border of emptiness so that there is space around to keep player in centre of the screen
        for num in range(0, 7):
            game_map.insert(0, ' ' * len(game_map[0]))
            game_map.append(' ' * len(game_map[0]))
        #add 7 buffer spaces to each side of the map
        for row in game_map:
            game_map[game_map.index(row)] = '       ' + row + '       '
        return game_map, player_pos
    def convert_dungeon(self):
        print("Rendering Map...")
        rooms = list(self.base_dungeon.values())
        game_map = []
        coords_list = []
        x_values = []
        y_values = []
        for room in rooms:
            #append coords and room_num
            coords_list.append([room[0], room[1], room[-1]])
            #create lists of x/y values
            x_values.append(room[0][0])
            y_values.append(room[0][1])
        min_x = min(x_values)
        max_x = max(x_values)
        min_y = min(y_values)
        max_y = max(y_values)
        #helper function to add rows to game map
        def add_row_to_map(rooms_dict, row):
            #get variables from above function & define other variables
            nonlocal game_map
            nonlocal min_x
            nonlocal max_x
            nonlocal room_row
            empty_string = '       '
            #create row in game map
            game_map.append('')
            current_x = min_x
            #loop for the length of the number of x values
            for num in range(min_x, max_x+ 1):
                #check if there is a room in the row with the current x coord
                found = False
                for room in row:
                    if room[0][0] == current_x:
                        found = True
                        room_index = row.index(room)
                        break
                #either add the row of the room to game map or empty string
                if found:
                    row_string = rooms_dict[row[room_index][1]][0][room_row][0]
                    #check last item in list to figure out if an obstical is required
                    objects = row[room_index][-1]
                    if row[room_index][0] != (0, 0):
                        for item in objects:
                            if item[0][1] == room_row:
                                row_string = row_string[:item[0][0]] + item[1] + row_string[-(6 -item[0][0]):]
                                
                    game_map[-1] += row_string
                else:
                    game_map[-1] += empty_string
                current_x += 1
        #2d list of rooms based on coords
        organised_room_list = []
        for num in range(min_y, max_y + 1):
            #set current y value
            current_y_value = num
            #add new row to organised rooms list
            organised_room_list.append([])
            #set rooms to pop to empty list
            rooms_to_pop = []
            #add any rooms with the right y value to the current row and add them to the rooms to pop list
            for room in coords_list:
                if (room[0][1] == current_y_value):
                    organised_room_list[-1].append(room)
                    rooms_to_pop.append(room)
            #remove already sorted rooms from list 
            for room in rooms_to_pop:
                index = coords_list.index(room)
                coords_list.pop(index )
            #organise row by x value
            organised_room_list[-1].sort(key=lambda sublist: sublist[0][0])
        #reverse the list as sorting puts the bottom at the top but doesn't reverse orientation
        organised_room_list.reverse()
        #get player pos
        for row in organised_room_list:
            for room in row:
                if (0, 0) in room:
                    #have to add offset because the index doent account for rooms that dont exist in the row
                    #have to change offset because rooms are 7x7
                    #have to add 7 to offset buffer spaces that are added later
                    player_pos = [(abs(min_x) * 7) + row.index(room) + 3 + 7, (abs(min_y) * 7) +organised_room_list.index(row) + 3 + 7]
        #add rows to map
        for row in organised_room_list:
            row_num = min_y + organised_room_list.index(row)
            room_row = 0
            #have to run this code 5 times; one for each row of the room
            for num in range(0, 7):
                room_row = num
                add_row_to_map(self.rooms_dict, row)
        #insert border of emptiness so that there is space around to keep player in centre of the screen
        for num in range(0, 7):
            game_map.insert(0, ' ' * len(game_map[0]))
            game_map.append(' ' * len(game_map[0]))
        for row in game_map:
            game_map[game_map.index(row)] = '       ' + row + '       '
        return game_map, player_pos
    def print_game_map(self):
        #make a copy of the game map
        map_to_print = self.game_map.copy()
        #reverse order; the map is upside down from the way it is stored when used during game play
        map_to_print.reverse()
        for row in map_to_print:
            #flip the string- flipping above flips it in the x and y
            print(row)
    def render_game_small(self):
        self.print_array = [''] * 7
        game_map = self.game_map
        #distance visable around player is 7x7
        window_leftx = self.player_pos[0] - 2
        window_topy = self.player_pos[1] - 2
        for num in range(0, 7):
            self.print_array[num] += game_map[window_topy - num][window_leftx:window_leftx + 7]
        #☺
        self.print_array[3] = self.print_array[3][:3] + '0' + self.print_array[3][-3:]
    def render_game(self):
        self.print_array = [''] * 7
        game_map = self.game_map
        #distance visable around player is 7x7
        window_leftx = self.player_pos[0] - 2
        window_topy = self.player_pos[1] - 2
        #error handlign- prevetns game from crashing if you go to high/low
        try:
            for num in range(0, 7):
                #map is flipped if done other way around
                index = 6- num
                self.print_array[index] += game_map[window_topy - index][window_leftx:window_leftx + 7]
            self.print_array[3] = self.print_array[3][:3] + '☺' + self.print_array[3][-3:]
        except:
            self.player_pos = self.player_start_pos
            self.render_game
    def print_window(self):
        for line in self.print_array:
            print(line)
    def move(self, direction):
        game_state = 'dungeon'
        #move & change game state based on what space you are moving to
        #in try/except so that it will not crash if you manage to move out of the 7-wide buffer zone
        try:
            match direction:
                case 'w' | 'W':
                    match self.print_array[2][3]:
                        case ' ':
                            self.player_pos[1] += 1
                        case 'C':
                            self.player_pos[1] += 1
                            game_state = 'chest_worker'
                        case 'O' | 'G' | 'B' | 'E' | 'K' | 'W' | '⛇':
                            game_state = 'battle_worker'
                            self.player_pos[1] += 1
                        case 'X':
                            game_state = 'chance'
                            self.player_pos[1] += 1
                        case 'M':
                            self.player_pos[1] += 1
                            game_state = 'merchant_worker'
                        case _:
                            self.print_window()
                            return game_state
                    self.player_on = self.print_array[2][3]
                case 'a' | 'A':
                    match self.print_array[3][2]:
                        case ' ':
                            self.player_pos[0] -= 1
                        case 'C':
                            self.player_pos[0] -= 1
                            game_state = 'chest_worker'
                        case 'O' | 'G' | 'B' | 'E' | 'K' | 'W' | '⛇':
                            game_state = 'battle_worker'
                            self.player_pos[0] -= 1
                        case 'X':
                            game_state = 'chance'
                            self.player_pos[0] -= 1
                        case 'M':
                            self.player_pos[0] -= 1
                            game_state = 'merchant_worker'
                        case _:
                            self.print_window()
                            return game_state
                    self.player_on = self.print_array[3][2]
                case 's' | 'S':
                    match self.print_array[4][3]:
                        case ' ':
                            self.player_pos[1] -= 1
                        case 'C':
                            self.player_pos[1] -= 1
                            game_state = 'chest_worker'
                        case 'O' | 'G' | 'B' | 'E' | 'K' | 'W' | '⛇':
                            game_state = 'battle_worker'
                            self.player_pos[1] -= 1
                        case 'X':
                            game_state = 'chance'
                            self.player_pos[1] -= 1
                        case 'M':
                            self.player_pos[1] -= 1
                            game_state = 'merchant_worker'
                        case _:
                            self.print_window()
                            return game_state
                    self.player_on = self.print_array[4][3]
                case 'd' | 'D':
                    match self.print_array[3][4]:
                        case ' ':
                            self.player_pos[0] += 1
                        case 'C':
                            self.player_pos[0] += 1
                            game_state = 'chest_worker'
                        case 'O' | 'G' | 'B' | 'E' | 'K' | 'W' | '⛇':
                            game_state = 'battle_worker'
                            self.player_pos[0] += 1
                        case 'X':
                            game_state = 'chance'
                            self.player_pos[0] += 1
                        case 'M':
                            self.player_pos[0] += 1
                            game_state = 'merchant_worker'
                        case _:
                            self.print_window()
                            return game_state
                    self.player_on = self.print_array[3][4]
                case _:
                    self.print_window()
                    return game_state
        except:
            self.player_pos = self.player_start_pos
        self.render_game()
        self.print_window()
        return game_state
    def change_pos(self, pos, icon):
        #function to change a specfic positon in game map
        edited_game_map = self.game_map 
        #player pos is off by 5 on the game map... don't know why
        column = edited_game_map[pos[1] - 5]
        #set icon to new icon
        row = column[:pos[0] + 1] + icon + column[pos[0] + 2:]
        #set row in map
        edited_game_map[pos[1] - 5] = row
        #set row in game map
        self.game_map = edited_game_map
        