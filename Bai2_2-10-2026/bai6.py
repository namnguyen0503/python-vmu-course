a,b,c = map(float, input().split())
print("Là tam giác hợp lệ: ", ((a+b>c) and (a+c>b) and (b+c>a)))