x = int(input('Enter a number x: '))
a=0
b=1
for i in range(x):
    print(a, end=',')
    a , b = b , a + b