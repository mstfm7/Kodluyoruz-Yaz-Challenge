from random import randint

liste1 = []
liste2 = []

for i in range(10):
    liste1.append(randint(1,20))

for i in range(7):
    liste2.append(randint(1,15))

liste1.sort()
liste2.sort()

print(liste1)
print(liste2)

print(f"İlk listenin medyanı : {(liste1[(len(liste1) // 2) - 1] + liste1[(len(liste1) // 2)]) / 2}")
print(f"İkinci listenin medyanı : {liste2[((len(liste2))+1) // 2 - 1]}")