# kita bisa membuat method static ataupun class static 
# untuk membuat methodstatic kita cukup menggunakan keyword @methodstatic
# sementara untuk class menggunakan @classstatic

class Hero:
    __jumlah = 0 #setiap hero yang kita inisiasi akan menambah jumlah dari Hero
    
    #membuat concstructor
    def __init__(self, name):
        self.name = name
        Hero.__jumlah +=1

    # method ini berlaku untuk object
    def getJumlah(self):
        return Hero.__jumlah
    
    # method ini tidak berlaku untuk object tapi untuk class
    def getJumlah1(): #tidak perlu menggunakan self
        return Hero.__jumlah
    
    # ini adalah contoh dari staticmethod yang nempel pada object dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    # ini adalah contoh dari classmethod yang nempel pada classnya
    @classmethod
    def getJumlah3(iniclass):#dengan ini kita bisa langsung mengakses semua atribute yang ada classnya 
        return iniclass.__jumlah


joy = Hero("joy")
print(joy.getJumlah()) #object joy mengakses method getJumlah()
digi = Hero("digi")
print(Hero.getJumlah1()) 
balmond = Hero("balmond")
print(Hero.getJumlah3())
    
