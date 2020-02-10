#!/usr/bin/python3
# coding = utf-8

# """断点"""

# import os
# currentPath = os.path.abspath('.')
# print(currentPath)

# # 遇到error后忽略
# with open("404.txt", 'r', encoding='utf-8', errors='ingore') as f:
#     print(f.name)
#     for line in f.readlines():
#         print(line.strip())

# from io import StringIO
# # 创建一个StringIO、并写入初始str(可以为空)
# f = StringIO('Hello World!\nNew day!')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())
# print('write')
# f.write('\nanother world')
# # 读取整个StringIO
# print(f.getvalue())
# print('end')

# from io import BytesIO
# # 以一个utf-8的字节流bytes初始化(可以为空)
# f = BytesIO('中文'.encode('utf-8 '))
# print(f.read())
# print(f.write(b'\xe4\xb8'))
# print(f.getvalue())

# e:\Python\comm>cd e:\Python\comm && 
#                   cmd /C "set "PYTHONIOENCODING=UTF-8" && 
#                   set "PYTHONUNBUFFERED=1" && 
#                   C:\ProgramData\Anaconda3\python.exe 
#                       c:\Users\Manon\.vscode\extensions\ms-python.python-2019.1.0\pythonFiles\ptvsd_launcher.py 
#                           --default --client --host localhost --port 52105 
#                           e:\Python\comm\IO\__init__.py "
# e:\Python\comm


# r    以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb   以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
# r+   打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+  以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# w    打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# wb   以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# w+   打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# wb+  以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab   以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# a+   打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# ab+  以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
