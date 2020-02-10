# doctest模块可以运行注释里面的代码

class Dict(dict):
    # 让doctest提取并运行这些代码
    # 
    # 格式：
    # 运行：
    #         >>> d1 = Dict()
    #         >>> d1['x'] = 100
    #         >>> d1.x
    # 期待的输出：
    #         100
    # 
    # 期待的输出 != 实际运行输出：doctest模块报错
    # 所以、运行ipython useDoctest.py没有任何报错就说明这里的注释代码ok
    # 
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()



# def fact(n):
#     # 正确的doctest注释代码:
#         # '''
#         # Calculate 1*2*...*n

#         # >>> fact(1)
#         # 1
#         # >>> fact(10)
#         # 3628800
#         # >>> fact(-1)
#         # Traceback (most recent call last):
#         #   File "C:\ProgramData\Anaconda3\lib\doctest.py", line 1330, in __run
#         #     compileflags, 1), test.globs)
#         #   File "<doctest __main__.fact[2]>", line 1, in <module>
#         #     fact(-1)
#         #   File "e:\module\2001-python\Qt Designer\comm\abnormal\__init__.py", line 58, in fact
#         #     raise ValueError('n < 1')
#         # ValueError: n < 1
#         # '''
#         # 
#     # 
#     # 错误的doctest注释代码:
#     '''
#     Calculate 1*2*...*n

#     >>> fact(1)
#     1
#     >>> fact(10)
#     ?
#     >>> fact(-1)
#     ?
#     '''
#     # 

#     if n < 1:
#         raise ValueError('n < 1')
#     if n == 1:
#         return 1
#     return n * fact(n - 1)

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
