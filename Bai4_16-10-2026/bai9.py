n = int(input())
so_goc = n
dao = 0
while n > 0:
    dao = dao * 10 + n % 10
    n = n // 10
if dao == so_goc:
    print("Số là palindrome")
else:
    print("Số không là palindrome")
