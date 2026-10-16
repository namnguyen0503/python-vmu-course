n = int(input("Nhập n (tìm các số nguyên tố đối xứng từ 2 đến n): "))
print("Các số nguyên tố đối xứng từ 2 đến", n, "là:")
for p in range(2, n + 1):
    la_nt_p = True
    i = 2
    while i * i <= p:
        if p % i == 0:
            la_nt_p = False
            break
        i += 1

    dao = 0
    m = p
    while m > 0:
        dao = dao * 10 + m % 10
        m = m // 10

    if not la_nt_p:
        continue

    la_nt_dao = dao >= 2
    i = 2
    while i * i <= dao:
        if dao % i == 0:
            la_nt_dao = False
            break
        i += 1

    if la_nt_dao:
        print(p)
