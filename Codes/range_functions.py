for x in range(11):
    print(x)

#print all odd and even number till 100 using range function (1)
#print table of 23 till 10 using range                        (2)
#print all even and odd using only range not condition satement(3)
#--------------------------------------------------------------------------------------------------
#(1)
print("even no. till 100 is:",end=' ')
for q in range(1,101,1):
    if(q%2==0) :
        print(q,end=' ')

print("\nodd no. till 100 is:",end=' ')
for q in range(1,101,1):
    if(q%2!=0) :
        print(q,end=' ')
print("\n")

#(2)
for p in range(23,231,23):       #table of 23
    print(p,end=' ')
print("\n")

#(3)
for x in range(1,101,2):         #for odd no.
    print(x,end=' ')
print("\n")

for y in range(2,101,2):         #for even no.
    print(y,end=' ')
print("\n")


