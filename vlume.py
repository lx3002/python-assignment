def f(x,y):
    return x^2 + y^2

a = 0
b = 1
n = 100


dy = (b - a)/n
dx = (b - a)/n

volume = 0

for i in range(n):
    for j in range(n):
        x = a + i * dx
        y = b + i * dy

volume += f(x,y) * dy * dx

print("the approximated volume is :", volume)


    