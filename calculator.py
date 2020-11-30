from tkinter import *

root = Tk()
root.minsize(550,700)
root.maxsize(550,700)
root.title('Calculator')

# Defining Them
def one():
	calc.set((calc.get())+'1')
def two():
	calc.set((calc.get())+'2')
def three():
	calc.set((calc.get())+'3')
def four():
	calc.set((calc.get())+'4')
def five():
	calc.set((calc.get())+'5')
def six():
	calc.set((calc.get())+'6')
def seven():
	calc.set((calc.get())+'7')
def eight():
	calc.set((calc.get())+'8')
def nine():
	calc.set((calc.get())+'9')
def ten():
	calc.set((calc.get())+'0')
def add():
	root.title('Addition')
	first.set((calc.get()))
	calc.set('')
	second.set('+')
def sub():
	root.title('Subtraction')
	first.set((calc.get()))
	calc.set('')
	second.set('-')
def mul():
	root.title('Multiplication')
	first.set((calc.get()))
	calc.set('')
	second.set('*')
def equall():
	root.title('Calculator')
	third.set((first.get())+(second.get())+(calc.get()))
	y = eval(third.get())
	calc.set(y)
def div():
	root.title('Division')
	first.set((calc.get()))
	calc.set('')
	second.set('/')
def square():
	gh = eval(calc.get())
	hh = eval(calc.get())
	fh = (gh*hh)
	calc.set(fh)
def cube():
	ghh = eval(calc.get())
	hhh = eval(calc.get())
	hhhh = eval(calc.get())
	ff = (ghh*hhh*hhhh)
	calc.set(ff)
def c():
	calc.set('')

f1 = Frame(borderwidth = 10,bg = "black")
f2 = Frame(borderwidth = 10,bg = "black")
f3 = Frame(borderwidth = 10,bg = "black")
f4 = Frame(borderwidth = 10,bg = "black")
f5 = Frame(borderwidth = 10,bg = "black")
f6 = Frame(borderwidth = 10,bg = "black")

# Creating Entry Widget
calc = StringVar()
first = StringVar()
second = StringVar()
third = StringVar()
Entry(textvariable = calc,width = 90,font = "comicsansms 30 bold",justify = "center").pack()

Button(f1,text = "1",padx = 6,pady = 18,width = 10,font = "comicsansms 20 bold",bg = "black",fg = "white",command = one).pack(side = LEFT)
Button(f1,text = "2",padx = 6,pady = 18,width = 10,font = "comicsansms 20 bold",bg = "black",fg = "white",command = two).pack(side = LEFT)
Button(f1,text = "3",padx = 6,pady = 18,width = 10,font = "comicsansms 20 bold",bg = "black",fg = "white",command = three).pack(side = LEFT)
Button(f2,text = "4",padx = 6,pady = 18,width = 10,font = "comicsansms 20 bold",bg = "black",fg = "white",command = four).pack(side = LEFT)
Button(f2,text = "5",padx = 6,pady = 18,width = 10,font = "comicsansms 20 bold",bg = "black",fg = "white",command = five).pack(side = LEFT)
Button(f2,text = "6",padx = 6,pady = 18,width = 10,font = "comicsansms 20 bold",bg = "black",fg = "white",command = six).pack(side = LEFT)
Button(f3,text = "7",padx = 6,pady = 18,width = 10,font = "comicsansms 20 bold",bg = "black",fg = "white",command = seven).pack(side = LEFT)
Button(f3,text = "8",padx = 6,pady = 18,width = 10,font = "comicsansms 20 bold",bg = "black",fg = "white",command = eight).pack(side = LEFT)
Button(f3,text = "9",padx = 6,pady = 18,width = 10,font = "comicsansms 20 bold",bg = "black",fg = "white",command = nine).pack(side = LEFT)
Button(f4,text = "0",padx = 6,pady = 18,width = 10,font = "comicsansms 20 bold",bg = "black",fg = "white",command = ten).pack(side = LEFT)
Button(f4,text = "+",padx = 6,pady = 18,width = 10,font = "comicsansms 20 bold",bg = "black",fg = "white",command = add).pack(side = LEFT)
Button(f4,text = "-",padx = 6,pady = 18,width = 10,font = "comicsansms 20 bold",bg = "black",fg = "white",command = sub).pack(side = LEFT)
Button(f5,text = "*",padx = 6,pady = 18,width = 10,font = "comicsansms 20 bold",bg = "black",fg = "white",command = mul).pack(side = LEFT)
Button(f5,text = "/",padx = 6,pady = 18,width = 10,font = "comicsansms 20 bold",bg = "black",fg = "white",command = div).pack(side = LEFT)
Button(f5,text = "=",padx = 6,pady = 18,width = 10,font = "comicsansms 20 bold",bg = "black",fg = "white",command = equall).pack(side = LEFT)
Button(f6,text = "^2",padx = 6,pady = 18,width = 10,font = "comicsansms 20 bold",bg = "black",fg = "white",command = square).pack(side = LEFT)
Button(f6,text = "^3",padx = 6,pady = 18,width = 10,font = "comicsansms 20 bold",bg = "black",fg = "white",command = cube).pack(side = LEFT)
Button(f6,text = "Clear All",padx = 6,pady = 18,width = 10,font = "comicsansms 20 bold",bg = "black",fg = "white",command = c).pack(side = LEFT)

f1.pack()
f2.pack()
f3.pack()
f4.pack()
f5.pack()
f6.pack()

root.config(bg = "black")
root.mainloop()
