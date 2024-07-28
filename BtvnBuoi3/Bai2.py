k = int(input('nhập vào số phần tử:'))
a = []
for i in range(k):
    a.append(int(input(f'nhập vào phần tử thứ {i +1}:')))
n = int(input('n ='))
m = int(input('m ='))
if m*n > k:
    print("NO")
else:
    matrix = []
    index = 0
    for i in range(n):
        row = []
        for j in range(m):
            row.append((a[index]))
            index +=1
        matrix.append(row)
print(matrix)


