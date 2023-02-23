
def fib(a, b):
    r = [a, b]
    for i in range(3, 51):
        v = r[i-3]+r[i-2]
        r.append(v)
    return r


c = int(input('Enter first no. :'))
d = int(input('Enter second no. :'))
r = fib(c, d)
print('First 50 Numbers of Fibonacci series is :', end=' ')
print(r)
