from random import randint

liste = []

for i in range(10):
    liste.append(randint(1,20))

print(liste)

print(f"Listede yer alan en büyük eleman : {max(liste)}")