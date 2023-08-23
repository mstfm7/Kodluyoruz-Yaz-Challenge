kirmizi = int(input("Torbadaki kırmızı top sayısını giriniz : "))
yesil = int(input("Torbadaki kırmızı top sayısını giriniz : "))
mavi = int(input("Torbadaki kırmızı top sayısını giriniz : "))

sum = kirmizi + yesil + mavi

prob_k = (kirmizi / sum) * (kirmizi-1) / (sum-1) 

prob_y = (yesil / sum) * (yesil-1) / (sum-1)

prob_m = (mavi / sum) * (mavi-1) / (sum-1)

print(f"Torbadan çekilen iki topun aynı renkte olma olasılığı : {prob_k + prob_m + prob_y}")