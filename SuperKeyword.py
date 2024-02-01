# dengan keyword super kita dapat mengakses apapun yang ada diclass parent seperti variabel, constructor, hingga method

class Hero:

    def __init__(self,name ,health):
        self.name = name
        self.health = health

    def info(self):
        print("{} mempunyai health : {}".format(self.name, self.health))

class Maksman(Hero):
    def __init__(self, name):
        super().__init__(name, 200)
        super().info()

class Tank(Hero):
    def __init__(self, name):
        super().__init__(name, 500)#keyword super untuk mengakses constructor paret, ini tidak perlu menggunakan self karena sudah ikut self constructor diatasnya
        super().info() #keyword super untuk mengakses method parent

# jadi setiap buat object maka constructor yang ada di class2 lain akan terpanggil dan akan mengakses method info()
hanabi = Maksman("Hanabi")
akai = Tank("Akai")


