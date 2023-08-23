b_price = 80
n_price = 20
p_price = 5

number_of_b = int(input("Aldığınız kitap sayısını giriniz : "))
number_of_n = int(input("Aldığınız defter sayısını giriniz : "))
number_of_p = int(input("Aldığınız kalem sayısını giriniz : "))

print(f"Ödemeniz gereken tutar : {b_price * number_of_b + n_price * number_of_n + p_price * number_of_p}")