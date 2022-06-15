# -*- coding: utf-8 -*-

l = []
for i in range(1,7,1):
    e = float(input())
    l.append(e)

contador = 0

for i in l:
    if(i > 0):
        contador = contador + 1
        
print("%i valores positivos"%contador )