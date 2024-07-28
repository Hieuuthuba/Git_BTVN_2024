s1 = input('nhập vào s1:')
s2 = input('nhập vào s2:')
print('s1 sau khi đảo ngược là:', s1[::-1])

a = int(input("nhâ a ="))
b = int(input("nhập b ="))
print("chuỗi đảo ngược từ vị trí a đến b là:", s2[:a] + s2[a:b+1][::-1] + s2[b+1:])


print("chuỗi sau khi xóa các phần tử chẵn là:", "".join([s1[i] for i in range(len(s1)) if i %2 != 0]))

length = max(len(s1), len(s2))
print("Chuỗi đan xen các kí tự của s1 và s2: ", "".join([s1[i] + s2[i] if i < len(s1) and i < len(s2) else s1[i:] + s2[i:] for i in range(length)]))


print("Chuỗi đổi chỗ 2 kí tự đầu: ", s2[0] + s1[1:], s1[0] + s2[1:])
