a = []
thay_ba = [1,3,5,7,9]
n = int(input("Nhập vào số phần tử: "))
for i in range(n):
    b = int(input(f"Nhập vào phần tử {i+1}: "))
    a.append(b)

like_thay_ba = [num for num in a if num % 10 in thay_ba]
print(len(like_thay_ba))
print(" ".join(map(str, like_thay_ba)))