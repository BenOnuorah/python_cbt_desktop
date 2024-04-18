#print("Opened database successfully");
from doctest import master
import tkinter  as tk 
from tkinter import messagebox
from tkinter import * 

from database import connect_db
my_conn = connect_db()

import cbt_mainboard

global loginuser, loginpw, loginout, loginid

size_all = 30
font_all='Arial 10'

class CBT_Login(tk.Toplevel):
  def __init__(self, *args, title="Login to take test", **kwargs):   
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

    
    lbl1 = tk.Label(self, text = "Surname", anchor="w", justify="left", width=size_all, font=(font_all))
    ent1 = tk.Entry(self, width=size_all, font=(font_all)) 
    blank_lbl1 = tk.Label(self, text = "\n")

    lbl5 = tk.Label(self, text = "Password", anchor="w", justify="left", width=size_all, font=(font_all))
    ent5 = tk.Entry(self, show="*", width=size_all, font=(font_all))
    blank_lbl5 = tk.Label(self, text = "\n")

    lbl1.pack()
    ent1.pack()
    blank_lbl1.pack()

    lbl5.pack()
    ent5.pack()
    blank_lbl5.pack()

    b= tk.Button(self, text = "Login", command = lambda: validate_login())
    b.pack()


    
     # Function to validate the login
    def validate_login():
        val1=ent1.get()
        val5=ent5.get()

        #rec = my_conn.execute("SELECT * FROM cbt_register WHERE surname="+str(val1)+" AND pass_word="+str(val5)+" ")
        val1=val1.upper()
        rec = my_conn.execute('SELECT * FROM cbt_register WHERE pass_word=? AND surname=?', (val5,val1,)) 
        row = rec.fetchone()
        if row is None:
            messagebox.showwarning("Warning", "You have not registered yet!")
        else:  
            rec_id = row[0]  
            #move to student dashboard....
            self.loginuser=val1
            self.loginpw=val5
            self.loginid=rec_id

            
            messagebox.showinfo("Welcome", "Welcome to login")
            cbt_mainboard.AllTest(self)
            self.withdraw()
            
        # You can add your own validation logic here
        #if userid == "admin" and password == "password":
        #    messagebox.showinfo("Login Successful", "Welcome, Admin!")
        #else:
        #    messagebox.showerror("Login Failed", "Invalid username or password")

    

if __name__ == "__main__":
    self = CBT_Login()
    self.mainloop()
    