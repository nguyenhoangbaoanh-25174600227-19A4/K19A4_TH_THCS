def la_so_nguyen_to(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def la_so_hoan_hao(n):
    tong = 0
    i = 1
    while i < n:
        if n % i == 0:
            tong += i
        i += 1
    return tong == n


def la_so_doi_xung(n):
    temp = n
    dao = 0
    while temp > 0:
        dao = dao * 10 + temp % 10
        temp //= 10
    return dao == n


# ===== CHƯƠNG TRÌNH CHÍNH =====
n = int(input("Nhập n: "))

# a
if la_so_nguyen_to(n):
    print("Là số nguyên tố")
else:
    print("Không phải số nguyên tố")

# b
if la_so_hoan_hao(n):
    print("Là số hoàn hảo")
else:
    print("Không phải số hoàn hảo")

# c
print("\nCác số đối xứng <= 1000:")
dem = 0
for i in range(1, 1001):
    if la_so_doi_xung(i):
        print(f"{i:5}", end="")
        dem += 1
        if dem % 15 == 0:
            print()