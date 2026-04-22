def P_a(n):
    p = 1
    for i in range(n + 1):
        p *= (2 * i + 1)
    return p
def S_b(n):
    s = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            s += i
        else:
            s -= i
    return s
def S_c(n):
    s = 0
    tong = 0
    for i in range(1, n + 1):
        tong += i      # 1+2+...+i
        s += tong
    return s
def mu(a, b):
    kq = 1
    for _ in range(b):
        kq *= a
    return kq

def P_d(x, y, n):
    tong = 0
    for k in range(1, n + 1):
        tong += (x + 32 * y + mu(y, k))
    return mu(x, y) + tong
n = int(input("Nhập n: "))
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))

print("a) P(n) =", P_a(n))
print("b) S(n) =", S_b(n))
print("c) S(n) =", S_c(n))
print("d) P(x,y) =", P_d(x, y, n))