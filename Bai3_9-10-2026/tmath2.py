m,n = map(int, input().split())

if(m>n):
    ngay_mot = n
    ngay_ko_mot = (m-n)//2
elif(n>m):
    ngay_mot = m
    ngay_ko_mot = (n-m)//2
else:
    ngay_mot=ngay_ko_mot=m

print(ngay_mot, ngay_ko_mot)