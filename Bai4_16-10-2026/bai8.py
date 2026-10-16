a, b = map(int, input().split())
print(f"Các số nguyên tố trong đoạn [{a}, {b}] là:")

for n in range(a, b + 1):
    if n < 2:
        continue

    la_nguyen_to = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            la_nguyen_to = False
            break
        i += 1

    if la_nguyen_to:
        print(n)
