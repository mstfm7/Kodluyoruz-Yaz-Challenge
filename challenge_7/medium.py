sayi = int(input('Lütfen bir doğal sayı giriniz : '))

sum = 0

x = sayi

while sayi != 0:
    sum += int(sayi % 10)
    sayi /= 10

print(f"{x} sayısının rakamları toplamı: {sum}")