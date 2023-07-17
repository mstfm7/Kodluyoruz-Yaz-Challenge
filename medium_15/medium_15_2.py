char_dictionary = {}  # Kullanıcının gireceği metindeki karakterleri kaydetmek üzere boş bir dictionary oluşturuyoruz. 

metin = input("Lütfen Türkçe karakterlerden oluşan bir metin giriniz: ")

for i in range(len(metin)):
    
    if metin[i].isalpha(): # Girilen metindeki karakterlerin alfabetik olup olmadığını kontrol ediyoruz.
        
        if metin[i] not in char_dictionary: # Bu aşamada karakterin dictionary içinde önceden var olup olmadığını kontrol ediyoruz. Eğer karakter halihazırda dictionary 
                                            # içinde yoksa karakteri dictionary içine ekliyoruz.
            char_dictionary[metin[i]] = 0
        
        char_dictionary[metin[i]] += 1  # Karakter dictionary içinde önceden var ise değerini 1 arttırıyoruz.

freq = sorted(char_dictionary.values()) # "value" değeri en büyük olandan en küçük olana doğru dictionary içindeki elemanları sıralayarak en çok tekrar eden karakterin
                                        # "value" değerini most_repeated adlı değişkene atıyoruz.

most_repeated = freq[-1]

print("Metinde en çok tekrar edilen karakter(ler): \n")

for key, value in char_dictionary.items(): # Son olarak dictionary içinde "value" değeri en büyük olan karakter ya da karakterleri ekrana bastırıyoruz.
    if value == most_repeated:
        print(f"{key} : {value} \n")  

   