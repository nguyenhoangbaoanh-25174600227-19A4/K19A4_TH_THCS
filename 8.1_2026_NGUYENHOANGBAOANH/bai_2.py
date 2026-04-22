def fibonacci():
    print("20 số đầu dãy Fibonacci:")
    a, b = 0, 1
    print(a, end=" ")
    print(b, end=" ")
    for i in range(18):
        a, b = b, a + b
        print(b, end=" ")
    print()

fibonacci()