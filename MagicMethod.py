# pada python terdapat beberapa magic method yang memudahkan kita dalam melakukan operasi
# berikut adalah beberapa contoh dari magicMethod dan penerapannya


class Mangga:

    def __init__(self, name, jumlah): # ini adalah contoh dari magic method pertama yaitu method init untuk constructor
        self.name = name
        self.jumlah = jumlah

    def __repr__(self): ## magic ini biasanya digunakan untuk debugging program
        return "{} memiliki jumlah : {}".format(self.name, self.jumlah)

    def __str__(self): ## magic ini biasanya digunakan jika program sudah finish
        return "{} memiliki jumlah : {}".format(self.name, self.jumlah)
    
    def __add__(self, object): ## magic digunakan untuk operasi penjulahan
        return self.jumlah + object.jumlah
    
    @property
    def __dict__(self):
        return "class ini memiliki atribute name dan jumlah"
    


mangga1 = Mangga("indramayu", 10)
mangga2 = Mangga("arummanis", 8)
print(mangga1) ## sebelum menggunakan magic method hasil dari ini sulit kita fahami namun karna ada __repr__
print(mangga1 + mangga2)
print(mangga1.__dict__)
