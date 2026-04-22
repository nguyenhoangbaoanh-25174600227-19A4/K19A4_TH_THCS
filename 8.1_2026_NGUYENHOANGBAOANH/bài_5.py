def in_ascii():
    print("Nhấn ESC để thoát (27)")
    while True:
        ky_tu = input("Nhập ký tự: ")
        if ord(ky_tu) == 27:  # ESC
            break
        print(f"ASCII của '{ky_tu}' = {ord(ky_tu)}")

in_ascii()