from tkinter import*

root = Tk()
root.title('Grid Tkinter')
root.geometry('500x300')

nama = Label(root,
             text='Nama :').grid(row=0, column=0, padx=(20, 5))

field_nama = Entry(root,
                   width=20).grid(row=0, column=1, padx=(5, 10))

password = Label(root,
               text='Password').grid(row=1, column=0, padx=(20, 5))

field_password = Entry(root, 
                    width=20, textvariabel=password , show='*'). grid(row=1, column=1, padx=(4,5))

btn = Button(root, text='Login').grid(row=2, column=1, padx=(10, 5))


root.mainloop()