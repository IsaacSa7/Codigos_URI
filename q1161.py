#calcula fatorial
def fatorial(n):
    if(n <= 1):
        return 1
    else:
        return n * fatorial(n - 1)

#principal
while(1):
    try:
     M = int(input("")) 
    except:
        break       
    N = int(input(""))

    soma = fatorial(N) + fatorial(M)

    print(soma)