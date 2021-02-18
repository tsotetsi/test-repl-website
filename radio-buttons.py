from tkinter import *

root = Tk()
root.geometry("300x300")
root.title("Tkinter Radio Buttons")

selected_value = IntVar()

# Creating Radio buttons using tkinter
Radiobutton(root, text="One", variable=selected_value, value=1).pack(anchor=W)
Radiobutton(root, text="Two", variable=selected_value, value=2).pack(anchor=W)

mainloop()
