choose = lambda a, b : a if ord(a) > ord(b) else b

a, b = input().split()

print(choose(a, b))
