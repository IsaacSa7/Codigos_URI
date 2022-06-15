def main():
    valores = input()
    lista = valores.split()

    A, B, C = float(lista[0]), float(lista[1]), float(lista[2])
    pi =  3.14159

    #triangulo
    triangulo = (A * C) / 2
    circulo = pi * (C**2)
    trapezio = ((A + B) * C) / 2
    quadrado = B ** 2
    retangulo = A * B

    #saida de dados
    print("TRIANGULO: %.3f" %triangulo)
    print("CIRCULO: %.3f" %circulo)
    print("TRAPEZIO: %.3f" %trapezio)
    print("QUADRADO: %.3f" %quadrado)
    print("RETANGULO: %.3f" %retangulo)

main()