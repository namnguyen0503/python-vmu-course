s1, v1, s2, v2, s3, v3 = map(float, input().split())
tong_quang_duong = s1 + s2 + s3
tong_thoi_gian = s1 / v1 + s2 / v2 + s3 / v3
van_toc_tb = tong_quang_duong / tong_thoi_gian
print("Tổng quãng đường:", round(tong_quang_duong, 2), "km")
print("Tổng thời gian:", round(tong_thoi_gian, 2), "giờ")
print("Vận tốc trung bình:", round(van_toc_tb, 2), "km/h")