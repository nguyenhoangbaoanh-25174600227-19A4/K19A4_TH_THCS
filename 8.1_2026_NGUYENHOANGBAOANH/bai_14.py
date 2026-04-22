def nhap_list(n):
    lst = []
    for i in range(n):
        x = int(input(f"Nhập phần tử {i+1}: "))
        lst.append(x)
    return lst

def binh_phuong_list(lst):
    return list(map(lambda x: x * x, lst))

def main():
    n = int(input("Nhập n: "))
    lst = nhap_list(n)

    print("List ban đầu:", lst)

    lst_bp = binh_phuong_list(lst)
    print("List bình phương:", lst_bp)

main()
