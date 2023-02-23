#exception handling

a=int(input('Enter a no.:'))
b=int(input('Enter b no.:'))

try:
    res=a/b
    print('res= ',res)
    r='ans'+200            #type error

except ZeroDivisionError:       #handling 'zerodivisionerror'  and allow further program to be execute
    print('can not divide by zero.')

except TypeError:            #handling type error and allow further program to be execute
    print('string and int cant be concatenated')


print('Thank You')
