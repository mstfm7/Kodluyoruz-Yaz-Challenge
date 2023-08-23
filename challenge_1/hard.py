mesafe = int(input("İlk yarışmacı ve ikinci yarışmacı arasındaki mesafeyi giriniz: "))

hız_1 = int(input("İlk yarışmacının hızını giriniz: "))

hız_2 = int(input("İkinci yarışmacının hızını giriniz: "))

while hız_2 < hız_1:
    
    hız_1 = int(input("İlk yarışmacının hızını giriniz: "))
    
    hız_2 = int(input("İkinci yarışmacının hızını giriniz: "))

print(f"İkinci yarışmacı ilk yarışmacıyı {mesafe/(hız_2 - hız_1)} saat sonra yakalar.")