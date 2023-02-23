# area of circle using user defined func

def area(r):     #add is called func.   here a & b are 'formal parameters'
    a=3.14*r*r
    c=2*3.14*r
    print('Area of circle = {}'.format(a))
    print('circumferance of circle = {}'.format(c))



#main
# main is a calling func.
r=float(input('enter redius:'))   #a & b are 'actual parameters'

area(r)  #passing the parameters or arguments
