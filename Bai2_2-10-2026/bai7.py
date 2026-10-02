sodien = float(input("So dien (kWh): "))

vuot = (sodien - 50 + abs(sodien - 50)) / 2
tong = sodien * 1678 + vuot * (2014 - 1678)
print(f"Gia dien: {tong:.0f} đ")