metin = input("Lütfen türkçe karakterlerden oluşan bir cümle giriniz: ")

flag = 0

liste = metin.split(" ")

for i in range(len(liste)):
    liste[i] = liste[i].lower()


for i in range(1, len(liste)):
    
    if liste[i-1] == liste[i]:
        flag = 1
        break

    else:
        continue

if flag == 1:
    print("Girdiğiniz cümlede ikileme kullandınız.")

else:
    print("Girdiğiniz cümlede ikileme bulunamadı.")