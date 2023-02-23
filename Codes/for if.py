#Write a Program to accept start value,stop value and step value from user and display all numbers which are divisible by 3 between start and stop values.

s = int(input('enter starting value:'))
t = int(input('\nEnter stopping value:'))
st = int(input('\nEnter Step value:'))

for i in range (s,t+1,st):
    if i%3==0:
        print('\n\n',i,end=' ')
