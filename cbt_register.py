
#print("Opened database successfully");
import tkinter  as tk 
from tkinter import messagebox
from tkinter import * 
import sqlite3 

from database import connect_db
my_conn = connect_db()


size_all = 30
font_all='Arial 10'

class CBT_Reg(tk.Toplevel):
  def __init__(self, *args, title="Register to take test", **kwargs):   
    super().__init__(*args, **kwargs)

    #self = tk.Tk()
    #self.geometry("600x300") 
   
    
    my_conn.execute('''CREATE TABLE IF NOT EXISTS cbt_register (id INTEGER PRIMARY KEY, 
    surname TEXT, othername TEXT, class TEXT, gender TEXT, pass_word TEXT)''')
    my_conn.commit()

    # add one Label --- top
    self.title(title)

    w = self.winfo_reqwidth()
    h = self.winfo_reqheight()
    ws = self.winfo_screenwidth()
    hs = self.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    self.geometry('+%d+%d' % (x, y))
    

    #self.geometry("600x250")
   
     
    
   
    t= tk.Label(self, text = title,font=('Helvetica', 13))
    t.pack(side = TOP)

    t2= tk.Label(self, text = "You will be login in with your surname and password",font=('Helvetica', 9))
    t2.pack()

    

    lbl1 = tk.Label(self, text = "Surname", anchor="w", justify="left", width=size_all, font=(font_all))
    ent1 = tk.Entry(self, width=size_all, font=(font_all)) 
    blank_lbl1 = tk.Label(self, text = "\n")

    lbl2 = tk.Label(self, text = "Other Name", anchor="w", justify="left", width=size_all, font=(font_all))
    ent2 = tk.Entry(self, width=size_all, font=(font_all))
    blank_lbl2 = tk.Label(self, text = "\n")
    
    lbl3 = tk.Label(self, text = "Class", anchor="w", justify="left", width=size_all, font=(font_all))
    ent3 = tk.Entry(self, width=size_all, font=(font_all))   
    blank_lbl3 = tk.Label(self, text = "\n")

    lbl4 = tk.Label(self, text = "Gender", anchor="w", justify="left", width=size_all, font=(font_all))
    ent4 = tk.Entry(self, width=size_all, font=(font_all))   
    blank_lbl4 = tk.Label(self, text = "\n")

    lbl5 = tk.Label(self, text = "Password", anchor="w", justify="left", width=size_all, font=(font_all))
    ent5 = tk.Entry(self, show="*", width=size_all, font=(font_all))
    blank_lbl5 = tk.Label(self, text = "\n")

   

    lbl1.pack()
    ent1.pack()
    blank_lbl1.pack()

    lbl2.pack()
    ent2.pack()
    blank_lbl2.pack()

    lbl3.pack()
    ent3.pack()
    blank_lbl3.pack()

    lbl4.pack()
    ent4.pack()
    blank_lbl4.pack()

    lbl5.pack()
    ent5.pack()
    blank_lbl5.pack()


    def donothing():
        x = 0

    b= tk.Button(self, text = "Register", command = lambda: add_data())
    b.pack()

    def add_data():        
        val1=ent1.get().upper()                   
        val2=ent2.get()
        val3=ent3.get()
        val4=ent4.get()
        val5=ent5.get()        
      

        if(len(val1) > 2 or len(val2)> 2  or len(val3) > 2 or len(val4) > 2 or len(val5) > 2):           
            try:
               
                #validate before entry                
                rec = my_conn.execute('SELECT * FROM cbt_register WHERE pass_word=?', (val5,))                
                row = rec.fetchone()
                if row is None:                   
                    my_data=(None,val1,val2,val3,val4,val5)
                    my_query="INSERT INTO cbt_register values(?,?,?,?,?,?)"
                    my_conn.execute(my_query,my_data)
                    my_conn.commit()
                    
                    messagebox.showinfo("Record added", "Registration was successful")
                    self.withdraw()
                else:    

                    messagebox.showwarning("Warning", "Password already taken try another one!")
                    
                
               
                '''
                ent1.delete('1.0',END)  
                ent2.delete('1.0',END) 
                ent3.delete()
                ent4.delete()
                ent5.delete()
                '''
                               
            except sqlite3.Error as my_error:
                messagebox.showwarning("Warning", my_error)

        else:
            messagebox.showwarning("Missing entry", "Enter value for...")
       

if __name__ == "__main__":
    self = CBT_Reg()
    self.mainloop()     
