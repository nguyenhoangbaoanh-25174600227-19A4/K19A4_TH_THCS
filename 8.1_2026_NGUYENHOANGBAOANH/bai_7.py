#a:
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#b: 
def bcnn(a, b):
    return abs(a * b) // ucln(a, b)

#c: 
def rut_gon_phan_so():
    tu = int(input("Nhập tử số: "))
    mau = int(input("Nhập mẫu số: "))
    uc = ucln(tu, mau)
    print(f"Phân số rút gọn: {tu//uc}/{mau//uc}")

#d:
def min_max_n_so():
    n = int(input("Nhập số lượng: "))
    if n <= 0:
        return
    min_val = max_val = int(input())
    for i in range(1, n):
        x = int(input())
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    print(f"Min: {min_val}, Max: {max_val}")

# Test
a, b = map(int, input("Nhập 2 số a b: ").split())
print(f"UCLN({a},{b}) = {ucln(a,b)}")
print(f"BCNN({a},{b}) = {bcnn(a,b)}")
rut_gon_phan_so()
min_max_n_so()