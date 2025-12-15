b=bytes([10,20,30,255,40])
print(type(b))
b[0]=11


ba = bytearray([10,20,30,255,40])
print(type(ba))
ba[0] = 11
for value in ba:
    print(value)