n = int(input("Nhập vào số n = "))

for i in range(1, n+1):
    sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10 # digit = 1 0
        sum += digit ** 3 # 1^ 3 + 7^3 + 3^3
        temp //= 10 # 37 # 3 0
    if i == sum:
        print(i, end = ' ')




