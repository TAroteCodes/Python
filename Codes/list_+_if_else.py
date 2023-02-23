#find the smallest and largest number in the list using if else and for loop

a=[200,501,300,99.99,400]
a.sort()
print('smallest value in the list is:{}'.format(a[0]))
print("Largest value in the list is: {}".format(a[4]))
#----------------------------------------------------------

b=[11,5,25]

if b[0]>b[1] and b[0]>b[2]:
    print("\nlargest number in the llist is:{}".format(b[0]))
elif b[1]>b[0] and b[1]>b[2]:
    print("\nlargest number in the llist is:{}".format(b[1]))
elif b[2]>b[0] and b[2]>b[1]:
    print("\nlargest number in the llist is:{}".format(b[2]))

if b[0]<b[1] and b[0]<b[2]:
    print("Smallest number in the list is:{}".format(b[0]))
elif b[1]<b[0] and b[1]<b[2]:
    print("Smallest number in the list is:{}".format(b[1]))
elif b[2]<b[0] and b[2]<b[1]:
    print("Smallest number in the list is:{}".format(b[2]))

#------------------------------------------------------------------------------

c=[51,75,48,65,85,47,64,55.8,20.14,15.15]
max=c[0]
for i in c:
    if i>=max:
        max=i
print("\nLargest number in the list is:{}".format(max))
min=c[0]
for i in c:
    if i<min:
        min=i
print("Smallest number in the list is:{}".format(min))




