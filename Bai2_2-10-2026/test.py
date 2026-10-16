giay_tong = int(input())
ngay = giay_tong // 86400
con_lai = giay_tong % 86400
gio = con_lai //3600
con_lai = con_lai % 3600
phut = con_lai // 60
giay = con_lai % 60
print(ngay,gio,phut,giay, sep":")