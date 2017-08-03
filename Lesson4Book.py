import os
import time

#20.8.1
alphabet = {}
s = input('String: ' )

for i in s:
    if i.lower() in alphabet:
        alphabet[i.lower()] += 1
    elif  i.upper() in alphabet:
        alphabet[i.upper()] += 1
    else:
        alphabet[i] = 1

print(alphabet)

time.sleep(5)
os.system('cls')

#20.8.2
def add_fruit(inventory, fruit, quantity = 0):
    inventory[fruit] = quantity

def test (state):
    if state == True :
        return True
    else :
        return False
      
# Make these tests work...
new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
print(test("strawberries" in new_inventory))
print(test(new_inventory["strawberries"] == 10))
add_fruit(new_inventory, "strawberries", 25)
print(test(new_inventory["strawberries"] == 35))

time.sleep(5)
os.system('cls')

#20.8.3
f = open ('alicewords.txt', 'r' ,encoding="utf8")
alice = f.read()
f.close()

_alice = {}


s = ''
i = 0
while i < len(alice):
    if  ord(alice[i]) >= 97 and ord(alice[i]) <= 122 or ord(alice[i].lower()) >= 97 and ord(alice[i].lower()) <= 122:  #Kiem tra xem alice[i] co phai chu cai khong qua ma ASCII
        s = s+alice[i]
    else:
        s = s.lower()
        if s in _alice:
            _alice[s] += 1
        else:
            _alice[s] = 1
        s = ''
    i +=1

s = s.lower()
if s in _alice:
    _alice[s] += 1
else:
    _alice[s] = 1

print('The word alice occurs ',_alice['alice'],' times in the book')
      
#convert to list:
__alice = list(_alice.items())
__alice.sort()

#em khong hieu sao cu dung cai file truyen alice la em bi thua cai phan tu '' o dau nen em phai xoa
del __alice[0]

f = open('alice_words.txt','w')
f.write('Word                               Count\n')
f.write('======================\n')
for (u,v) in __alice:
    f.write('{0}                                  {1}\n'.format(u,v))
f.close()
time.sleep(5)
# Em xep hoi lon xon ti a :(        
        


    
