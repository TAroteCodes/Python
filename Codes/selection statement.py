# selection statement elif
print('MENU')
print('Add 1')
print('sub 2')
print('mul 3')
print('div 4')
print('EXIT 5')
ch=int(input('enter your choice:'))
a=int(input('Enter a:'))
b=int(input('Enter b:'))
if ch==1:
    res=a+b
    print('sum=',res)
elif ch==2:
    res=a-b
    print('sub=',res)
elif ch==3:
    res=a*b
    print('mul=',res)
elif ch==4:
    res=a/b
    print('Div=',res)
elif ch==5:
    print('Exiting...')
    exit(0)
else:
    print('wrong choise')
