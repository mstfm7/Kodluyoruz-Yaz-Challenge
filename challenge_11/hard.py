havuz = 60 # Havuzun büyüklüğü 60x olsun.
ilk_musluk = havuz / 10 # İlk musluk 60x'lik havuzu 10 saatte dolduruyorsa 1 saatte 6x su akıtmaktadır.
ikinci_musluk = havuz / 15 # İkinci musluk 60x'lik havuzu 15 saatte dolduruyorsa 1 saatte 4x su akıtmaktadır.
bosalma_hizi = havuz / 30 # 60x'lik havuz 30 saatte kendiliğinden boşalıyorsa saatte 2x su boşaltmaktadır.

print(f"Havuz toplamda {havuz / (ilk_musluk + ikinci_musluk - bosalma_hizi)} saatte dolar.")