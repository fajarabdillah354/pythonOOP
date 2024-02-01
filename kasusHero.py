class Hero:
    jumlah = 0

    def __init__(self, inputName, health, attack, defend):
        self.name = inputName
        self.menyerang = attack
        self.bertahan = defend
        self.darah = health

    def serang(self,enemy):
        print(self.name + " Menyerang " + enemy.name)
        enemy.diserang(self, self.menyerang)

    def diserang(self, enemy, attackpower_lawan):
        print(self.name +" diserang " + enemy.name )
        seranganDiterima = attackpower_lawan/self.bertahan
        print("serangan yang diterima "+self.name+ " adalah : "+ str(seranganDiterima))
        self.darah -= seranganDiterima
        print("Darah "+self.name+ " tersisa :"+str(self.darah))



hanabi = Hero("Hanabi", 350, 40, 100) 
lesley = Hero("Lesley", 200, 50, 112)
hanabi.serang(lesley)

print("\n")

lesley.serang(hanabi)

