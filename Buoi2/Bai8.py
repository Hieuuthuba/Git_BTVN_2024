n = int(input())

pascal = [[1]]


for i in range(n):
    row = [1]
    if i > 0:
        for j in range(1,i):
            row.append(pascal[i-1][j-1] + pascal[i-1][j])
        row.append(1)
        pascal.append(row)

for row in pascal:
    print(" ".join(map(str,row)).center(2*n))