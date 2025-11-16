from tkinter import *

root = Tk()
root.title("d-value Generator")
root.geometry("170x250")

active_entry = None

def entry_1(event):
    global active_entry
    active_entry = entry_e

def entry_2(event):
    global active_entry
    active_entry = entry_mod

def Click_e(number):
    if active_entry is None:
        return
    first_digit = active_entry.get()
    active_entry.delete(0, END)
    active_entry.insert(0, first_digit + str(number))

def Clr():
    entry_d.delete(0, END)

def generate():
    entry_d.delete(0, END)
    num_list = []
    e = int(entry_e.get())
    mod = int(entry_mod.get())

    for num in range(1, 1001):
        if (e * num) % mod == 1:
            num_list.append(num)

    entry_d.insert(0, str(num_list))


# create buttons
button1 = Button(root, text="1", padx=20, pady=10, command=lambda: Click_e(1))
button1.grid(row=2, column=0)
button2 = Button(root, text="2", padx=20, pady=10, command=lambda: Click_e(2))
button2.grid(row=2, column=1)
button3 = Button(root, text="3", padx=20, pady=10, command=lambda: Click_e(3))
button3.grid(row=2, column=2)
button4 = Button(root, text="4", padx=20, pady=10, command=lambda: Click_e(4))
button4.grid(row=3, column=0)
button5 = Button(root, text="5", padx=20, pady=10, command=lambda: Click_e(5))
button5.grid(row=3, column=1)
button6 = Button(root, text="6", padx=20, pady=10, command=lambda: Click_e(6))
button6.grid(row=3, column=2)
button7 = Button(root, text="7", padx=20, pady=10, command=lambda: Click_e(7))
button7.grid(row=4, column=0)
button8 = Button(root, text="8", padx=20, pady=10, command=lambda: Click_e(8))
button8.grid(row=4, column=1)
button9 = Button(root, text="9", padx=20, pady=10, command=lambda: Click_e(9))
button9.grid(row=4, column=2)
button0 = Button(root, text="0", padx=20, pady=10, command=lambda: Click_e(0))
button0.grid(row=5, column=0)

button_clear = Button(root, text="C", padx=20, pady=10, command=Clr)
button_clear.grid(row=5, column=1)
button_generate = Button(root, text="=", padx=20, pady=10, command=generate)
button_generate.grid(row=5, column=2)

entry_e = Entry(root, width=10)
entry_e.place(x=0, y=200)
entry_e.bind("<FocusIn>", entry_1)
Label(root, text="e-value", font="century 8").place(x=0, y=178)

entry_mod = Entry(root, width=10)
entry_mod.place(x=70, y=200)
entry_mod.bind("<FocusIn>", entry_2)
Label(root, text="mod", font="century 8").place(x=70, y=178)

entry_d = Entry(root, width=20)
entry_d.place(x=0, y=225)

root.mainloop()
