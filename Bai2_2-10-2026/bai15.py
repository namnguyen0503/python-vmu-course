giay = int(input("Nhập vào số giây: "))

ngay = giay // 86400
giay %= 86400
gio = giay // 3600
giay %= 3600
phut = giay // 60
giay %= 60

print(f"{ngay}:{gio}:{phut}:{giay}")