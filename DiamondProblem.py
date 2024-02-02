# berikut adalah contoh kasus diamond problem

class A:
    pass


class B(A):
    def get(self):
        print("ini method class B")


class C(A):
    def get(self):
        print("ini method class C")


class D(C,B):
    pass

obj = D()
obj.get()
help(obj)


# KESIMPULANNYA method yang di get dari object class D tergantung dari Parameter yang kita tulis di dalam class D
# jika parameter yang ditulis duluan adalah B lalu C make method get() yang pertama di cek adalah dari class B
# jika di class B ada method dengan nama get() maka langsung di cetak tapi jika tidak ada maka akan mencari ke class C

