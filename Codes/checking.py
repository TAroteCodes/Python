n=int(input('Enter no.:'))
k=2
while k<=n-1:
        if n%k==0:
            print('{} is not a prime no.'.format(n))
            break
        else:
            print('{}is a prime no.'.format(n))
            break
