from tkinter import *

root = Tk()
root.title("A basic calculator")

entry_value = Entry(root, width=50, borderwidth=6)
entry_value.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

def button_click(number):
     entry_value.insert(END, str(number))

# can similarly be done this way
# def button_click(number):
    # current = entry_value.get()
    # entry_value.delete(0, END)
    # entry_value.insert(0, str(current) + str(number))
    
def button_clear():
     entry_value.delete(0, END)

def button_add():
     global initial_value
     initial_value = int(entry_value.get())
     entry_value.delete(0, END)

def button_equal():
     second_value = entry_value.get()
     entry_value.delete(0, END)
     entry_value.insert(0, initial_value + int(second_value))


# defining buttons
button1 = Button(root, text="1", padx=40, pady=20, command= lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_addition = Button(root, text="+", padx=40, pady=91,command= button_add)
button_equals = Button(root, text="=", padx=91, pady=20, command=lambda: button_equal())
button_erase = Button(root, text="clear", padx=40, pady=20, command=button_clear)

# clicking button on to screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
button_erase.grid(row=4, column=1)
button_equals.grid(row=4, column=2, columnspan=2)

button_addition.grid(row=1, column=3, rowspan=3)


root.mainloop()
