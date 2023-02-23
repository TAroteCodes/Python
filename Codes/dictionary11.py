#dictionary
user = {'un1':'pwd1','un2':'pwd2','un3':'pwd3'}

nu = input('Enter user name:')
if nu in user:
    npd = input('Enter password:')
    if user[nu] == npd:
        print('Login Successfull!')
    else:
        print('Password incorrect')
else:
    print('User name is incorrect')
