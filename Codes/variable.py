
c=10                    #globle variable type 1
def add(a,b):
    x=20                #local variable

    global y            #global variable type 2
    y=15

    print(x)            #accessing local variable
    print(a+b)

def sub(a,b):
    print(a-b)
    print(c)               #accessing globle variable 
    print(y)               #accessing globle variable

def mul(a,b):
    p=5
    def div(a,b):
        print(p)
        c=50
        print(c)  #preference to local variable so ans is 50 not 10
    div(2,3)
mul(2,3)
add(5,5)
sub(5,5)
