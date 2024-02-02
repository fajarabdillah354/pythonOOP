# kita akan mempelajari bagaiamana penerepan decorator lain dalam abstrat class
import abc
from abc import ABC,abstractmethod


class Button(ABC):

    def __init__(self, set_link):
        self.link = set_link

    @abstractmethod
    def click(self):
        pass

    # sekarang kita  juga akan buat agar linknya bisa ada di class PushButton
    @property
    @abstractmethod
    def link(self):
        pass 

# setelah set_link kita buat sebagai atribute dengan decoration @property
# kita harus membuat getter setter untuk method link pada class PushButton

class PushButton(Button):

    def click(self):
         print("go to : {}".format(self.link))

    @Button.link.setter ## kita perlu memberikan decoration super class abstractnya lalu method propertynya
    def link(self, inputLink):
        self.__link = inputLink

    @link.getter
    def link(self):
        return self.__link


tekan = PushButton("WWW.SavannahNote.com")
tekan.click()