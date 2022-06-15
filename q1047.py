e = input()
lista = e.split()
hi = int(lista[0])
mi = int(lista[1])
hf = int(lista[2])
mf = int(lista[3])

#processamento
if(hi > hf):
    c = (hi - 24) + hf
elif(hi == hf):
    c = 24
else:
    c = hf - hi

if(mi > mf):
    m = (mi - 60) + mf
elif(mi == mf):
    m = 60
else:
    m = mf - mi

if(m == 60):
    c = c + 1
    m = 0

c = (c * 60) + m
m = c % 60
c = (c - m) / 60

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(c, m))