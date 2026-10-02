year = int(input("Nhập năm: "))
print("Là năm nhuận: ", (year%400==0 or(year%100!=0 and year%4==0)))