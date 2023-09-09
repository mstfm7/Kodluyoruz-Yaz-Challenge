x = int(input("Lütfen bir tam sayı giriniz: "))

sum = 0

for i in range(1, x+1):
    
    if x % i == 0:
        sum += i
    
    else:
        continue

print(f"{x} sayısının tam bölenlerinin toplamı : {sum}")
