"""
k(0)x^3 + k(1)x^2 + k(2)x^1 + k(n) 
f(x)|   k(0)    k(1)    k(2)    k(n)
    |_______________________________
        h(0)    h(1)    h(n)    s(x)
"""
faktor = []
x = [1,4,1,-6]
# x = [k(0),k(1),k(2),k(n)]
# k(n) != 0
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
    if h[len(h)-1] == 0:
        s = "(faktor)"
    else:
        s = ""
        
    print("hasil bagi {} dengan f(x) [{}] {}".format(h,faktor[z],s))
""" 
stdout
hasil bagi [1, 5, 6, 0] dengan f(x) [1] (faktor)
hasil bagi [1, 3, -2, -4] dengan f(x) [-1] 
hasil bagi [1, 6, 13, 20] dengan f(x) [2]
hasil bagi [1, 2, -3, 0] dengan f(x) [-2] (faktor)
hasil bagi [1, 7, 22, 60] dengan f(x) [3]
hasil bagi [1, 1, -2, 0] dengan f(x) [-3] (faktor)
hasil bagi [1, 10, 61, 360] dengan f(x) [6]
hasil bagi [1, -2, 13, -84] dengan f(x) [-6]
"""
