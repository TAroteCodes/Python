# prime no.
ch= 'y'
while ch== 'y':
    n=int(input('Enter no.:'))
    k=2
    while k<=n-1:
        if n%k==0:
            print('{} is not a prime no.'.format(n))
            break
        else:
            k=k+1
    else:
        print('{}is a prime no.'.format(n))

    ch=input('Do you want to continue(y/n):')

    
