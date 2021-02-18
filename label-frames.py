from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Tkinter Frames")

# Creating a left frame label. When your packing your widget, the
# options side, fill and expand are very important.

fst_frame = Frame(window)
fst_frame.pack(fill="both", expand="yes")

left_frame_label_1 = LabelFrame(fst_frame, text="Left Frame")
left_frame_label_1.pack(side="left", fill="both", expand="yes")

right_frame_label_2 = LabelFrame(fst_frame, text="Right Frame")
right_frame_label_2.pack(side="right", fill="both", expand="yes")

scnd_frame = Frame(window)
scnd_frame.pack()

left_frame_label_1 = LabelFrame(fst_frame, text="Second Frame")
left_frame_label_1.pack()

window.mainloop()
