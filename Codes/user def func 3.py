#retuening value to main func in user defined func


def add(a,b):     #add is called func.   here a & b are 'formal parameters'
    s=a+b
    return (s)     #returning value of 's' to main func 
    


#main
# main is a calling func.
a=int(input('enter a:'))   #a & b are 'actual parameters'
b=float(input('enter b:'))

sum=add(a,b)  #passing the parameters or arguments #sum is catching the returned value.
print(a '+' b = sum)

