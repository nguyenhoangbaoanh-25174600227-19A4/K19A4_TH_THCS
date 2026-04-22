def nhap_nv():
    ho_ten = input("Họ tên: ")
    que_quan = input("Quê quán: ")
    tham_nien = int(input("Thâm niên: "))
    return ho_ten, que_quan, tham_nien

def tinh_luong(tham_nien):
    luong_co_ban = 5000000
    phu_cap = tham_nien * 500000
    return luong_co_ban + phu_cap

def xuat_nv(ho_ten, que_quan, tham_nien, luong):
    print(f"Họ tên: {ho_ten}")
    print(f"Quê quán: {que_quan}")
    print(f"Thâm niên: {tham_nien} năm")
    print(f"Lương: {luong:,.0f} VND")

# Sử dụng
ho_ten, que_quan, tham_nien = nhap_nv()
luong = tinh_luong(tham_nien)
xuat_nv(ho_ten, que_quan, tham_nien, luong)