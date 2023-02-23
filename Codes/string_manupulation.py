str1="my name is Tushar "         #string declaraation
print(len(str1))                #printing length of string
print(str1[11])                #charactor at 11th index
x=14525
print(str(x))              #converting a from int to string

print(type(x))             #it gives int because strings are immutables(we cant manupulate original one)

print(str1.find('a'))      #give index of first a element

print(str1.upper())        #to convert string in upper case

print(str1.count('m'))     #this is counting how many time a given charactor is repeating in whole string

print(str1.strip())        #removes space from starting and endi ng

print(str1.replace("m","b").upper())          #replacing m with b & converting whole string in upper case in single line

print(str1[3:11:1])                   #slicing:-gives perticular part of the string

print(str1.capitalize())              #make first charactor uppercase and rest will be in lower case

print(str1.split())                   # spliting string as per spaces given in between and showing output as list

print(str1.split("is"))               # spliting from is gives two sets before is and after is

print(str1[::-1])                     #reverse the string