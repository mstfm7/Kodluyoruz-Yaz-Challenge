from random import randint

liste = []

for i in range(10):
    liste.append(randint(1,20))

print(liste)

minimum = liste[0]
maximum = liste[0]

for i in liste:
    if(i > maximum):
        maximum = i
    
    if(minimum > i):
        minimum = i

print(f"Listedeki en büyük eleman : {maximum}\nListedeki en küçük eleman : {minimum}")