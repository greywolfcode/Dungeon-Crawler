#this file holds the data for all items so other files can access it 
#item rarity data
items = {
        'common': ['Bread', 'Dagger', 'Coin', 'Club'],
        'medium': ['Sword', 'Shield', 'Spear', 'Lance', 'Studded_leather helmet', 'Studded_leather chestplate', 'Studded_leather_leggings', 'Studded_leather boots', 'Gem'],
        'rare': ['Healing', 'Chainmail helmet', 'Chainmail chestplate', 'Chainmail leggings', 'Chainmail boots', 'Scalemail helmet', 'Scalemail chestplate', 'Scalemail leggings', 'Scalemail boots', 'Bow'],
        'super_rare': ['Plate helmet', 'Plate chestplate', 'Plate leggings', 'Plate boots'],
        }
#item states for use in battle file
battle_data = {
            'Dagger': {
                    'attacks': {
                            'slash': {
                                    'defult_damage': 2,
                                    'energy_cost': 1,
                                    'lose_item': False,
                                    #effectivness against different armour types
                                    'effectivness': {
                                            '': 100,
                                            'Studded_leather': 50,
                                            'Chainmail': 30,
                                            'Scalemail': 10,
                                            'Plate': 5,
                                            'head': 45,
                                            'torso': 89,
                                            'legs': 45,
                                            'boots': 0.1,
                                            },
                                    },
                            'stab': {
                                    'defult_damage': 3,
                                    'energy_cost': 2,
                                    'lose_item': False,
                                    #effectivness against different armour types
                                    'effectivness': {
                                            '': 100,
                                            'Studded_leather': 80,
                                            'Chainmail': 60,
                                            'Scalemail': 58,
                                            'Plate': 23,
                                            'head': 55,
                                            'torso': 92,
                                            'legs': 54,
                                            'boots': 1,
                                            },
                                    },
                            },
                    'defences': {
                            'parry': {
                                    #effectivness against different weapon types
                                    'effectivness': {
                                            'Dagger': 85,
                                            'Club': 0,
                                            'Sword': 1,
                                            'Spear': 0,
                                            'Lance': 0,
                                            'Bow': 0,
                                            'Shield': 0.01,
                                            'head': 50,
                                            'torso': 50,
                                            'legs': 20,
                                            'boots': 1,
                                            },
                                    },
                            },
                    },
            'Club': {
                    'attacks': {
                            'smash': {
                                    'defult_damage': 7,
                                    'energy_cost': 5,
                                    'lose_item': False,
                                    #effectivness against different armour types
                                    'effectivness': {
                                            '': 100,
                                            'Studded_leather': 80,
                                            'Chainmail': 75,
                                            'Scalemail': 75,
                                            'Plate': 40,
                                            'head': 55,
                                            'torso': 90,
                                            'legs': 50,
                                            'boots': 5,
                                            },
                                    },
                            'punch': {
                                    'defult_damage': 6,
                                    'energy_cost': 4,
                                    'lose_item': False,
                                    #effectivness against different armour types
                                    'effectivness': {
                                            '': 100,
                                            'Studded_leather': 70,
                                            'Chainmail': 65,
                                            'Scalemail': 65,
                                            'Plate': 30,
                                            'head': 45,
                                            'torso': 50,
                                            'legs': 20,
                                            'boots': 1,
                                            },
                                    },
                            },
                    'defences': {
                        
                            },
                    },
            'Sword': {
                    'attacks': {
                            'slash': {
                                    'defult_damage': 5,
                                    'energy_cost': 3,
                                    'lose_item': False,
                                    #effectivness against different armour types
                                    'effectivness': {
                                            '': 100,
                                            'Studded_leather': 80,
                                            'Chainmail': 75,
                                            'Scalemail': 65,
                                            'Plate': 50,
                                            'head': 50,
                                            'torso': 95,
                                            'legs': 60,
                                            'boots': 15,
                                            },
                                    },
                            'stab': {
                                    'defult_damage': 5,
                                    'energy_cost': 4,
                                    'lose_item': False,
                                    #effectivness against different armour types
                                    'effectivness': {
                                            '': 100,
                                            'Studded_leather': 90,
                                            'Chainmail': 85,
                                            'Scalemail': 65,
                                            'Plate': 60,
                                            'head': 55,
                                            'torso': 98,
                                            'legs': 58,
                                            'boots': 16,
                                            },
                                    },
                            },
                    'defences': {
                            'parry': {
                                    #effectivness against different weapon types
                                    'effectivness': {
                                            'Dagger': 98,
                                            'Club': 34,
                                            'Sword': 85,
                                            'Spear': 1,
                                            'Lance': 1,
                                            'Bow': 0.05,
                                            'Shield': 5,
                                            'head': 60,
                                            'torso': 75,
                                            'legs': 45,
                                            'boots': 12,
                                            },
                                    },
                                },
                    },
            'Spear': {
                    'attacks': {
                            'thrust': {
                                    'defult_damage': 7,
                                    'energy_cost': 6,
                                    'lose_item': False,
                                    #effectivness against different armour types
                                    'effectivness': {
                                            '': 100,
                                            'Studded_leather': 90,
                                            'Chainmail': 85,
                                            'Scalemail': 75,
                                            'Plate': 63,
                                            'head': 60,
                                            'torso': 80,
                                            'legs': 50,
                                            'boots': 2,
                                            },
                                    },
                            'throw': {
                                    'defult_damage': 5,
                                    'energy_cost': 2,
                                    'lose_item': True,
                                    #effectivness against different armour types
                                    'effectivness': {
                                            '': 100,
                                            'Studded_leather': 65,
                                            'Chainmail': 55,
                                            'Scalemail': 50,
                                            'Plate': 30,
                                            'head': 30,
                                            'torso': 50,
                                            'legs': 20,
                                            'boots': 0.01,
                                            },
                                    },
                            },
                    'defences': {
                            'Shaft Parry': {
                                    #effectivness against different weapon types
                                    'effectivness': {
                                            '': 98,
                                            'Club': 32,
                                            'Sword': 21,
                                            'Spear': 0.05,
                                            'Lance': 0.05,
                                            'Bow': 0.005,
                                            'Shield': 1,
                                            'head': 75,
                                            'torso': 21,
                                            'legs': 1,
                                            'boots': 0.001,
                                            },
                                    },
                                },
                    },
            'Lance': {
                    'attacks': {
                            'thrust': {
                                    'defult_damage': 8,
                                    'energy_cost': 6,
                                    'lose_item': False,
                                    #effectivness against different armour types
                                    'effectivness': {
                                            '': 100,
                                            'Studded_leather': 90,
                                            'Chainmail': 85,
                                            'Scalemail': 75,
                                            'Plate': 63,
                                            'head': 60,
                                            'torso': 80,
                                            'legs': 50,
                                            'boots': 2,
                                            },
                                    },
                            },
                    'defences': {
                        
                            },
                    },
            'Bow': {
                    'attacks': {
                            'shoot': {
                                    'defult_damage': 6,
                                    'energy_cost': 4,
                                    'lose_item': False,
                                    #effectivness against different armour types
                                    'effectivness': {
                                            '': 100,
                                            'Studded_leather': 90,
                                            'Chainmail': 85,
                                            'Scalemail': 80,
                                            'Plate': 70,
                                            'head': 80,
                                            'torso': 99,
                                            'legs': 75,
                                            'boots': 60,
                                            },
                                    },
                            },
                    'defences': {
                        
                            },
                    },
            'Claw': {
                    'attacks': {
                            'claw': {
                                    'defult_damage': 3,
                                    'energy_cost': 3,
                                    'lose_item': False,
                                    #effectivness against different armour types
                                    'effectivness': {
                                            '': 100,
                                            'Studded_leather': 80,
                                            'Chainmail': 60,
                                            'Scalemail': 30,
                                            'Plate': 10,
                                            'head': 45,
                                            'torso': 60,
                                            'legs': 43,
                                            'boots': 12,
                                            },
                                    },
                            },
                    'defences': {
                        
                            },
                    },
            'Hand': {
                    'attacks': {
                            'punch': {
                                    'defult_damage': 1,
                                    'energy_cost': 2,
                                    'lose_item': False,
                                    #effectivness against different armour types
                                    'effectivness': {
                                            '': 100,
                                            'Studded_leather': 5,
                                            'Chainmail': 1,
                                            'Scalemail': 0.5,
                                            'Plate': 0,
                                            'head': 45,
                                            'torso': 60,
                                            'legs': 43,
                                            'boots': 12,
                                            },
                                    },
                            },
                    'defences': {
                            'Dodge': {
                                    #effectivness against different weapon types
                                    'effectivness': {
                                            'Dagger': 80,
                                            'Club': 45,
                                            'Sword': 47,
                                            'Spear': 62,
                                            'Lance': 63,
                                            'Bow': 20,
                                            'Shield': 86,
                                            'head': 64,
                                            'torso': 30,
                                            'legs': 65,
                                            'boots': 75,
                                            },
                            },
                    },
                },
            'Shield': {
                    'attacks': {
                            'Sweeping Edge': {
                                    'defult_damage': 2,
                                    'energy_cost': 4,
                                    'lose_item': False,
                                    #effectivness against different armour types
                                    'effectivness': {
                                            '': 100,
                                            'Studded_leather': 50,
                                            'Chainmail': 50,
                                            'Scalemail': 40,
                                            'Plate': 30,
                                            'head': 15,
                                            'torso': 56,
                                            'legs': 20,
                                            'boots': 1,
                                            },
                                    },
                            },
                    'defences': {
                            'block': {
                                    #effectivness against different weapon types
                                    'effectivness': {
                                            'Dagger': 99,
                                            'Club': 89,
                                            'Sword': 87,
                                            'Spear': 80,
                                            'Lance': 80,
                                            'Bow': 87,
                                            'Shield': 90,
                                            'head': 90,
                                            'torso': 92,
                                            'legs': 73,
                                            'boots': 32,
                                            },
                            },
                    },
            },
        }
