a = 10
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)
if a == b:
    print('yes')
elif a > b:
    print('a lớn hơn b')
else:
    print('a nhỏ hơn b')

print(a&b)
print(a|b)
print(a^b)
print(~a==b)
print(~a) #phủ định của n = -(n+1)
print(a<<1) #dịch trái a đi n bit thì kết quả sau khi dịch là a*(2**n)
print(a>>1) #dịch phải a đi n bit thì ngược lại với dịch trái sẽ là chia 2**n