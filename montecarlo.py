from math import sqrt
from random import random
from multiprocessing import Pool
from timeit import timeit

def piMonteCarlo(n):
    """Computes and returns an estimation of pi
    using Monte Carlo simulation.

    Keyword arguments:
    n - The number of samples.
    """

    total = 0

    for i in range(n):
        total += sqrt(1 - random()**2)

    return 4 / n * total

def piParallelMonteCarlo(n, p=4):
    """Computes and returns an estimation of pi
    using a parallel Monte Carlo simulation.

    Keyword arguments:
    n - The total number of samples.
    p - The number of processes to use.
    """

    with Pool(p) as pool:
        ss = [pool.apply_async(piMonteCarlo, (n // p,)) for i in range(p)]
        t = 0
        for s in ss:
            t += s.get()
        return t / p

def generateTable():
    n = 12

    row = []
    row.append('{:<10}'.format('n'))
    row.append('{:<10}'.format('0'))
    row.append('{:<10}'.format('1'))
    row.append('{:<10}'.format('2'))
    row.append('{:<10}'.format('3'))
    row.append('{:<10}'.format('4'))
    print(''.join(row))

    for i in range(21):
        row = []
        row.append('{:<10}'.format(n))
        row.append('{:<10.5f}'.format(piMonteCarlo(n)))
        row.append('{:<10.5f}'.format(piParallelMonteCarlo(n, 1)))
        row.append('{:<10.5f}'.format(piParallelMonteCarlo(n, 2)))
        row.append('{:<10.5f}'.format(piParallelMonteCarlo(n, 3)))
        row.append('{:<10.5f}'.format(piParallelMonteCarlo(n, 4)))
        print(''.join(row))
        n *= 2

def time():
    n = 12

    row = []
    row.append('{:<10}'.format('n'))
    row.append('{:<10}'.format('0'))
    row.append('{:<10}'.format('1'))
    row.append('{:<10}'.format('2'))
    row.append('{:<10}'.format('3'))
    row.append('{:<10}'.format('4'))
    print(''.join(row))

    for i in range(21):
        row = []
        row.append('{:<10}'.format(n))
        row.append('{:<10.5f}'.format(timeit(lambda: piMonteCarlo(n), number=1)))
        row.append('{:<10.5f}'.format(timeit(lambda: piParallelMonteCarlo(n, 1), number=1)))
        row.append('{:<10.5f}'.format(timeit(lambda: piParallelMonteCarlo(n, 2), number=1)))
        row.append('{:<10.5f}'.format(timeit(lambda: piParallelMonteCarlo(n, 3), number=1)))
        row.append('{:<10.5f}'.format(timeit(lambda: piParallelMonteCarlo(n, 4), number=1)))
        print(''.join(row))
        n *= 2
