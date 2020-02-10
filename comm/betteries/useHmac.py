#!/usr/bin/python3
# coding = utf-8


import hmac
import random

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, name, password):
        self.name = name
        self.key  = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db = {
    'michael':User('michael', '123456'),
    'alice'  :User('alice', 'abc999')
}

def login(name, password):
    if name not in db:
        raise InterruptedError(name + ' not in db')
    user = db[name]
    return user.password == hmac_md5(user.key, password)

if __name__ == "__main__":
    assert login('michael', '123456')
    assert login('alice', 'abc999')
    assert not login('michael', '1234567')
    assert not login('alice', 'Alice2008')
    assert not login('bob', '123456')
    print('ok')