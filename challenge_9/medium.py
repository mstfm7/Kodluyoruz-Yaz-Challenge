from random import randint

sum = 0
liste = []

for i in range(20):
    liste.append(randint(0,100))

for sayi in liste:
    
    if sayi % 2 == 0:
        sum += sayi
    
    else:
        continue

print(liste)
print(f"Oluşturulan listedeki çift sayıların toplamı : {sum}")