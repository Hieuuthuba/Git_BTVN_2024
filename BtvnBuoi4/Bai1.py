
x = '123456789'
tup = tuple(x)
print("Tuple đầu tiên:", tup)
lst = ()
for i in tup:
    a = int(i)
    lst += (a,)
print("Tuple sau khi sửa:", lst)
tong = 0
for i in lst:
    tong += i
print(f"Giá trị trung bình của dãy:{tong/len(lst)}")