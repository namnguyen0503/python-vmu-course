n = int(input())
duong =0
am =0
for i in range(n):
    x = int(input())
    if x > 0: duong+=1
    if x<0: am+=1
print("Số lượng số dương: " , duong)
print("Số lượng số âm:" , am)