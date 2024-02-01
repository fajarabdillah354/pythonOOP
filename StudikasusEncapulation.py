# pada file kali ini mensimulasikan game dalam menggunakan encapulation

class Hero:

    __jumlah = 0


    def __init__(self, name, health, attackPower, armor):
        self.__nama = name
        self.__darahawal = health
        self.__powerawal = attackPower
        self.__armorawal = armor
        self.__level = 1
        self.__exp = 0


        #ketika hero level up
        self.__darahup = self.__darahawal * self.__level
        self.__powerup = self.__powerawal * self.__level
        self.__armorup = self.__armorawal * self.__level

        self.darahsekarang = self.__darahup 
        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} : \n\tlevel : {} \n\tdarah : {} \n\tpower : {}\n\tarmor : {}".format(self.__nama, self.__level, self.__darahup, self.__powerup, self.__armorup)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, inputExp):
        self.__exp += inputExp
        if(self.__exp >= 100):
            print(self.__nama,"naik level")
            self.__level += 1
            self.__exp -= 100
        
            self.__darahup = self.__darahawal * self.__level
            self.__powerup = self.__powerawal * self.__level
            self.__armorup = self.__armorawal * self.__level

juno = Hero("juno", 100, 40, 50)
print(juno.info)
juno.gainExp = 60
juno.gainExp = 80
print(juno.info)

