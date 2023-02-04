from tkinter import *


#def backbtn_clicked():
#  import page4




window = Tk()

window.geometry("1318x967")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 967,
    width = 1318,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"howtouse.png")
background = canvas.create_image(
    650.0, 480.0,
    image=background_img)

img = PhotoImage(file = f"backbtn.png")
b0 = Button(
    image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = backbtn_clicked,
    relief = "flat")

b0.place(
    x = 1121.44, y = 910.43,
    width = 160.29,
    height = 35.02)

window.resizable(False, False)
window.mainloop()
