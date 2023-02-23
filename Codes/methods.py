def add(x,y):                       #use def to create method
    print(x+y)

a=int(input('Enter first no.:'))
b=int(input('Enter Second no.:'))
add(a,b)

#-----------------------------------------------------------
def s(q):                           #s method and q is input
    for p in q:                     #iterating through string
        print(p,end=',')
def j(c):
    print(c+20)

k=str(input('Enter A string :'))    #user string input
s(k)                   #passing string to s
d=int(input('\nEnter no.:'))
j(d)