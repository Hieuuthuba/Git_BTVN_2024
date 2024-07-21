n = int(input())

for a in range(1,n+1):
    sum_a = 0
    for j in range(1,a):
        if a % j == 0:
            sum_a += j

    b = sum_a

    sum_b =0

    for j in range(1,b):
        if b % j == 0:
            sum_b += j

    if a<b and sum_b == a:
        print(a,b)