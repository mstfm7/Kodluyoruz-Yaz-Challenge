number_of_animals = int(input("Çiftlikteki toplam tavuk ve koyun sayısını giriniz: "))
number_of_legs = int(input("Çiftlikteki toplam bacak sayısını giriniz: "))

print(f"Çiftlikteki toplam koyun sayısı: {int((number_of_legs- 2 * number_of_animals) / 2)}\nÇiftlikteki toplam tavuk sayısı: {int(number_of_animals - ((number_of_legs - 2 * number_of_animals) / 2))}")