# from functools import reduce

# def str2num(s):
#     try:
#         return int(s)
#     except ValueError:
#         try:
#             return float(s)
#         except ValueError:
#             raise

# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     # ns = list(map(str2num, ss))
#     return reduce(lambda acc, x: acc + x, ns)

# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)
#     r = calc('1 + 2.2 + a')
#     print('1 + 2.2 + a =', r)

# main()





# def getValue(va):
#     assert va != 0 , 'input can\'t be 0'
#     return 100 / va

# getValue(10)
# getValue('a')
# 10.0

def fact(n):
# 正确的doctest注释代码:
    # '''
    # Calculate 1*2*...*n

    # >>> fact(1)
    # 1
    # >>> fact(10)
    # 3628800
    # >>> fact(-1)
    # Traceback (most recent call last):
    #     File "C:\ProgramData\Anaconda3\lib\doctest.py", line 1330, in __run
    #     compileflags, 1), test.globs)
    #     File "<doctest __main__.fact[2]>", line 1, in <module>
    #     fact(-1)
    #     File "e:\module\2001-python\Qt Designer\comm\abnormal\__init__.py", line 58, in fact
    #     raise ValueError('n < 1')
    # ValueError: n < 1
    # '''
# 
# 
# 错误的doctest注释代码:
    '''
    Calculate 1*2*...*n
    
    >>> fact(1)
    1
    >>> fact(10)
    ?
    >>> fact(-1)
    ?
    '''
# 
    if n < 1:
        raise ValueError('n < 1')
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()