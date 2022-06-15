#dados
lista = [[1, 4.00], [2, 4.50], [3, 5.00], [4, 2.00], [5, 1.50]]

#processamento
entrada = input()
valores = entrada.split()

x = int(valores[0])
y = int(valores[1])

saida = 0.0

for i in range(0,4,1):
    b = lista[i][0]
    if(x == b):
        saida = float(lista[i][1] * y)
        break

print("Total: R$ %.2f" %saida)