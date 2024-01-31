class Hero:
    #class variabel
    jumlah = 0

    #constructor
    def __init__(self, inputname, inputhealth, inputrole):
        self.name = inputname
        self.health = inputhealth
        self.role = inputrole
        Hero.jumlah += 1
    ## self digunakan untuk mengakses object, ini wajib kita inisiasi jika membuat object

    # berikut beberapa contoh method
    # 1.  yang tidak menggunakan param
        
    def serang(self):
        print(f"hero {self.name} sedang menyerang")
    
    # 2. yang menggunakan param dengan "healup"
    def healing(self, healup):
        self.heal = healup

    # 3. yang menggunakan return value
    def succesHeal(self):
        return self.heal ##mengembalikan dengan nilai instance variabel heal
    
hero1 = Hero("bajo", 500, "fighter") ## membuat object dengan nama hero1
hero2 = Hero("viper", 500, "smoker")

print(hero1.name)
print(hero1.__dict__)

hero1.serang() ## mengakses method serang() yang ada pada class
hero1.healing(250) ## mengakses dan meng inisiasi method healing()
print(hero1.succesHeal()) ## hasil nilai kembalian yang ada pada method succesheal()