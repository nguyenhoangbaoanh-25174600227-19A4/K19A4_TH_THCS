import random
A = []
for i in range(1000):
    A = A + [random.randint(1, 99999)]

A_manual = A[:] # Copy list
for i in range(len(A_manual)):
    for j in range(len(A_manual) - 1):
        if A_manual[j] > A_manual[j+1]:
            A_manual[j], A_manual[j+1] = A_manual[j+1], A_manual[j]