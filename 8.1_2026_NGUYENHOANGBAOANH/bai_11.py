def nhap_sv():
    ho_ten = input("Họ tên: ")
    toan = float(input("Điểm Toán: "))
    ly = float(input("Điểm Lý: "))
    hoa = float(input("Điểm Hóa: "))
    return ho_ten, toan, ly, hoa

def tinh_tb(toan, ly, hoa):
    return (toan + ly + hoa) / 3

def xuat_sv(ho_ten, toan, ly, hoa):
    tb = tinh_tb(toan, ly, hoa)
    print(f"Họ tên: {ho_ten}")
    print(f"Điểm: Toán={toan}, Lý={ly}, Hóa={hoa}")
    print(f"Điểm TB: {tb:.2f}")

# Sử dụng
ho_ten, toan, ly, hoa = nhap_sv()
xuat_sv(ho_ten, toan, ly, hoa)