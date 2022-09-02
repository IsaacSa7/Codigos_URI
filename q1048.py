x = int(input())
s = 0.0
p = 0

if(x <= 400):
    s = x * 1.15
    p = 15
elif(x > 400 and x <= 800):
    s = x * 1.12
    p = 12
elif(x > 800 and x <= 1200):
    s = x * 1.1
    p = 10
elif(x > 1200 and x <= 2000):
    s = x * 1.07
    p = 7
else:
    s = x * 1.04
    p = 4

y = s - x
print("Novo salario: %.2f"%s)
print("Reajuste ganho: %.2f"%(y))
print("Em percentual: "+ str(p) +" %")