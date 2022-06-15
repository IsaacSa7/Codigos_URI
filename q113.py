valores = input()
lista = valores.split()
A = int(lista[0])
B = int(lista[1])
C = int(lista[2])

m = (A + B + abs(A - B)) / 2

a = 0
if(m == A):
    a = A
else:
    a = B

m2 = int((a + C + abs(a - C)) / 2)

print("%i eh o maior" %m2)