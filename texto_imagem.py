from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM
root = Tk()
photo = PhotoImage (file = 'computer.gif').subsample(5)
image = Label (master = root, image = photo)
image.pack(side = TOP)
text = Label (master = root, font = ('Çourier', 18), text = 'Ola alunos da UNIVESP!')
text.pack(side = BOTTOM)
root.mainloop()

