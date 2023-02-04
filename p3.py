from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("850x700")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 700,
    width = 850,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"p3bg3.png")
background = canvas.create_image(
    425.5, 350.5,
    image=background_img)

img = PhotoImage(file = f"next3.png")
b0 = Button(
    image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x =719, y = 648,
    width = 100,
    height = 30)

img1= PhotoImage(file = f"back3.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 32, y = 645,
    width = 100,
    height = 30)

window.resizable(False, False)
window.mainloop()
