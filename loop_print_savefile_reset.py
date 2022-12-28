# 循环输出打印字符串, 五次后重启
import time

count = 0
while True:
    if (count == 5):
        break
    print('I have a pen.')
    count += 1
    time.sleep(0.5)

f = open('/data.dat', 'wb')
data = bytearray(2048)
f.write(data)
f.close()

import machine;machine.reset()