import time
import itertools

def factor(n, x):
    d = 4/x
    if n % 2 == 1:
        return d
    else:
        return -d

def PIn(n):
    natuals = itertools.count(1)
    odd     = filter(lambda x: x % 2 == 1, natuals)
    odd_N   = itertools.takewhile(lambda x: x < n, odd)
    sum_N = 0
    count = 1
    for i in odd_N:
        sum_N += factor(count, i)
        count += 1
        # print(i, sum_N)
    return sum_N

def Pin_2(n):
    odd   = itertools.count(1, 2)
    odd_N = itertools.takewhile(lambda x: x < (2 * n - 1), odd)
    mul   = itertools.cycle([4, -4])
    sum_N = map(lambda x: next(mul) / x, odd_N)
    return sum(sum_N)

from functools import reduce
def Pin_3(n):
    odd   = itertools.count(1, 2)
    odd_N = itertools.takewhile(lambda x: x < (2 * n - 1), odd)
    mul   = itertools.cycle([4, -4])
    div   = map(lambda x: next(mul) / x, odd_N)
    sum_N = reduce(lambda a, b: a + b, div)
    return sum_N

if __name__ == "__main__":
    print(Pin_3(20000))
    print(Pin_2(200000))
    print(PIn(20000))
    print('end')