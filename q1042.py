#entrada
e = input()
n = e.split()

n1 = int(n[0])
n2 = int(n[1])
n3 = int(n[2])

#processamento
primeiro = segundo = terceiro = 0
aux = n1

if(n1 > n2 > n3):
    primeiro , segundo, terceiro = n3, n2, n1
elif(n1 > n3 > n2):
    primeiro , segundo, terceiro = n2, n3, n1
elif(n1 < n2 < n3):
    primeiro , segundo, terceiro = n1, n2, n3
elif(n2 > n1 > n3):
    primeiro , segundo, terceiro = n3, n1, n2
elif(n2 < n1 < n3):
    primeiro , segundo, terceiro = n2, n1, n3
elif(n1 < n3 < n2):
    primeiro , segundo, terceiro = n1, n3, n2

#saida
print(primeiro)
print(segundo)
print(terceiro)
print()
print(n1)
print(n2)
print(n3)


