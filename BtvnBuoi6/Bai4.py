so_buoc = 0
def so_n (n : int):
    sum = 0

    def soN (n : int):
        if n < 10:
            return 'nhập lại số lớn hơn 10'
        else:
            return soN(n // 10) + (n % 10)
