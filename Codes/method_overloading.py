#one parameter find squre 
#two parameter add
#three-multiply
#four-find perfect square
from math import sqrt
from multipledispatch import dispatch

@dispatch(int)
def act(a):
    print(a**2)

@dispatch(int,int)
def act(a,b):
    print(a+b)

@dispatch(int,int,int)
def act(a,b,c):
    print(a*b*c)

@dispatch(int,int,int,int)
def act(a,b,c,d):
    e=a*b*c*d
    f=int(sqrt(e))
    if f**2==e:
        print(e,'is a perfect square\n')
    else:
        print(e,' is not a perfect squre')
                
act(10)
act(10,20)
act(10,20,30)
act(1,3,3,3)
