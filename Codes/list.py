#heterogeneous=any type of data can store
#can store duplicate values in list
#mutable=editable in same place
#orderd=indexing & negative indexing is present
#define in [ ] brackets
#append= add new values at the end of list

T=[10,20,10,20,'a','A',"Tushar",99.99]           #stored list in variable T

print(type(T))                                   #to check class of T

print(T[6])                                      #gives value store at 6th index

print(T[4:7:1])                                  #slicing=gives value from index 4 to 6

T[7]=[1,2,3,4,5]                                     #replacing 7th index value with new list

print(T)

print(T[7][1])

T.append((91.1,92.2,91.3,91.4,91.5))            #appended tupple with list at last
print(T)                                        #(WE CAN ONLY APPEND 1 VALUE AT A TIME WITH LIST)

T.pop(4)                                        #removing element from 4th index value
T[6].pop(1)                                     #poping value from list of list
print(T)

T.reverse()                                     #reversed whole list
print(T)

T.insert(3,45)                                  #inserted 45 at the 3rd index
T[1].insert(1,2)
print(T)

print(T.__contains__('A'))                      #checking for object is in list or not

print(T.count(10))                              #how many times 10is there in list


T.remove(10)                                    #we are removing 10 from list it will remove only the first '10' from the list and rest will be there
print(T)

s=list(eval(input("Enter list for sorting in assending order:")))  #taking list from user
print(s)
s.sort()                                        #for sorting a list
print(s)

r=list(eval(input("Enter list for sorting in decending order:")))  #taking list from user
print(r)
r.sort(reverse=True)                 #or else we can sort first and then reversed the list
print(r)
r.clear()                            #to clear the whole list it gives empty list