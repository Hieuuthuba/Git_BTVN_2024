n = int(input('nhập n ='))
a = [i for i in range(0,n+1)]
dem = 0
m = int(input('nhập m ='))
for j in a:
    if j == m:
        dem += 1
print(dem)


a[2:8] = [8, 5, 4, 0, 1, 3]
b = a[2:8]
print(a)

print(max(a))
# print(min(a))

y = int(input('nhập y ='))
a.insert(0, y)
print('list sau khi chèn là:',a)
if sorted(a, reverse= False) == a:
   print('tăng')
elif sorted(a, reverse= True) == a:
    print('giảm')
else:
    print('NO')

my_list = [sum(a[0:i + 1]) for i in range(n+1)]
print(my_list)

my_list1 = [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
print(sorted(my_list1))
my_list1 = [abs(i) for i in my_list1]
print(sorted(my_list1))
