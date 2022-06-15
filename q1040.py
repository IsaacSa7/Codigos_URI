#entrada
entrada = input()
lista = entrada.split()
n1 = float(lista[0])
n2 = float(lista[1])
n3 = float(lista[2])
n4 = float(lista[3])

#processamento
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 ) / 10
print("Media: %.1f" %media)

if(media >= 7.0):
    print("Aluno aprovado.")
elif(media < 5.0):
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: %.1f" %exame)

    media = (media + exame) / 2
    
    if(media >= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print("Media final: %.1f" %media)
