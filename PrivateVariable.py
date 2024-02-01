class Hero:
    jumlah = 0
    #contoh private var dalam class dengan menggunakan double underscore
    __privateJumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        #contoh instance var private
        self.__privateVar = "private" #variabel ini ada cuma hanya bias di akses dalam instance 

        #contoh instance var protected
        self._protecVar = "protected"

kadita = Hero("kadita", 100)
print(Hero.__dict__)
# print(Hero.__privateJumlah) #karna private kita tidak bisa akses sembarang maka akan tampil tidak ada atribut __privateJumlah 
# print(kadita.__privateVar)
# kadita.__privateVar = "ini variable private" #ini akan membuat nilai baru yang ada di variabel private sehingga merusak sifat dari variabel private sendiri


# print(kadita.__privateVar)
print(kadita.__dict__)

#kita masih bisa mengakses variable yang sifatnya protec berbeda dengan private variable
print(kadita._protecVar)
print(kadita.__dict__)
