import os
import time
#clothes shop
items = ['T-shirts','Sweater']
#An Q de sang bai moi
print('An Q de sang bai moi')
while True:
    action = input('Welcome t’o our shop, what do you want (C, R, U, D)?')
    elif action == 'C' or action == 'c':
        items.append(input('New item: '))
        print(items)
    elif action == 'R' or action =='r':
        print(items)
    elif action == 'U' or action =='u':
        p = int(input('Position?'))
        i = input('Item?:')
        del items[p]
        items.insert(p-1,i)
        print(items)
    elif action == 'D' or action =='d':
        del items[int(input('Position? '))-1]
        print(items)
    elif action == 'Q' or action =='q':
        break
    else
        print('we don\'t  offer that, GTFO')

# shepherd
flock = [5, 7, 300, 90, 24, 50, 75]
print('Hello, my name is Khanh and these are my sheep size: ')     #2.1
print(flock)
print('Now my biggest sheep has size', max(flock),' let\'s shear it') #2.2
flock[flock.index(max(flock))] = 8                                                   #2.3
print('After shearing, hear is my flock ')
print(flock)
flock = [x+50 for x in flock]                                                             #2.4 Ng¾n gän, xóc tÝch =))
print('1 month has passed , here is my flock: ')
print(flock)
time.sleep(5)            #Doi 5 giay
os.system('cls')
#2.5: Em gép c¶ 5.5 vµ 5.6 nªn kÕt qu¶ h¬i kh¸c vÝ dô
flock = [5, 7, 300, 90, 24, 50, 75]
print('Hello, my name is Khanh and these are my sheep size: ')    
print(flock)
for _ in range(4):
    print()
    print('Month', _+1)
    flock = [x+50 for x in flock]                                                            
    print('1 month has passed , here is my flock: ')
    print(flock)
    print('Now my biggest sheep has size', max(flock),' let\'s shear it')
    flock[flock.index(max(flock))] = 8                                                   
    print('After shearing, hear is my flock ')
    print(flock)
print('I\'m bored with this')
t = 0
for i in flock:
    t += i
print('My flock has size in total: ',t)
print('So i would get : ',t, ' *2$ = ', t*2 ,'$')
    


