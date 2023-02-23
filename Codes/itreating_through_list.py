#iterating through list using loop
a=['sourabh','yogi','prashant','ram','anoop','gireesh','aditya']

for x in a:
    print(x)

#list of list

b=[['a','b','c'],['d','e']]
for c in b:
    for d in c:
        print(d)

p=[['india','delhi'],['usa','new jersy'],['canada','vancouver']]
for m,n in p:
    print("My country is " +m+ " and I live in " +n)

Di=dict(p)                           #type casting list to dictionary
print(Di)                            #we cant convert nested list to set but we can convert simple list to set
for j,k in Di.items():               #iterating through converted dictionary using for loop
    print(j,k)

T=tuple(p)                          #list----->tuple
print(T)

