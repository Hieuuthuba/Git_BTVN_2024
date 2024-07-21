n = int(input('n ='))
a = 0
b = 1
print(a, end=' ')
print(b, end=' ')
for i in range(0,n - 2):
    s = a + b
    a = b
    b = s
print(s, end=' ')