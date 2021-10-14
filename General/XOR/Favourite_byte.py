from pwn import *

message = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

for i in range(0, 255):
    flag = str(xor(message, i))
    if (flag.startswith("b'crypto")):
        print(flag)