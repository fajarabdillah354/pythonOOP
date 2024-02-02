# saat kita membuat method yang sama dalam inheritance ada method yang memiliki prioritas lebih tinggi

class A:
    def ini_method(self): #nama method yang ada di class A sama dengan class B
        print("INI PUNYA A")

class B:
    def ini_method(self):
        print("INI PUNYA B")

class C(B,A): #karna B lebih dulu di inisiasi dalam param maka method yang akses pertama adala punya class B
    pass
    

Get = C()
Get.ini_method() ## saat kita akses method ini_method() kita ngk tau method di class mana yang terambil
help(Get)