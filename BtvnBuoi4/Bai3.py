n = int(input(" nhập n ="))
m = int(input("nhập m ="))
lst= [input() for i in range(n)]
print("các số yêu thích là:")
seta= {input() for i in range(m)}
print("các số không thích là:")
setb= {input() for i in range(m)}
hp=0
for i in range(n):
    if lst[i] in seta:
        hp += 1
    elif lst[i] in setb:
        hp -= 1
    else: hp=hp
print("muc do hanh phuc la ",hp)