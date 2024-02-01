import tkinter
#ini adalah contoh penerapan OOP yang ada didalam library tkinter

main_window = tkinter.Tk()#membuat object main_window dengan class Tk()


#mengakses class Label dengan object tkinter
label1 = tkinter.Label(main_window, text="hello ini label1")
label2 = tkinter.Label(main_window, text="hello ini label2")
tombol1 = tkinter.Button(main_window, text="tombol1")
tombol2 = tkinter.Button(main_window, text="tombol2")


# menginisiasi posisi
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()


# menanpilkan GUI
main_window.mainloop()

