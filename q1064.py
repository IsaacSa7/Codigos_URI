s = 0
c = 0
for i in range(1, 7, 1):
    n = float(input())
    if(n > 0):
        s = s + n
        c = c + 1
x = s / c

print("%d valores positivos" %c)
print("%.1f" %x)