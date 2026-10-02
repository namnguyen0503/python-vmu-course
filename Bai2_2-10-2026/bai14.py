tien = int(input("Nhap so tien: "))
namtram = tien//500 
tien%=500
haitram = tien//200
tien%=200
mottram = tien//100
tien%=100
print("Số tờ 500: ", namtram, "\nSố tờ 200: ", haitram, "\nSố tờ 100: ",mottram)