#a
c = [i for i in range(1, 101) if i % 2 == 0]
print("Chẵn [1,100]:", c)

# b
from functools import reduce

n = int(input("Nhập n: "))
a = list(range(1, n+1))

# lọc số chẵn
chan = list(filter(lambda x: x % 2 == 0, a))

# tính tổng
tong = reduce(lambda x, y: x + y, chan)

print("Danh sách:", a)
print("Số chẵn:", chan)
print("Tổng số chẵn:", tong)