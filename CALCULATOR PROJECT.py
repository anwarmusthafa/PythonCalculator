from tkinter import *

window=Tk()
window.title("CALCULATOR")
window.geometry("304x413")
window.resizable(0,0)

display=Entry(width=47,borderwidth=10)
display.place(x=0,y=0)

def button_click(num):
    current=display.get()
    display.delete(0,END)
    display.insert(0,str(current)+str(num))


button=Button(window,text="0", width=9, height=5, bg="white", fg="black",command=lambda :button_click(0))
button.place(x=80,y=60)
button=Button(window,text=".", width=9, height=5, bg="white", fg="black",command=lambda :button_click('.'))
button.place(x=155,y=60)
button=Button(window,text="1", width=9, height=5, bg="white", fg="black",command=lambda :button_click(1))
button.place(x=5,y=148)
button=Button(window,text="2", width=9, height=5, bg="white", fg="black",command=lambda :button_click(2))
button.place(x=80,y=148)
button=Button(window,text="3", width=9, height=5, bg="white", fg="black",command=lambda :button_click(3))
button.place(x=155,y=148)
button=Button(window,text=".", width=9, height=5, bg="white", fg="black",command=lambda :button_click('.'))
button.place(x=5,y=236)
button=Button(window,text="5", width=9, height=5, bg="white", fg="black",command=lambda :button_click(5))
button.place(x=80,y=236)
button=Button(window,text="6", width=9, height=5, bg="white", fg="black",command=lambda :button_click(6))
button.place(x=155,y=236)
button=Button(window,text="7", width=9, height=5, bg="white", fg="black",command=lambda :button_click(7))
button.place(x=5,y=324)
button=Button(window,text="8", width=9, height=5, bg="white", fg="black",command=lambda :button_click(8))
button.place(x=80,y=324)
button=Button(window,text="9", width=9, height=5, bg="white", fg="black",command=lambda :button_click(9))
button.place(x=155,y=324)

def add():
    first_number=display.get()
    global math
    math='addition'
    global f
    f=int(first_number)
    display.delete(0,END)
button=Button(window,text="+", width=9, height=5, bg="white", fg="black",command=add)
button.place(x=230,y=148)

def subtration():
    first_number = display.get()
    global math
    math='subtration'
    global f
    f = int(first_number)
    display.delete(0,END)
button=Button(window,text="-", width=9, height=5, bg="white", fg="black",command=subtration)
button.place(x=230,y=236)

def multiplication():
    first_number = display.get()
    global math
    math='multiplication'
    global f
    f = int(first_number)
    display.delete(0,END)

button=Button(window,text="*", width=9, height=5, bg="white", fg="black",command=multiplication)
button.place(x=230,y=324)

def division():
    first_number = display.get()
    global math
    math='division'
    global f
    f = float(first_number)
    display.delete(0,END)


button = Button(window, text="/", width=9, height=5, bg="white", fg="black", command=division)
button.place(x=155, y=60)


def clear_button():
    display.delete(0,END)
button=Button(window,text="C", width=9, height=5, bg="white", fg="black",command=clear_button)
button.place(x=5,y=60)

def equal():
    second_number=display.get()
    display.delete(0,END)
    if math=='addition':
     display.insert(0,f+int(second_number))
    elif math=='subtration':
        display.insert(0,f-int(second_number))
    elif math=='multiplication':
        display.insert(0,f*float(second_number))
    elif math=='division':
        display.insert(0,f/float(second_number))

button=Button(window,text="=", width=9, height=5, bg="white", fg="black",command=equal)
button.place(x=230,y=60)



window.mainloop()
