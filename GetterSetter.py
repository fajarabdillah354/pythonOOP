class Hero:
    
    def __init__(self, inputName, inputHealth, inputArmor):
        self.name = inputName
        self.__health = inputHealth
        self.__armor = inputArmor
        # self.info = "name : {}  \n\t health : {}".format(self.__name, self.__health)

    @property #dengan property kita bisa menganggap method sebagai variabel
    def info(self):
        return "name : {}  \n\t health : {}".format(self.name, self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print("armor di delete")
        self.__armor = None


bruno = Hero("bruno", 100, 50)
print(bruno.info)# karna dia property maka tidak perlu () untuk memanggilnya

#mengubah nilai name
bruno.name = "lilia"

print(bruno.info)# nilai dari name akan berubah menjadi lilia

print("contoh getter setter armor")
print("ini sebelum ada setter")
print(f"armor : {bruno.armor}")

print("ini setelah memakai setter")
bruno.armor = 20 #kita tidak perlu bruno.armor() cukup memakai = saja nilai akan otomatis masuk ke parameter yang ada di method
print(f"armor : {bruno.armor}")

print("mendelete armor")
del bruno.armor
print(bruno.__dict__) ## maka armor akan bernilai none



