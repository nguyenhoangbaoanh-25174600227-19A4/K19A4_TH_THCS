def nam_nhuan(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

def so_ngay_thang(m, y):
    if m < 1 or m > 12:
        return "Tháng không hợp lệ"

    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    else:  # tháng 2
        if nam_nhuan(y):
            return 29
        else:
            return 28



y = int(input("Nhập năm: "))
m = int(input("Nhập tháng: "))

if nam_nhuan(y):
    print("Năm", y, "là năm nhuận")
else:
    print("Năm", y, "không phải năm nhuận")

print("Số ngày trong tháng:", so_ngay_thang(m, y))