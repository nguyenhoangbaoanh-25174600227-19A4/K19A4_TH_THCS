def tron():
    r = float(input("r = "))
    if r <= 0: return print("Sai")
    print("CV =", 2*3.14*r, "DT =", 3.14*r*r)

def vuong():
    a = float(input("a = "))
    if a <= 0: return print("Sai")
    print("CV =", 4*a, "DT =", a*a)

def chu_nhat():
    a = float(input("dài = "))
    b = float(input("rộng = "))
    if a <= 0 or b <= 0: return print("Sai")
    print("CV =", 2*(a+b), "DT =", a*b)

def tam_giac():
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    if a<=0 or b<=0 or c<=0 or a+b<=c or a+c<=b or b+c<=a:
        return print("Không hợp lệ")
    p = (a+b+c)/2
    print("CV =", a+b+c, "DT =", (p*(p-a)*(p-b)*(p-c))**0.5)

while True:
    print("\n1.Tròn 2.Vuông 3.CN 4.TG 0.Thoát")
    chon = input("Chọn: ")
    if chon == "1": tron()
    elif chon == "2": vuong()
    elif chon == "3": chu_nhat()
    elif chon == "4": tam_giac()
    elif chon == "0": break
    else: print("Sai lựa chọn")