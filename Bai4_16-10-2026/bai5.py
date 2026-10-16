n = int(input())
check =True
if n<2:
    check=False
elif(n==2):
    check=True
else:
    for i in range(2,n):
        if n%i==0: check=False

if check:
    print("n là số nguyên tố")
else:
    print("n không là số nguyên tố")