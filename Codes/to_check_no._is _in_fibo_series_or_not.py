from math import sqrt


def fib(i):
    c = (5*i*i-4)
    d = (5*i*i+4)
    e = int(sqrt(c))
    f = int(sqrt(d))
    
    if e**2 == c or f**2 == d:
        print('{} this no. is a part of fibonacci series.'.format(i))
    else:
        print('{} this no is not a part of fibonacci series.'.format(i))


a = int(input('Enter a no. to check it is in fibonacci series or not :'))
fib(a)
