#entrada de dados
e = input().split()
e.sort()           

A = float(e[2])
B = float(e[1])
C = float(e[0])

#processamento
if(A >= (B + C)):
    print("NAO FORMA TRIANGULO")
else :
    if((A * A) == (B * B) + (C * C)):
        print("TRIANGULO RETANGULO")
    if((A * A) > ((B * B) + (C * C))):
        print("TRIANGULO OBTUSANGULO")
    if((A * A) < (B * B) + (C * C)):
        print("TRIANGULO ACUTANGULO")
    if( A == B and A == C):
        print("TRIANGULO EQUILATERO")
    if(A == B or A == C or B == C):
        print("TRIANGULO ISOSCELES")
