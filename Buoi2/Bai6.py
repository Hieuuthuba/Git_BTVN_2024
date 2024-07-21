n = int(input('nhập n ='))
for i in range(1,n+1):
    tong = 0
    for a in range(1,i):
        if i % a == 0:
            tong = tong + a
    if tong == i:
        print(i)

