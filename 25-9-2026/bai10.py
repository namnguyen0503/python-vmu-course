can_nang, chieu_cao = map(float, input().split())
bmi = can_nang / (chieu_cao ** 2)
print("Chỉ số BMI:", round(bmi, 2))