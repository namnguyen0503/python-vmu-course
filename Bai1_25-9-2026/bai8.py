gia, sl, giam, vat = map(float, input().split())
tien = gia * sl
tien_sau_giam = tien * (1 - giam / 100)
thanh_toan = tien_sau_giam * (1 + vat / 100)
print(round(thanh_toan))