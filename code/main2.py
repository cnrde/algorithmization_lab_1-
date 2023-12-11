import timeit
import matplotlib.pyplot as plt
import numpy as np


def GCD(a, b):
    gcd = 1
    for i in range(2, max(a, b)):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd


def GCDbest(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return GCDbest(a % b, b)
    else:
        return GCDbest(a, b % a)


def create_graph(b, c, d):
    y_values = np.linspace(0, max(c+d), num=5)
    x_values = np.linspace(b[0], b[-1], num=10)
    plt.plot(b, c)
    plt.plot(b, d)
    plt.title("НОД")
    plt.xlabel("Второе число в функции")
    plt.ylabel("Время работы алгоритма")
    plt.xticks(x_values)
    plt.yticks(y_values)
    plt.show()


a = 560
startnum = 400
endnum = 800
b = []
c = []
d = []
print("GCD:")
for i in range(startnum, endnum):
    b.append(i)
    time = sum(timeit.timeit(lambda: GCD(a, i), number=1)
               for j in range(500))
    k = time/500
    c.append(k)
    print("При i = ", i, "Число =", GCD(a, i), "время = ", k)
print("GCDbest:")
for i in range(startnum, endnum):
    time = sum(timeit.timeit(lambda: GCDbest(a, i), number=1)
               for j in range(500))
    l = time/500
    d.append(l)
    print("При i = ", i, "Число =", GCDbest(a, i), "время = ", l)

create_graph(b, c, d)
