
a = int(input('nhap a : '))
dem = 0
while a != 0 :
    a //= 2
    dem += 1
print ('cần:',dem,'bits')

# #3 cách in ra "python is awesome"
x = "awesome"
print("python is", x)
print("python is", format(x))
print(f'python is {x}')

# #kiểm tra version
import sys
print(sys.version)