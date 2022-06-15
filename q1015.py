import math

valorX = input()
valorY = input()

listaX = valorX.split()
listaY = valorY.split()

x1 = float(listaX[0])
y1 = float(listaX[1])
x2 = float(listaY[0])
y2 = float(listaY[1])


distacia = math.sqrt(((x2 - x1)**2 ) + ((y2 - y1)**2))

print("%.4f" %distacia)