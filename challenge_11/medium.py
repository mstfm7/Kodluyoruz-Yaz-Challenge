from random import randint

sum = 0
liste = []

for i in range(10):
    liste.append(randint(1,50))

print(liste)

for x in liste:
    sum += x

print(sum)

print(f"Listedeki sayıların ortalaması : {sum / len(liste)}")