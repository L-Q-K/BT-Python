#Write a program that asks user their height (cm) and weight (kg), and then calculate their BMI (Body Mass Index):
import os
import time
print('Moi bai cach nhau khoang 10s')
h = int(input('Nhap chieu cao (cm nha): '))
w =int(input('Bao nhiau can (kg)? : '))
bmi = w/(h/100)**2
if bmi<16:
    print('Qua gay')
elif bmi <18.55:
    print('Hoi gay')
elif bmi<25 :
    print('Body chuan')
elif bmi<30:
    print('Beo roi ®ay')
else:
    print('Beo PHI')
time.sleep(10)
#Study how to print without moving to a new line:
os.system('cls')
print('Hello',end=' ')
print(', my name',end=' ')
print('is B-max')
time.sleep(10)
os.system('cls')
#Print out the following patterns, remember that the number of columns and rows can be changed later, so try to write programs that scale
print('Em lam bai tong quat luon a! ')
print('In sao voi so hang , cot tuy y :')
c = int(input('So cot: '))
r = int(input('So hang: '))
for i in range(r):
    for j in range(c):
        print('*',end=' ')
    print()
time.sleep(10)
os.system('cls')
print('In stars and xs voi so hang , cot tuy y :')
c = int(input('So cot: '))
r = int(input('So hang: '))
for i in range(r):
    for j in range(c):
        if i%2==0:
            print('x*',end=' ')
        else:
            print('*x',end=' ')
    print()
time.sleep(10)
os.system('cls')
#Write a piece of code that uses nested conditionals
x=10
y=9
if x>y:
    if x<11:
        print('Nice')
    else:
        print('Bad')
else:
    print('Nope')









    
