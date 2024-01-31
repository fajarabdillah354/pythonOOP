class Hewan:
    def __init__(self, namaHewan, jenisHewan, beratHewan):
        self.nama = namaHewan
        self.jenis = jenisHewan
        self.berat = beratHewan


hewan1 = Hewan("Rusa", "Mamalia", 70)
hewan2 = Hewan("Kadal", "Reptil", 2)
hewan3 = Hewan("Katak", "Amfibi", 2)

print(hewan1.__dict__) ## melihat isi dari object hewan1

## kita juga bisa memanggil beberapa field sekaligus dari beberapa object

print(f"{hewan1.nama} adalah nama dari object hewan1")
print(f"{hewan2.jenis} adalah jenis dari object hewan2")
print(f"{hewan3.berat} adalah berat dari object hewan3")


