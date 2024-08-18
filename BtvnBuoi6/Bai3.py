import math


def calculate(operation : str, *args):
    if operation == 'add':
        return sum(args)
    elif operation == 'multiply':
        return math.prod(args)
    elif operation == 'max':
        return max(args)
    elif operation == 'min':
        return min(args)
    else:
        return 'nvalid operation'
print(calculate('add',1,2,3,4,5,6,7,8,9,10,11))
#chỗ 'add' có thể thay tùy vào tùy chọn đầu vào