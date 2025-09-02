#import modules
import random
#merchant class
class Merchant():
    def __init__(self, x, y, data):
        self.location = [x, y]
        #list of how much the merchant values each item
        #coins always have the lowest value of 1
        self.values = {
                    '': 0,
                    'Coin': 1,
                    }
        #iterate through the items and set how much the merchant values each item 
        for rarity in  data:
            match rarity:
                case 'common':
                    for item in data[rarity]:
                        if item == 'Coin':
                            continue
                        self.values[item] = random.randint(1, 3)
                case 'medium':
                    for item in data[rarity]:
                        self.values[item] = random.randint(3, 8)
                case 'rare':
                    for item in data[rarity]:
                        self.values[item] = random.randint(9, 14) 
                case 'super_rare':
                    for item in data[rarity]:
                        self.values[item] = random.randint(15, 20)
        #gems can only be gotten from enemies, so they have high value, but have to be added seperatly
        self.values['Gem'] = random.randint(21, 24)
        self.inventory = {}
        num_items = random.randint(12, 24)
        #add items to inventory
        for num in range(1, num_items):
            #get item rarity
            item_rarity = random.choices(['common', 'medium', 'rare', 'super_rare'], k=1, weights = (50, 30, 15, 5))
            item = random.choice(data[item_rarity[0]])
            self.inventory[f'slot_{num}'] = [item, random.randint(1, 10)]
        self.chart = []
    def print_barter_list(self):
        count = 0
        self.chart = []
        #assemble chart of items
        for num in range(1, len(self.inventory)):
            item = self.inventory[f'slot_{num}']
            #add items to chart
            if num % 2 != 0:
                #add new row if even count
                self.chart.append([[item[0] + ': ' + str(item[1]), item[0]]])
            else:
                #add to current row if odd count
                self.chart[-1].append([item[0] + ': ' + str(item[1]), item[0]])
        for row in self.chart:
            row_string = ''
            for item in row:
                row_string = row_string + item[0] + ',  '
            print(row_string)
    def barter(self, offer_parts):
        #split apart the offer parts
        slot = offer_parts[0]
        slot_amount = int(offer_parts[1])
        offer_payment = offer_parts[2]
        offer_payment_amount = int(offer_parts[3])
        #check if merchant has enough of that item
        if self.inventory['slot_' + slot][1] < slot_amount:
            return 'not_enough_of_item_error'
        #get item in slot
        slot_value = self.values[self.inventory['slot_' + slot][0]] * slot_amount
        payment_value = self.values[offer_payment] * offer_payment_amount
        #make trade if value of slot is less than value of offer
        if slot_value <= payment_value:
            return True
        #otherwise make a counter offer
        else:
            payment_type = random.choice(['item', 'coins'])
            if payment_type == 'item':
                #offer different amount of same item
                self.counter_offer = str(round((slot_value + 1) / self.values[offer_payment])) + ' ' + offer_payment
            elif payment_type == 'coins':
                self.counter_offer = str(slot_value) + ' coins'
            return False
