from random import randint

liste = []
hedef_sayi = int(input("Dizide aramak istediğiniz sayıyı giriniz."))

for i in range(10):
    liste.append(randint(1,20))

liste.sort()

print(liste)

if liste.count(hedef_sayi) == 0:
    print("Aradığınız sayı dizide bulunamadı")

else:
    print(f"Aranılan sayı dizide {liste.count(hedef_sayi)} defa tekrar etmiştir.")

