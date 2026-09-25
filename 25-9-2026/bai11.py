dai, rong, cao, cua_ra_vao, cua_so = map(float, input().split())
dien_tich_4_tuong = 2 * (dai + rong) * cao
dien_tich_can_son = dien_tich_4_tuong - cua_ra_vao - cua_so
print("Diện tích cần sơn:", round(dien_tich_can_son, 2), "m²")