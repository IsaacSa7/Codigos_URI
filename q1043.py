#entradao
n = input().split()
a = float(n[0])
b = float(n[1])
c = float(n[2])

x = b - c
y = a - c
z = a - b

if(x < 0):
    x = x * -1
if(y < 0):
    y = y * -1
if(z < 0):
    z = z * -1

if(((x < a) and (a < (b + c))) and ((y < b) and (b < (a + c))) and ((z < c) and (c < (a + b)))):
    calculo = a + b + c
    print("Perimetro = %.1f" %calculo)
else:
    calculo = ((a + b) * c) / 2
    print("Area = %.1f" %calculo)