from tkinter import*

root = Tk()
root.title("DATA DIRI")
root.geometry("800x800")
root.maxsize(800, 500)
root.minsize(100, 100)
root.configure(bg='black')

root['pady'] = 200
root['padx'] = 100

a = Label(root,text="Halo Semuanya !!!")
a.pack()

b = Label(root,text="Perkenalkan namaku Haris Septiawan")
b.pack()

c = Label(root,text="Aku berasal dari Sidoarjo, tepatnya dari Kecamatan Tarik")
c.pack()

d = Label(root,text="Aku suka sekali tidur")
d.pack()

e = Label(root,text="Motto hidupku adalah ya iyu")
e.pack()

f = Label(root,text="~~Sekian, Terimakasih :D ~~")
f.pack()

root.mainloop()

