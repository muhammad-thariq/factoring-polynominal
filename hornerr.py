"""
f(x)|   x(0)    x(1)    x(2)    x(n)
    |
    |_______________________________
        h(0)    h(1)    h(n)    s(x)
"""
faktor = []

x = [2, -3, -2]
# x = [x(0),x(1),x(2)]

n = x[len(x)-1]
if n >= 0:
    pass
elif n < 0:
    n = n*-1

for i in range(1, n+1):
    if n % i == 0:
        posv = i
        neg = i*-1
        faktor.append(posv)
        faktor.append(neg)

for z in range (len(faktor)):

    faktor1 = []
    faktor1.append(faktor[z])

    h = []
    for n in range(len(faktor1)):
        for i in range(len(x)):
            if i == 0:
                h.append(x[0])
            elif i > 0:
                h.append(h[i-1]*faktor1[n]+x[i])

    print("hasil bagi {} dengan faktor [{}]".format(h,faktor[z]))        
