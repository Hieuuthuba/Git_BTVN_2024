## câu a bài 3
n = int(input('n ='))
sum = 0
for i in range(1,2 * n + 2):
    if i % 2 == 0:
        sum = sum - i
    else:
        sum = sum + i
print("tổng =", sum)

## Câu b bài 3
n = int(input('n ='))
s = 0
for i in range(1,n+1):
    s = s + 1 / i
print(s)

## câu c bài 3
a = int(input('a ='))
b = int(input('b ='))
c = int(input('c ='))
if a == 0 and b == 0:
    print("nhập lại a và b sao cho 2 số khác 0")
else:
    delta = (b * b) - (4 * a * c)
    if delta < 0:
        print("phương trình vô nghiệm")
    elif delta == 0:
        print("phương trình có nghiệm kép x1=x2=", ((-b) / (2 * a)))
    else:
        print("phương trình có 2 nghiệm phân biệt:")
        print("x1 =", ((-b) + delta ** (1 / 2)) / (2 * a))
        print("x2 =", ((-b) - delta ** (1 / 2)) / (2 * a))


