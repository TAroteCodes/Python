#addition using user defined func

def add(a,b):     #add is called func.   here a & b are 'formal parameters'
    s=a+b
    print('{} + {} = {}'.format(a,b,s))



#main
# main is a calling func.
a=int(input('enter a:'))   #a & b are 'actual parameters'
b=float(input('enter b:'))

add(a,b)  #passing the parameters or arguments
