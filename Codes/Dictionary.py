#dictionary
#has key value pair
#enclosed in {} brackets
#unorder,mutable
#dictionary is mapping type data

d={1:'Tushar',2:'gireesh',3:'yogee',4:'vasundhara'}
print(d[1])
d[5]='Sourabh'                                       #adding element to dictionary
print(d)
print(d.get(2))                                      #acess value using get method
print(d.keys())                                      #to get all keys from dictionary
d.pop(2)                                             #poping perticular key value from dictionary
print(d)
print(d.__contains__(5))                             #for checking is 5b present in dictionary or not
print(d.items())
print((d.values()))                                  #gives all values
d[1]='SELF'                                          #modifying value of 1
print(d)
d.update({3:'yogeshwaran',4:'VASUNDHARA'})           #modifying more than 1 value(we can update or add multiple keyvalue in same line of code)
print(d)
d.popitem()                                          #by default it removes last key value
print(d)
d.clear()                                            #remove all elements
print(d)