#print("Opened database successfully");
from doctest import master
import tkinter  as tk 
from tkinter import messagebox
from tkinter import * 

from database import connect_db
my_conn = connect_db()




size_all = 30
font_all='Arial 10'

class Detail(tk.Toplevel):
  def __init__(self, *args, title="Result Detail", **kwargs):   
    super().__init__(*args, **kwargs)

    self.title(title)

    w = self.winfo_reqwidth()
    h = self.winfo_reqheight()
    ws = self.winfo_screenwidth()
    hs = self.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    self.geometry('+%d+%d' % (x, y))
   
    # Create the main window
    
    t= tk.Label(self, text = title,font=('Helvetica', 13))
    t.pack(side = TOP)

    
    lbl1 = tk.Label(self, text = "Result Detail", anchor="w", justify="left", width=size_all, font=(font_all))   
    blank_lbl1 = tk.Label(self, text = "\n")    
    lbl1.pack()   
    blank_lbl1.pack()

    

    #b= tk.Button(self, text = "Login", command = lambda: validate_login())
    #b.pack()


    
    
    

if __name__ == "__main__":
    self = Detail()
    self.mainloop()
    