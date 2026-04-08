a = []
while True:
    v = int(input("Nhập số (0 để dừng): "))
    if v == 0: break
    a = a + [v]

# a. 
sub = [1, 2, 3]
a_dau = sub + a
a_cuoi = a + sub
a_5 = a[:4] + sub + a[4:]
print("Chèn vào vị trí 5:", a_5)

# b. 
k = int(input("Nhập vị trí k cần xóa: "))
if 1 <= k <= len(a):
    a = a[:k-1] + a[k:]
print("Sau khi xóa:", a)

# c. 
for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print("Sắp xếp tăng dần:", a)