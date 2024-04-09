import tkinter as tk
from tkinter import *


from PIL import Image, ImageTk
import os

#from cbt_create_new_test import create_test

#my classes
import cbt_class, cbt_create_new_test, cbt_manage_test, cbt_register, cbt_login

font_size_small='arial 12'
font_size_large='arial 17'

dir_path = os.path.dirname(os.path.realpath(__file__))

def install_server(): 
    lbl_status["text"] = "Installing"
   
def start_server():   
    lbl_status["text"] = "Server started"

def start_app(): 
    lbl_status["text"] = "CBT App started"  

#def create_new(): 
#    cbt_create_new_test.CreateTest()   

def open_win():
    new= Toplevel(window)
    new.geometry("750x250")
    new.title("New Window")
    #window.eval('tk::PlaceWindow . center')
    window.eval(f'tk::PlaceWindow {str(new)} center')
    #new.eval('tk::PlaceWindow %s center' % new.winfo_pathname(new.winfo_id()))
    #Create a Label in New window
    Label(new, text="Hey, Howdy?", font=('arial 17')).pack(pady=30)

    new.wm_transient(window)

def open_win1():
    root= Toplevel(window)
    #root.geometry("750x250")
    root.title("New Window")
   
    # Apparently a common hack to get the window size. Temporarily hide the
    # window to avoid update_idletasks() drawing the window in the wrong
    # position.
    root.withdraw()
    root.update_idletasks()  # Update "requested size" from geometry manager

    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry("+%d+%d" % (x, y))

    # This seems to draw the window frame immediately, so only call deiconify()
    # after setting correct window position

    Label(root, text="Hello world").pack()

    
#from tkinter.filedialog import askopenfilename, asksaveasfilename




window = tk.Tk()

#main window screen
#getting screen width and height of display
width= window.winfo_screenwidth() 
height= window.winfo_screenheight()

#width = 750
#height = 250

#setting tkinter window size
#window.eval('tk::PlaceWindow . center')
window.geometry("%dx%d" % (width, height))
window.title("EduSystem CBT Software")
window.attributes('-alpha',True)

#Main menus
def donothing():
   x = 0
   
menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0, font=(font_size_small))
filemenu.add_command(label="New", command=open_win)
filemenu.add_command(label="Open", command=open_win1)
filemenu.add_command(label="Save", command=lambda: cbt_class.SecondWindow())
filemenu.add_separator()
filemenu.add_command(label="Exit", command=menubar.quit)
menubar.add_cascade(label="File",font=(font_size_small), menu=filemenu)

adminmenu = Menu(menubar, tearoff=0, font=(font_size_small))
adminmenu.add_command(label="Create New Test", command=lambda: cbt_create_new_test.CreateTest())
adminmenu.add_command(label="Manage Test", command=lambda: cbt_manage_test.ManageTest())
menubar.add_cascade(label="Administrator",font=(font_size_small), menu=adminmenu)

helpmenu = Menu(menubar, tearoff=0, font=(font_size_small))
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", font=(font_size_small), menu=helpmenu)
#-------------------------- end menu -----------------------------------------

# main image 
image = Image.open(dir_path+'/img/1.jpg')
image = ImageTk.PhotoImage(image)
label_img = tk.Label(window, image=image)
label_img.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

# Quick Access buttons --- In Frame
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

btn_install = tk.Button(frm_buttons, text="Register to take test",  font=(font_size_large), command=lambda: cbt_register.CBT_Reg())
btn_start = tk.Button(frm_buttons, text="Take Test",  font=(font_size_large), command=lambda: cbt_login.CBT_Login())
#btn_open = tk.Button(frm_buttons, text="Start CBT App",  font=(font_size_large), command=start_app)
btn_exit = tk.Button(frm_buttons, text="Exit",  font=(font_size_large), command=window.quit)
lbl_status=tk.Label(frm_buttons, text="",  font=(font_size_large))

'''
ns
ew
nsew
'''

btn_install.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_start.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
#btn_open.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_exit.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
lbl_status.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

frm_buttons.grid(row=0, column=0, sticky="ns")







window.mainloop()
