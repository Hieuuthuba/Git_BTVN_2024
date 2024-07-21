##Câu a bài 1: tính tổng các chữ số của 1 số nguyên dương
n = int(input('n ='))
S = 0
while n != 0:
    S = S + n%10
    n //= 10
print(S)


##Câu b bài 1: tính tông ước của 1 số n
n = int(input('n ='))
S = 0
if n < 0:
    print("vui lòng nhập lại số nguyên dương")
else:
    for i in range(1, n + 1):
        if n % i == 0:
            S += i
    print(S)

## Câu c bài 1
a = int(input('a ='))
b = int(input('b ='))
c = int(input('c ='))
if a + b > c and b + c > a and a + c > b:
    if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        latamgiac = 'vuông'
    elif a==b and b==c:
        latamgiac = 'đều'
    elif a==b or b==c or a==c:
        latamgiac = 'cân'
    elif a*a+b*b<c*c or a*a+c*c<b*b or b*b+c*c<a*a:
        latamgiac = 'tù'
    else:
        latamgiac = 'Nhọn'
    print('{}, {}, {} là 3 cạnh của tam giác {}'.format(a,b,c,latamgiac))
else:
    print('{}, {}, {} không là 3 cạnh của tam giác'. format(a,b,c))








