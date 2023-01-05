from tkinter import *

window = Tk()
def from_kg():
    gram = float(e2_value.get())*1000
    pound = float(e2_value.get())*2.20462
    ounce = float(e2_value.get())*35.274
    quintal = float(e2_value.get())*0.01
    t1.delete("1.0",END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)
    t4.delete("1.0",END)
    t4.insert(END, quintal)

window.title('GUI - Weight Converter')

e1 = Label(window, text="Input the weight in KG")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text="Gram", bg="orange")
e4 = Label(window, text="Pound", bg="light blue")
e5 = Label(window, text="Ounce", bg="light green")
e6 = Label(window, text="Quintal", bg="yellow")

t1 = Text(window, height=5, width=20)
t2 = Text(window, height=5, width=20)
t3 = Text(window, height=5, width=20)
t4 = Text(window, height=5, width=20)

b1 = Button(window, text="Convert", bg="sky blue", command=from_kg)

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
e6.grid(row=1, column=3)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
t4.grid(row=2, column=3)
b1.grid(row=0, column=2)

window.mainloop()
