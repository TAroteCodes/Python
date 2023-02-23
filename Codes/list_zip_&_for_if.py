CP=[405,499,399,501,999.99]         #List 1
SP=[499,601.50,350,501,1200]        #List 2
BS=zip(CP,SP)                       #zipping both the Lists
print(set(BS))

for a,b in BS:
    if(b>a):                        #to compaire sell price with cost price (SP>CP)
        print("You Made A profit Of {} Rupees.".format(b-a))
    elif (a>b):                     #to compaire sell price with cost price (CP>SP)
        print("You Made A Loss OF {} Rupees".format(a-b))
    else:                           #when both the price is same
        print("You Neither Made Any Profit Nor A Loss.")
