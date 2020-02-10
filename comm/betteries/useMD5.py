#!/usr/bin/python3
# coding = utf-8

import random
import hashlib

def getMD5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, name, password):
        self.name     = name
        self.salt     = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = getMD5(password + self.salt)

db = {
    'michael':User('michael', '123456'),
    'bob':User('bob', 'abc999'),
    'alice':User('alice', 'alice2019')
}

def login(name, password):
    if name not in db:
        raise InterruptedError(name + ' not exist')
    user = db[name]
    # user是一个User实例
    return user.password == getMD5(password + user.salt)

def register(name, password):
    if name in db:
        raise InterruptedError(name + ' has exist')
    user = User(name, password)
    db[name] = user
    return True

if __name__ == "__main__":
    assert login('michael', '123456')
    assert login('bob', 'abc999')
    assert login('alice', 'alice2019')
    assert not login('michael', '1234567')
    assert not login('bob', '123456')
    assert not login('alice', 'alice2009')
    assert register('miky', '123456')
    assert login('miky', '123456')
    assert not login('miky', '1234567')
    print('ok')