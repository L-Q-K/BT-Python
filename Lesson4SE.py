import os
import time

#1.
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']

inventory['backpack'].sort()
inventory['backpack'].remove('dagger')

inventory['gold'] += 50

print(inventory)

time.sleep(5)
os.system('cls')

#2.
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
    }
purchased_items = {
    "banana": 5,
    "orange": 3,
    }

total = 0

for i in purchased_items:
    print('{0}, quantity : {1}, unit price: {2}'.format(i,purchased_items[i],prices[i]))
    total += purchased_items[i] * prices [i]
    
print(total)

time.sleep(5)

