# types of arguments
# positional argument
# keyword argument
# required argument
# optional argument
def add(a, b, c):                  # a,b,c is a parameters
    d = a+b+c
    return d                     # returning value of d


p = int(input('Enter first no.:'))
q = int(input('Enter second no.:'))
r = int(input('Enter third no.:'))
e = add(p, q, r)                    # p,q,r is a arguments
print(e)                        # printing returned value
