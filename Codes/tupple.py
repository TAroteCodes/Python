#it is heterogenious,orderd,imutable
#tupple is declaired in a () brackets
a=(1,2,5,8,'A','B',5,2)       #tupple diclaration
print(a)
print('A'in a)            #to check whether 'A' is in a or not
print(a[3])               #to check perticular index value
#methods in tupple
#count
print(a.count(5))
for i in a:
    print(i,end=' ')
print(type(a))
b=(2,3,5,8)
z=a+b
print(z)
print(b*3)
