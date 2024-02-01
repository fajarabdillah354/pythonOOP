# override adalah penulisan ulang pada suatu method

class Hero:
    def __init__(self, name, armor):
        self.name = name
        self.armor = armor

    def info(self):
        print("{} memiliki armor {}".format(self.name, self.armor))

class Mage(Hero):
    def __init__(self, name):
        super().__init__(name, 100)

    #override method info yang ada di class parent
    def info(self):
        print("{} adalah role dari MAGE ".format(self.name))

#class support tidak memiliki override method dari class parent
class Support(Hero):
    def __init__(self, name):
        super().__init__(name, 399)

digi = Support("digi")
digi.info()
nova = Mage("nova")
nova.info() #hasil dari method info disini akan mengakses method yang dioverride dalam class Mage

