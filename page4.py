import tkinter as tk
from tkinter import *
import os
from tkinter import ttk
from tkinter import colorchooser

def show():
    
    os.system("python Virtual_Canvas.py ")
def choose_color():
 
    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title ="Choose color")
    print(color_code)

def btn_clicked():
    print("Button Clicked")


def helpbtn_clicked():
    import Howtouse


window = tk.Tk()

window.geometry("850x700")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 700,
    width = 850,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

# label CHOOSE OBJECT COLOR DROPDOWN
img3 = PhotoImage(file = f"choosecolor.png")
l = Label(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")


l.place(x =500, y=164, width = 300 , height = 40)

# CHOOSE OBJECT COLOR DROPDROWN BOX
n = tk.StringVar()
colorchoosen = ttk.Combobox(window, width = 27, textvariable = n)
  
# Adding combobox drop down list
colorchoosen['values'] = (' blue', 
                          ' red',
                          ' yellow',
                          ' green',
                          )


  
colorchoosen.place(x =500,y = 200, width = 274.60 , height = 60)
colorchoosen.current(2)

# label CHOOSE YOUR TOOL DROPDOWN 
img4 = PhotoImage(file = f"choosetool.png")
l2 = Label(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

l2.place(
    x = 500, y = 320,
    width = 265, height= 40
)
# Combobox creation
n = tk.StringVar()
toolchoosen = ttk.Combobox(window, width = 27, textvariable = n)
  
# Adding combobox drop down list
toolchoosen['values'] = (' Object', 
                          ' Hand',
                          
                          )
  
toolchoosen.place(x =500,y = 360, width = 274.60 , height = 60)
toolchoosen.current(0)

background_img = PhotoImage(file = f"bg.png")
background = canvas.create_image(
    430.0, 350.0,
    image=background_img)

img = PhotoImage(file = f"opencanvasbtn.png")
b0 = Button(
    image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = show,
    relief = "flat")


b0.place(
    x = 537, y = 445,
    width = 175,
    height = 30)


img1 = PhotoImage(file = f"infobtn.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 750, y = 320,
    width = 48,
    height = 42)

img2 = PhotoImage(file = f"helpbtn.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = helpbtn_clicked,
    relief = "flat"
    )

b2.place(
    x = 151, y = 422,
    width = 136,
    height = 24)



window.resizable(False, False)
window.mainloop()
