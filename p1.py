from tkinter import *
import tkinter as tk 

  
def Page1():
    def btn_clicked():
        window.destroy()
        Page2()
    
    def center_window_on_screen():
        x_cord = int((screen_width/2) - (width/2))
        y_cord = int((screen_height/2) - (height/2))
        window.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))
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
    
    width, height = 850, 700
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    center_window_on_screen()

    background_img = PhotoImage(file = f"bg1.png")
    background = canvas.create_image(
        425.5, 350.5,
        image=background_img)
    
    img = PhotoImage(file = f"next1.png")
    b0 = Button(
        image = img,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")
    
    b0.place(
        x = 717, y = 638,
        width = 100,
        height = 30
        )
    
    window.resizable(False, False)
    window.mainloop()


def Page2():
    def center_window_on_screen():
        x_cord = int((screen_width/2) - (width/2))
        y_cord = int((screen_height/2) - (height/2))
        window.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))


    def next1():
        window.destroy()
        Page3()
        
    def back1():
        window.destroy()
        Page1()
    
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
    
    width, height = 850, 700
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    center_window_on_screen()

    background_img = PhotoImage(file = f"bg2.png")
    background = canvas.create_image(
        425.0, 350.0,
        image=background_img)
    
    img = PhotoImage(file = f"next2.png")
    b0 = Button(
        image = img,
        borderwidth = 0,
        highlightthickness = 0,
        command = next1,
        relief = "flat")
    
    b0.place(
        x =719, y = 648,
        width = 100,
        height = 30)
    
    img1= PhotoImage(file = f"back2.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = back1,
        relief = "flat")
    
    b1.place(
        x = 32, y = 645,
        width = 100,
        height = 30)
    window.resizable(False, False)
    window.mainloop()

def Page3():
    def center_window_on_screen():
        x_cord = int((screen_width/2) - (width/2))
        y_cord = int((screen_height/2) - (height/2))
        window.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))

    def next1():
       window.destroy()
       Page4()
       
    def back1():
       window.destroy()
       Page2()


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

    width, height = 850, 700
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    center_window_on_screen()

    background_img = PhotoImage(file = f"p3bg3.png")
    background = canvas.create_image(
        425.5, 350.5,
        image=background_img)

    img = PhotoImage(file = f"next3.png")
    b0 = Button(
        image = img,
        borderwidth = 0,
        highlightthickness = 0,
        command = next1,
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
        command = back1,
        relief = "flat")

    b1.place(
        x = 32, y = 645,
        width = 100,
        height = 30)

    window.resizable(False, False)
    window.mainloop()

def Page4():

    import tkinter as tk
    import os
    from tkinter import ttk
    from tkinter import colorchooser
    def center_window_on_screen():
        x_cord = int((screen_width/2) - (width/2))
        y_cord = int((screen_height/2) - (height/2))
        window.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))

    def show():
        
        os.system("python Virtual_Canvas.py ")
    def choose_color():
     
        # variable to store hexadecimal code of color
        color_code = colorchooser.askcolor(title ="Choose color")
        print(color_code)

    def back1():
        window.destroy()
        Page3()


    def helpbtn_clicked():
        howtoUse()
 
    def tools():
        opentools()


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


    width, height = 850, 700
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    center_window_on_screen()

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
        command = tools,
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

    img3= PhotoImage(file = f"back3.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = back1,
        relief = "flat")

    b3.place(
        x =719, y = 648,
        width = 100,
        height = 30)

    window.resizable(False, False)
    window.mainloop()
    
def howtoUse():
    def center_window_on_screen():
        x_cord = int((screen_width/2) - (width/2))
        y_cord = int((screen_height/2) - (height/2))
        window.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))
    def back1():
        window.destroy()
        Page4()
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
    width, height = 850, 700
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    center_window_on_screen()

    background_img = PhotoImage(file = f"howtouse.png")
    background = canvas.create_image(
        650.0, 480.0,
        image=background_img)

    img = PhotoImage(file = f"backbtn.png")
    b0 = Button(
        image = img,
        borderwidth = 0,
        highlightthickness = 0,
        command = back1,
        relief = "flat")

    b0.place(
        x = 1121.44, y = 910.43,
        width = 160.29,
        height = 35.02)

    window.resizable(False, False)
    window.mainloop()
    

def opentools():
    def center_window_on_screen():
        x_cord = int((screen_width/2) - (width/2))
        y_cord = int((screen_height/2) - (height/2))
        window.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))
    def back1():
        window.destroy()
        Page4()
    window = Tk()

    window.geometry("864x427")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 427,
        width = 864,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)
    width, height = 864, 427
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    center_window_on_screen()

    background_img = PhotoImage(file = f"tool.png")
    background = canvas.create_image(
        650, 480.0,
        image=background_img)

    img = PhotoImage(file = f"backbtn.png")
    b0 = Button(
        image = img,
        borderwidth = 0,
        highlightthickness = 0,
        command = back1,
        relief = "flat")

    b0.place(
        x = 726, y = 385,
        width = 105.6,
        height = 19)

    window.resizable(False, False)
    window.mainloop()  
Page1()


  