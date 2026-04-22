def luy_thua():
    a = int(input("Nhập số cơ số a: "))
    n = int(input("Nhập số mũ n: "))
    ket_qua = 1
    for i in range(n):
        ket_qua *= a
    print(f"{a}^{n} = {ket_qua}")

luy_thua()