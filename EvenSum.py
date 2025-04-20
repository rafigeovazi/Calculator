def hitung_jumlah_bilangan_genap(angka_maksimal):
    bilangan_genap = [
        bilangan 
        for bilangan in range(1, angka_maksimal + 1) 
        if bilangan % 2 == 0
    ]
    return sum(bilangan_genap)
print(hitung_jumlah_bilangan_genap(10)) 