import timeit
import matplotlib.pyplot as plt
import numpy as np


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonaccibest(n):
    a = [0, 1]
    for i in range(2, n+1):
        a.append(a[i-1]+a[i-2])
    return a[n]


def create_graph(b, c, d):
    y_values = np.linspace(0, max(c+d), num=5)
    plt.plot(b, c)
    plt.plot(b, d)
    plt.title("Фибоначчи")
    plt.xlabel("Номер числа фибоначчи")
    plt.ylabel("Время работы алгоритмов")
    plt.xticks(b)
    plt.yticks(y_values)
    plt.show()


N = 15
b = []
c = []
d = []
print("Фибоначчи через массив")
for i in range(1, N):
    b.append(i)
    time = sum(timeit.timeit(lambda: fibonacci(i), number=1)
               for j in range(10000))
    k = time/10000
    c.append(k)
    print("При i = ", i, "Число =", fibonacci(i), "время = ", k)
print("Фибоначчи")
for i in range(1, N):
    time = sum(timeit.timeit(lambda: fibonaccibest(i), number=1)
               for j in range(10000))
    l = time/10000
    d.append(l)
    print("При i = " + ",", i, "Число = " + ",", fibonaccibest(i), "Время = "+ ",", l)

create_graph(b, c, d)
