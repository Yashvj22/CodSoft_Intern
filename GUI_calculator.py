''' Design a simple calculator with basic arithmetic operations. Prompt the user to input two numbers and an operation choice.
    Perform the calculation and display the result '''

from tkinter import *

def evaluate():
    result = eval(expression.get())
    field.delete(0, END)
    field.insert(0, result)

def nine():
    current = expression.get()
    field.delete(0, END)
    field.insert(0, current + '9')

def eight():
    current = expression.get()
    field.delete(0, END)
    field.insert(0, current + '8')

def seven():
    current = expression.get()
    field.delete(0, END)
    field.insert(0, current + '7')

def six():
    current = expression.get()
    field.delete(0, END)
    field.insert(0, current + '6')

def five():
    current = expression.get()
    field.delete(0, END)
    field.insert(0, current + '5')

def four():
    current = expression.get()
    field.delete(0, END)
    field.insert(0, current + '4')

def three():
    current = expression.get()
    field.delete(0, END)
    field.insert(0, current + '3')

def two():
    current = expression.get()
    field.delete(0, END)
    field.insert(0, current + '2')

def one():
    current = expression.get()
    field.delete(0, END)
    field.insert(0, current + '1')

def plus():
    current = expression.get()
    field.delete(0, END)
    field.insert(0, current + '+')

def minus():
    current = expression.get()
    field.delete(0, END)
    field.insert(0, current + '-')

def multiply():
    current = expression.get()
    field.delete(0, END)
    field.insert(0, current + '*')

def divide():
    current = expression.get()
    field.delete(0, END)
    field.insert(0, current + '/')

def zero():
    current = expression.get()
    field.delete(0, END)
    field.insert(0, current + '0')

def decimal():
    current = expression.get()
    field.delete(0, END)
    field.insert(0, current + '.')

def clear():
    current = expression.get()
    field.delete(0, END)

root = Tk()

root.title("Calculator")

root.geometry("250x450")
root.minsize(width=100, height=200)

expression = StringVar()
field = Entry(textvariable=expression, font=20 )
field.pack(fill=X, padx=20, pady=20)


equals_to = Button(text="=", foreground='black',command=evaluate, font='20', width=2, height=2)
equals_to.pack()

f1 = Frame(root)
f1.pack(anchor='w', pady=5)

btn_7 = Button(f1, text="7", foreground='black', command=seven, font='20', width=2, height=2)
btn_7.pack(side=LEFT, padx=20 )

btn_8 = Button(f1, text="8", foreground='black', command=eight, font='20', width=2, height=2)
btn_8.pack(side=LEFT)

btn_9 = Button(f1, text="9", foreground='black', command=nine, font='20', width=2, height=2)
btn_9.pack(side=LEFT, padx=20)

btn_add = Button(f1, text="+", foreground='green', command=plus, font='20', width=2, height=2)
btn_add.pack()

f5 = Frame(root)
f5.pack(side=RIGHT, padx=20)

f2 = Frame(root)
f2.pack(anchor='w', pady=5)

btn_4 = Button(f2, text="4", foreground='black', command=four, font='20', width=2, height=2)
btn_4.pack(side=LEFT, padx=20)

btn_5 = Button(f2, text="5", foreground='black', command=five, font='20', width=2, height=2)
btn_5.pack(side=LEFT)

btn_6 = Button(f2, text="6", foreground='black', command=six, font='20', width=2, height=2)
btn_6.pack(side=LEFT, padx=20)

btn_subtract = Button(f2, text="-", foreground='green', command=minus, font='20', width=2, height=2)
btn_subtract.pack(side=LEFT)

f3 = Frame(root)
f3.pack(pady=5, anchor='w')

btn_1 = Button(f3, text="1", foreground='black', command=one, font='20', width=2, height=2)
btn_1.pack(side=LEFT, padx=20)

btn_2 = Button(f3, text="2", foreground='black', command=two, font='20', width=2, height=2)
btn_2.pack(side=LEFT)

btn_3 = Button(f3, text="3", foreground='black', command=three, font='20', width=2, height=2)
btn_3.pack(side=LEFT, padx=20)

btn_multiply = Button(f3, text="*", foreground='green', command=multiply, font='20', width=2, height=2)
btn_multiply.pack(side=LEFT)

f4 = Frame(root)
f4.pack(anchor='w', pady=5)

btn_0 = Button(f4, text="0", foreground='black', command=zero, font='20', width=2, height=2)
btn_0.pack(side=LEFT, padx=20)

btn_decimal = Button(f4, text=".", foreground='black', command=decimal, font='20', width=2, height=2)
btn_decimal.pack(side=LEFT)

clear_btn = Button(f4, text="C", foreground='red', command=clear, font='20', width=2, height=2)
clear_btn.pack(side=LEFT, padx=20)

btn_divide = Button(f4, text="/", foreground='green', command=divide, font='20', width=2, height=2)
btn_divide.pack(side=LEFT)

root.mainloop()