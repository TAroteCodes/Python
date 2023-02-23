#for loop
n=int(input('enter no.:'))
osum=0
esum=0
for n in range(1,n+1,1):
    if n%2==0:
        esum = esum+n
    else:
        osum=osum+n
print('sum of odd no.=',osum)
print('sum of even no.=',esum)
