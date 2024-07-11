import abc
from abc import ABC,abstractclassmethod

class Agent(ABC):

    @abstractclassmethod
    def menu(self):
        pass

    @abstractclassmethod
    def enemy(self):
        pass

class Duelist(Agent):

    def menu(self):
        print("====== Menu agent duelist ======")

    @staticmethod
    def enemy(self):
        self.enemy_health = 100

    class Jett():
        def __init__(self, name):
            self.name = name
        
        def jett_ability(self, ability1, ability2, ability3, ultimate):
            self.skill1 = ability1
            self.skill12 = ability2
            self.skill3 = ability3
            self.jurus_pamungkas = ultimate
            self.enemy_health = Duelist.enemy()
            self.ultimate_hit = self.enemy_health - self.jurus_pamungkas
            print("sisa health setelah terkena ultimate : {}".format(self.ultimate_hit))
            

    

    


    def add_agent(self, input_agent):
        self.tambah_duelist = input_agent
        print("berhasil menambahkan agent :{}".format(self.tambah_duelist))
        
    def del_agent(self, input_agent):
        self.hapus_agent = input_agent
        if self.hapus_agent == Duelist.add_agent(self, self.tambah_duelist):
            del self.hapus_agent

        print("berhasil menghapus agent : {}".format(self.hapus_agent)) 
         


agent1 = Duelist()
agent1.menu()
agent1.add_agent("jett")
agent1.del_agent("jett")
print(agent1.__dict__)
agent2 = Duelist.Jett("Jett")
print(agent2.name)
agent2.jett_ability("DASH", "UPDRAFE", "SMOKE" ,50)

