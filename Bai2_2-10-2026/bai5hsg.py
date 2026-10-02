D, R, K, L = map(int, input().split())

chu_vi = 2 * (D + R)
tong_coc = chu_vi // K
coc_moi_cay = L // K

so_cay = (tong_coc + coc_moi_cay - 1) // coc_moi_cay
print(so_cay)