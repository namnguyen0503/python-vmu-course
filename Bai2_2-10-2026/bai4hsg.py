a, step, b = map(int, input().split())

cuoi = a + (b - 1) * step
tong = b * (a + cuoi) // 2

print("Tong =", tong)