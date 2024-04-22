from multiprocessing import Value


#print("Opened database successfully");
import tkinter  as tk
from tkinter import messagebox 
from tkinter import * 
import sqlite3 
from database import connect_db
my_conn = connect_db()

size_all = 30
font_all='Arial 15'

class AddQuestion(tk.Toplevel):
  def __init__(self, master, *args, title="Add Question", **kwargs):   
    super().__init__(*args, master,  **kwargs)
 
    val_id = self.master.val_id

    
    rec =  my_conn.execute("SELECT * FROM cbt_test WHERE id="+str(val_id)+" ")
    record = rec.fetchone()

    rec_id = record[0]
    rec_test_name = record[1].strip()
    rec_class_name = record[2]
    rec_status = record[3]
   

    #print ("I am printing here "+ str(val_id))
    #print (rec_test_name)

   
    #self.geometry("600x300") 
    self.title(title)

    w = self.winfo_reqwidth()
    h = self.winfo_reqheight()
    ws = self.winfo_screenwidth()
    hs = self.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    self.geometry('+%d+%d' % (x, y))
    

    #self.geometry("600x250")
   
     
    
   
    t= tk.Label(self, text = f"Add Question to {rec_test_name}",font=(font_all))
    t.pack(side = TOP)

    
    
    lbl1 = tk.Label(self, text = "Question", anchor="w", justify="left", width=size_all)
    ent1 = tk.Text(self, height = 5, width=size_all)  
    scroll = tk.Scrollbar(self) 
    ent1.configure(yscrollcommand=scroll.set) 
    scroll.config(command=ent1.yview) 
    scroll.pack(side=tk.RIGHT, fill=tk.Y) 

    blank_lbl1 = tk.Label(self, text = "\n")

    lbl2 = tk.Label(self, text = "Option 1", anchor="w", justify="left", width=size_all)
    ent2 = tk.Entry(self, width=size_all)   
    #blank_lbl2 = tk.Label(self, text = "\n")
    
    lbl3 = tk.Label(self, text = "Option 2", anchor="w", justify="left", width=size_all)
    ent3 = tk.Entry(self, width=size_all)  
    #blank_lbl3 = tk.Label(self, text = "\n")

    lbl4 = tk.Label(self, text = "Option 3", anchor="w", justify="left", width=size_all)
    ent4 = tk.Entry(self, width=size_all)  
    #blank_lbl4 = tk.Label(self, text = "\n")


    lbl5 = tk.Label(self, text = "Option 4", anchor="w", justify="left", width=size_all)
    ent5 = tk.Entry(self, width=size_all)    
    #blank_lbl5 = tk.Label(self, text = "\n")

    lbl6 = tk.Label(self,   text = "Select Correct Option", anchor="w", justify="left", width=size_all )
    
    '''
    check1 = tk.IntVar()
    check2 = tk.IntVar()
    check3 = tk.IntVar()
    check4 = tk.IntVar()

    #ent6.set('A')
    r1 = tk.Checkbutton(self, text="A", variable=check1)   
    r2 = tk.Checkbutton(self, text="B", variable=check2)
    r3 = tk.Checkbutton(self, text="C", variable=check3)
    r4 = tk.Checkbutton(self, text="D", variable=check4)
    '''

    check = IntVar()
    r1 = tk.Radiobutton(self, text="A", variable=check, value=1) 
    r2 = tk.Radiobutton(self, text="B", variable=check, value=2)
    r3 = tk.Radiobutton(self, text="C", variable=check, value=3)
    r4 = tk.Radiobutton(self, text="D", variable=check, value=4)

   # blank_lbl6 = tk.Label(self, text = "\n")
    
   
    lbl7 = tk.Label(self, text = "Explain", anchor="w", justify="left", width=size_all)
    ent7 = tk.Entry(self, width=size_all)    
    #blank_lbl7 = tk.Label(self, text = "\n")

   

    lbl1.pack()
    ent1.pack()
    blank_lbl1.pack()

   
    lbl2.pack()
    ent2.pack()
    #blank_lbl2.pack()

    lbl3.pack()
    ent3.pack()
    #blank_lbl3.pack()

    lbl4.pack()
    ent4.pack()
    #blank_lbl4.pack()

    lbl5.pack()
    ent5.pack()
    #blank_lbl5.pack()

    lbl6.pack()
    r1.pack()
    r2.pack()  
    r3.pack()
    r4.pack()
    #blank_lbl6.pack()

    lbl7.pack()
    ent7.pack()
   
    
    def donothing():
        x = 0

    b= tk.Button(self, text = "Add", command = lambda: add_data())
    b.pack(side=BOTTOM)
    #--------------------------------------------------------------

    def add_data():
        my_conn.execute('''CREATE TABLE IF NOT EXISTS cbt_questions (id INTEGER PRIMARY KEY, 
        test_id INTEGER, question TEXT, question1 TEXT, question2 TEXT, question3 TEXT, question4 TEXT,  
        right_option TEXT, explanation TEXT)''')
        my_conn.commit()
       

       

        record_id=rec_id 
        question=ent1.get("1.0",END) 
        ans1=ent2.get()
        ans2=ent3.get()
        ans3=ent4.get()
        ans4=ent5.get()

        '''
        opt1=check1.get() 
        opt2=check2.get()
        opt3=check3.get()
        opt4=check4.get()
        '''

        right_opt = check.get()

        #right_opt= f"{opt1}{opt2}{opt3}{opt4}"
        explain=ent7.get() 

                   



        if(len(question) > 2 or len(ans1)> 2  or len(right_opt) > 2 ):           
            try:
                #print("Connected to database successfully")
                my_data=(None,record_id,question,ans1,ans2,ans3,ans4,right_opt,explain)
                my_query="INSERT INTO cbt_questions values(?,?,?,?,?,?,?,?,?)"
                my_conn.execute(my_query,my_data)
                my_conn.commit()
                
                messagebox.showinfo("Record added", "Your record is now added.")
                
               
               
                ent1.delete('1.0',END)  
                ent2.delete('1.0',END) 
                ent3.delete()
                ent4.delete()
                ent5.delete()
                ent7.delete()

                #ent2.delete('1.0',END)
                #ent2.delete('1.0',END)

            except sqlite3.Error as my_error:
                messagebox.showwarning("Warning", my_error)

        else:
            messagebox.showwarning("Missing entry", "Enter value for Question")
          
 

'''
if __name__ == "__main__":
    self = AddQuestion()
    self.mainloop()     
'''