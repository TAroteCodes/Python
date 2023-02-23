#nested if else
cp=int(input('enter cost price:'))
sp=int(input('enter selling price:'))
if sp>cp:
    print('you are making profit in these deal')
else:
    if cp>sp:
        print('you are making loss in this deal.')
    else:
        print('no profit no loss here.')
