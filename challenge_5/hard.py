from math import sqrt

k = int(input("Lütfen bir sayı giriniz : "))

square_root = sqrt(k)

str_square_root = str(square_root)

if len(str_square_root) == 3 :
    print(f"{int(square_root)}")

else:
    print(f"{k} sayısı karekökten tam olarak çıkmıyor.")