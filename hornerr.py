import numpy as np
"""
f(x)|   1       -3      -13     15
    |
    |_______________________________
        h(0)    h(1)    h(n)    s(x)
"""

faktor = []
x = [1,-3,-13,15]

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

        arr = np.array(h)
        p = len(faktor1)
        newarr = np.array_split(h,p)

        for i in range(len(newarr)):
            print("hasil bagi :",newarr[i],"\t:",faktor1[i],"(faktor)")
