giay = int(input("Nhap so giay: "))
gio = giay//3600 
giay%=3600
phut = giay//60
giay%=60
print("Giờ: ", gio, " Phút: ", phut, " Giây: ",giay)