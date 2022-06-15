#entrada
idade = int(input())

aux = idade % 365
ano = int(( idade - aux ) / 365)
idade = aux

aux = (idade % 30)
meses = int((idade - aux) / 30)
idade = aux

dias = int(idade)

print("%i ano(s)" %ano)
print("%i mes(es)" %meses)
print("%i dia(s)" %dias)



