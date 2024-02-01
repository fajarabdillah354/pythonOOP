# inheritance adalah sebuah pewarisan atau penurunan dalam bahasa pemograman, kita bisa mewariskan class ataupun method

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Jungler(Hero):#kita bisa memasukan class Hero sebagai parent dalam parameter yang child sehingga kita bisa mengakses __init__ yang ada di parent
    pass

class Mage(Hero):
    pass

    

alucard = Hero("alu", 200)
print(alucard.__dict__)
print(alucard.name)
haya = Jungler("hayabusa", 250)#class Jungler juga memiliki object __init__ sehingga ktia perlu mengisi parameternya
nana = Mage("nana", 100)
print(nana.__dict__)
print(nana.name)
