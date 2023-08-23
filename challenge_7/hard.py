metin = input("Lütfen Türkçe karakterlerden oluşan bir metin giriniz: ")

sesli_harfler = "aeıioöuü"

temp = 0

for harf in metin:
    if harf.isalpha():
        if harf in sesli_harfler:
            temp += 1

print(f"Girdiğiniz metindeki ünlü harf sayısı : {temp}")