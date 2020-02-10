#!/usr/bin/python3
# coding = utf-8

import subprocess

print('$ nslookup www.python.org')
# 启动一个子进程、并给出输入
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code: ', r)

print("# nslookup")
# 启动一个子进程
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, 
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
# 继续给子进程输入数据
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode("utf-8"))
print(output.decode("gbk"))
print('Exit code:', p.returncode)