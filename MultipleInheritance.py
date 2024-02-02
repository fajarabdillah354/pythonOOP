# pada bahasa python kita bisa melakukan multiple inheritance dimana turunan dari sebuah class 
# dapat mengakses 2 superclass sekaligus, contoh dibawah ini

class A:
    def ini_methodA(self):
        print("ini method punya A")
class B:
    def ini_methodB(self):
        print("ini method punya B")
class C(A,B): ## kita jadikan class A,B sebagai super class dari class C
    def __init__(self, name, age):
        self.name = name
        self.age = age

Sesuatu = C("fajar", 21)
print(Sesuatu.__dict__)
Sesuatu.ini_methodA() ## ini mengambil dari method class A
Sesuatu.ini_methodB() ## ini mengambil dari method class B