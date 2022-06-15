#entrada
valor = int(input())
x = valor

#processamento
aux = valor % 100
nota100 = (valor - aux)  / 100
valor = aux

aux =  valor % 50
nota50 = (valor - aux) / 50
valor = aux

aux =  valor % 20
nota20 = (valor - aux) / 20
valor = aux

aux =  valor % 10
nota10 = (valor - aux) / 10
valor = aux

aux =  valor % 5
nota5 = (valor - aux)  / 5
valor = aux

aux =  valor % 2
nota2 = (valor - aux) / 2
valor = aux

nota1 = valor

#saida
print("%i "%x)
print("%i nota(s) de R$ 100,00" %nota100)
print("%i nota(s) de R$ 50,00" %nota50)
print("%i nota(s) de R$ 20,00" %nota20)
print("%i nota(s) de R$ 10,00" %nota10)
print("%i nota(s) de R$ 5,00" %nota5)
print("%i nota(s) de R$ 2,00" %nota2)
print("%i nota(s) de R$ 1,00" %nota1)

