Window:
from tkinter import *
window=Tk()
window['bg'] = 'pink'
lbl=Label(window, text="Name: Zashi Avinash Patil", fg='olive', font=("Helvetica", 16))
lbl.place(x=60, y=50)
btn=Button(window, text="Roll No.:31 ", fg='purple')
btn.place(x=150, y=100)
window.title('Welcome to PVG')
window.geometry("350x200+10+10")
window.mainloop()
Calculator:
from tkinter import *
class MyWindow:
def __init__(self, win):
self.lbl1=Label(win, text='First number')
self.lbl2=Label(win, text='Second number')
self.lbl3=Label(win, text='Result')
self.t1=Entry(bd=3)
self.t2=Entry()
self.t3=Entry()
self.btn1 = Button(win, text='Add')
self.btn2=Button(win, text='Subtract')
self.lbl1.place(x=100, y=50)
self.t1.place(x=200, y=50)
self.lbl2.place(x=100, y=100)
self.t2.place(x=200, y=100)
self.b1=Button(win, text='Add', command=self.add)
self.b2=Button(win, text='Subtract')
self.b2.bind('<Button-1>', self.sub)
self.b1.place(x=100, y=150)
self.b2.place(x=200, y=150)
self.lbl3.place(x=100, y=200)
self.t3.place(x=200, y=200)
def add(self):
self.t3.delete(0, 'end')
num1=int(self.t1.get())
num2=int(self.t2.get())
result=num1+num2
self.t3.insert(END, str(result))
def sub(self, event):
self.t3.delete(0, 'end')
num1=int(self.t1.get())
num2=int(self.t2.get())
result=num1-num2
self.t3.insert(END, str(result))
window=Tk()
mywin=MyWindow(window)
window.title('Calculator')
window['bg'] = 'pink'
window.geometry("400x300+10+10")
window.mainloop()