#entrada
lista = input()
valores = lista.split()
A = int(valores[0])
B = int(valores[1])
C = int(valores[2])
D = int(valores[3])

#processamento
x = C + D
y = A + B

if((B > C) and (D > A) and (x  > y ) and (C > 0) and ( D > 0 ) and (A % 2 == 0)):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")