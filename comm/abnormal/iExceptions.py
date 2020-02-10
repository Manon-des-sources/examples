# 自定义错误class、并使用raise抛出

class NameError(ValueError):
    pass

def getName(name):
    if isinstance(name, str) == False:
        raise NameError('name must be a str')
    return name


print(getName('hello'))
print(getName(1))
