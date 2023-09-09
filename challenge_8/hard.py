x = int(input("Lütfen bir tam sayı giriniz: "))

temp = x
sum = 0

while temp != 0:
    sum += (temp % 10) ** 3
    temp //= 10 

if x == sum:
    print(f"{x} sayısı bir Armstrong sayısıdır.")

else:
    print(f"{x} sayısı bir Armstrong sayısı değildir.")