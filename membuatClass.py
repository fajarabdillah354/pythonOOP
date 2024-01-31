class MobileLegend: ## membuat class dengan nama Mobile Legend
    pass

hero1 = MobileLegend() ## membuat object dengan class Mobile Legend
hero2 = MobileLegend()
hero3 = MobileLegend()

hero1.name = "Layla" ## membuat field pada object yang telah dibuat
hero1.role = "Maksman"
hero1.health = 800

hero2.name = "Balmon"
hero2.role = "Fighter"
hero2.health = 1200

hero3.name = "Joy"
hero3.role = "Jungler"
hero3.health = 1000

print(hero1.__dict__)
print(hero1)

print(hero2.__dict__)
print(hero2)

print(hero3.__dict__)
print(hero3)





