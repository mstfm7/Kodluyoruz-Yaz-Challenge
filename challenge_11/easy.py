x = int(input("Lütfen faktoriyelini hesaplamak istediğiniz sayıyı giriniz: "))
y = x

carpim = 1

while x > 0:
    carpim *= x
    x -= 1

print(f"{y}! = {carpim}")