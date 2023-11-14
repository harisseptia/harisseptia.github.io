from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('hariswebsite')
root.geometry('500x300')

judul = Label(root,
             text="Login",
             font=('arial',15),
             pady=20)
judul.pack()
image = Image.open("logo.jpg")
logo = ImageTk.PhotoImage(image)

gambar = Label(root, image=logo)
gambar.pack()

frame1 = Frame(root, pady=20)
frame1.pack()

nama = Label(frame1,
             text='username :',background='red').grid(row=0, column=0, padx=(20,10))

field_nama = Entry(frame1,
                   width=30, ).grid(row=0, column=1, padx=(20,10))

password = Label(frame1,
             text='password :',background='blue').grid(row=2, column=0, padx=(20,10))

field_alamat = Entry(frame1,
                   width=30, textvariable = password, show='*').grid(row=2, column=1, padx=(20,10))


loginbutton = Button(frame1,
                   width=10, text='login',background='white').grid(row=5, column=1, padx=(20,10))
root.mainloop()