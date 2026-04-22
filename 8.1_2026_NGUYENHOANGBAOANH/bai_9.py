def cong(a, b): return a + b
def tru(a, b): return a - b
def nhan(a, b): return a * b

def chia(a, b):
    if b == 0:
        print("Không chia được")
        return None
    return a / b

def luy_thua(a, n):
    kq = 1
    for i in range(n):
        kq *= a
    return kq



a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
n = int(input("Nhập n (lũy thừa): "))

print("Cộng:", cong(a, b))
print("Trừ:", tru(a, b))
print("Nhân:", nhan(a, b))

kq_chia = chia(a, b)
if kq_chia != None:
    print("Chia:", kq_chia)

print("Lũy thừa a^n:", luy_thua(a, n))