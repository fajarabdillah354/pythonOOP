#  saat program kita menggunakan abstract class maka kita harus meng implements semua method yang ada di dalamnya
# di python kita bisa menggunakan abs = abstrack base class
import abc
from abc import ABC,abstractmethod

class Hewan(ABC):#kita gunakan class ABS sebagai superclass untuk membuat abstrack
    @abstractmethod
    def ciri(self):
            print("berikut adalah ciri tiap hewan") 
    

class Ayam(Hewan):
      def ciri(self): ##kita harus meng implements method yang ada di abstrack classnya
            super().ciri() ##kita juga bisa menggunakan super untuk mengakses abstrakMethod yang ada di superClass
            print("ayam berkaki 2")


class Sapi:
      def ciri(self): ## implement method yang ada di class abstrack
            print("sapi berkaki 4")

binatang1 = Ayam()
binatang2 = Sapi()

binatang2.ciri()
binatang1.ciri()