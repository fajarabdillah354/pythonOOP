class Hewan:
    # ini adalah variabel class yang bersifat static
    jumlah = 0


    def __init__(self, namaHewan, jenisHewan, beratHewan):
        # ini adalah instance variabel object yang dibuat
        self.nama = namaHewan
        self.jenis = jenisHewan
        self.berat = beratHewan
        Hewan.jumlah += 1 #mengakses variabel class  


hewan1 = Hewan("Rusa", "Mamalia", 70)
print(Hewan.jumlah) # setiap object hewan dibuat maka jumlah bertambah
hewan2 = Hewan("Kadal", "Reptil", 2)
print(Hewan.jumlah)
hewan3 = Hewan("Katak", "Amfibi", 2)
print(Hewan.jumlah)

print(hewan1.__dict__) ## melihat isi dari object hewan1



