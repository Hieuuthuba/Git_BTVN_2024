n = int(input("nhập n ="))
m = int(input("nhập m ="))
print("số mã sinh viên bàn 1 là:")
ban1 = {input() for i in range(n)}
print("số mã sinh viên bần 2 là:")
ban2 = {input() for i in range(m)}
print("mã sinh viên đăng kí ở bàn 1 là:", ban1)
print("mã sinh viên đăng kí ở bàn 2 là", ban2)
print("mã sinh viên đăng kí ở cả 2 bàn là:", ban1&ban2)
print("tổng mã sinh viên đăng kí là:", ban1|ban2)
print("mã sinh viên chỉ đăng kí ở bàn 1 là:", ban1-ban2)
