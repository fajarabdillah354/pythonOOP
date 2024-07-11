class Hero:

    def __init__(self, name, health):
        self.__name = name ##UNTUK MEMBUAT ENCAPULATION __nameVar
        self.__health = health

    #getter
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    #setter
    def diserang(self, damageserangan):
        self.__health -= damageserangan

    def setHealth(self, nilaihealthbaru):
        self.__health = nilaihealthbaru
    
karina = Hero("karina",100)
print("Hero sebelum diserang")
print(f"nama hero : {karina.getName()}")
print(f"health hero : {karina.getHealth()}")

karina.diserang(31)
print("Hero setelah diserang")
print(f"health hero setelah diseran : {karina.getHealth()}")