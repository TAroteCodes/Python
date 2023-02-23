#return values to main in udf


def calci(a,b):     #add is called func.   here a & b are 'formal parameters'
    s = a+b
    d = a-b
    m = a*b
    c = a/b
    return s,d,m,c



#main
# main is a calling func.
a=int(input('enter a:'))   #a & b are 'actual parameters'
b=int(input('enter b:'))

sum,diff,mul,div = calci(a,b)  #passing the parameters or arguments
print('{} + {} = {}'.format(a,b,s))
print('{} - {} = {}'.format(a,b,d))
print('{} * {} = {}'.format(a,b,m))
print('{} / {} = {}'.format(a,b,c))
