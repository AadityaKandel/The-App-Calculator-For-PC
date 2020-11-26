from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title('Calculator')
root.geometry('600x640')
root.maxsize(600,640)
root.minsize(600,640)

# Giving Global Variable
qqq = 999999999999999999999999999

# Deining THem
def error():
	tmsg.showinfo('Warning',"0 Mustn't Be First")
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
def zero():
	calc.set((calc.get())+'0')
def addition():
	calc.set((calc.get())+'+')
def subtract():
	calc.set((calc.get())+'-')
def division():
	calc.set((calc.get())+'/')
def equal():
	if ((calc.get()) == str(qqq)):
		calc.set('Maximum Number Reached..')
	else:
		try:
			a = eval((calc.get()))
			calc.set(a)
		except:
			tmsg.showinfo('Warning',"0 Mustn't Be First\n\n              OR\n\n Number Error Occured")
def clear():
	calc.set('')
def c():
	try:
		a = eval((calc.get()))
		b = eval((calc.get()))
		c = a*b
		calc.set(c)
	except:
		error()
def cc():
	try:
		a = eval((calc.get()))
		b = eval((calc.get()))
		c = eval((calc.get()))
		c = a*b*c
		calc.set(c)
	except:
		error()
def multiplication():
	calc.set((calc.get())+'*')


# Making The ENtry Widget
calc = StringVar()

# Making Frames
f1 = Frame(borderwidth = 10, bg = 'black')
f2 = Frame(borderwidth = 10, bg = 'black')
f3 = Frame(borderwidth = 10, bg = 'black')
f4 = Frame(borderwidth = 10, bg = 'black')
f5 = Frame(borderwidth = 10, bg = 'black')
f6 = Frame(borderwidth = 10, bg = 'black')

Entry(textvariable = calc,font = "comicsansms 30 bold",width = 100,justify = 'center',fg = "black",bg = "white").pack()

Button(f1,text = "1",pady = 19,width = 6,fg = "white",bg = "black",command = one,font = "comicsansms 16 bold").pack(side = LEFT)
Button(f1,text = "2",pady = 19,width = 6,fg = "white",bg = "black",command = two,font = "comicsansms 16 bold").pack(side = LEFT)
Button(f1,text = "3",pady = 19,width = 6,fg = "white",bg = "black",command = three,font = "comicsansms 16 bold").pack(side = LEFT)
Button(f2,text = "4",pady = 19,width = 6,fg = "white",bg = "black",command = four,font = "comicsansms 16 bold").pack(side = LEFT)
Button(f2,text = "5",pady = 19,width = 6,fg = "white",bg = "black",command = five,font = "comicsansms 16 bold").pack(side = LEFT)
Button(f2,text = "6",pady = 19,width = 6,fg = "white",bg = "black",command = six,font = "comicsansms 16 bold").pack(side = LEFT)
Button(f3,text = "7",pady = 19,width = 6,fg = "white",bg = "black",command = seven,font = "comicsansms 16 bold").pack(side = LEFT)
Button(f3,text = "8",pady = 19,width = 6,fg = "white",bg = "black",command = eight,font = "comicsansms 16 bold").pack(side = LEFT)
Button(f3,text = "9",pady = 19,width = 6,fg = "white",bg = "black",command = nine,font = "comicsansms 16 bold").pack(side = LEFT)
Button(f4,text = "0",pady = 19,width = 6,fg = "white",bg = "black",command = zero,font = "comicsansms 16 bold").pack(side = LEFT)
Button(f4,text = "*",pady = 19,width = 6,fg = "white",bg = "black",command = multiplication,font = "comicsansms 16 bold").pack(side = LEFT)
Button(f4,text = "/",pady = 19,width = 6,fg = "white",bg = "black",command = division,font = "comicsansms 16 bold").pack(side = LEFT)
Button(f5,text = "+",pady = 19,width = 6,fg = "white",bg = "black",command = addition,font = "comicsansms 16 bold").pack(side = LEFT)
Button(f5,text = "-",pady = 19,width = 6,fg = "white",bg = "black",command = subtract,font = "comicsansms 16 bold").pack(side = LEFT)
Button(f5,text = "=",pady = 19,width = 6,fg = "white",bg = "black",command = equal,font = "comicsansms 16 bold").pack(side = LEFT)
Button(f6,text = "Clear All",pady = 19,width = 9,fg = "white",bg = "black",command = clear,font = "comicsansms 16 bold").pack(side = LEFT)
Button(f6,text = "^2",pady = 19,width = 6,fg = "white",bg = "black",command = c,font = "comicsansms 16 bold").pack(side = LEFT)
Button(f6,text = "^3",pady = 19,width = 6,fg = "white",bg = "black",command = cc,font = "comicsansms 16 bold").pack(side = LEFT)
f1.pack()
f2.pack()
f3.pack()
f4.pack()
f5.pack()
f6.pack()

root.config(bg = "black")
root.mainloop()