#!/usr/bin/python3
# coding = utf-8

import base64
import struct
from collections import namedtuple

bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

# BMP头
_BmpHead_UnpackFmt = '<ccIIIIIIHH'
BmpHead = namedtuple('BmpHead', [
    'os1', 'os2', # 头两个字节：b'BM' = Windows位图、b'BA' = OS/2位图
    'size',       # (uint32_t)位图大小
    'reserved0',  # (uint32_t)始终为0
    'offset',     # (uint32_t)实际图像数据的偏移
    'headerSize', # (uint32_t)Header大小
    'width',      # (uint32_t)位图宽度
    'height',     # (uint32_t)位图高度
    'reserved1',  # (uint16_t)始终为1
    'colors'      # (uint16_t)颜色数
    ])

def bmp_info(data):
    headBytes = struct.unpack(_BmpHead_UnpackFmt, data[0:30])
    headInfo = BmpHead(*headBytes)
    if headInfo.os1 + headInfo.os2 in (b'BM', b'BA') and \
       headInfo.reserved0 == 0                       and \
       headInfo.reserved1 == 1                       :
        return {
            'width' : headInfo.width,
            'height': headInfo.height,
            'colors': headInfo.colors
        }
    else:
        raise TypeError('Bad bmp headstruct!')

if __name__ == "__main__":
    print(bmp_info(bmp_data))
