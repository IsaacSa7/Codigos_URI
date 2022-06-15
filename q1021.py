#entrada
valor = float(input())
valor = valor * 100

#processamento
aux = valor % 10000
nota100 = (valor - aux)  / 10000
valor = aux

aux =  valor % 5000
nota50 = (valor - aux) / 5000
valor = aux

aux =  valor % 2000
nota20 = (valor - aux) / 2000
valor = aux

aux =  valor % 1000
nota10 = (valor - aux) / 1000
valor = aux

aux =  valor % 500
nota5 = (valor - aux)  / 500
valor = aux

aux =  valor % 200
nota2 = (valor - aux)  / 200
valor = aux

aux =  valor % 100
nota1 = (valor - aux) / 100
valor = aux

aux =  valor % 50
notaMoeada0_5 = (valor - aux)  / 50
valor = aux

aux =  valor % 25
notaMoeda0_25 = (valor - aux)  / 25
valor = aux

aux =  valor % 10
notaMoeda0_10 = (valor - aux)  / 10
valor = aux

aux =  valor % 5
notaMoeda0_05 = (valor - aux)  / 5
valor = aux

aux =  valor % 1
notaMoeda0_01 = (valor - aux)  / 1
valor = aux

#saida
print("NOTAS:")
print("%i nota(s) de R$ 100.00" %nota100)
print("%i nota(s) de R$ 50.00" %nota50)
print("%i nota(s) de R$ 20.00" %nota20)
print("%i nota(s) de R$ 10.00" %nota10)
print("%i nota(s) de R$ 5.00" %nota5)
print("%i nota(s) de R$ 2.00" %nota2)
print("MOEDAS:")
print("%i moeda(s) de R$ 1.00" %nota1)
print("%i moeda(s) de R$ 0.50" %notaMoeada0_5)
print("%i moeda(s) de R$ 0.25" %notaMoeda0_25)
print("%i moeda(s) de R$ 0.10" %notaMoeda0_10)
print("%i moeda(s) de R$ 0.05" %notaMoeda0_05)
print("%i moeda(s) de R$ 0.01" %notaMoeda0_01)

