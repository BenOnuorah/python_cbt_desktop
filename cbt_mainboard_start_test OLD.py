from multiprocessing import Value
import sqlite3
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

my_conn = sqlite3.connect(dir_path+'/cbt_app.db')

#print("Opened database successfully");
import tkinter  as tk
from tkinter import messagebox 
from tkinter import * 

size_all = 30
font_all='Arial 15'

class Start(tk.Toplevel):
  def __init__(self, *args, title="Take Test", **kwargs):   
    super().__init__(*args, **kwargs)  
 
  #def __init__(self, master, *args, title="Add Question", **kwargs):   
  #  super().__init__(*args, master,  **kwargs)
 
    #val_id = self.master.val_id

    
    #rec =  my_conn.execute("SELECT * FROM cbt_test WHERE id="+str(val_id)+" ")
    #record = rec.fetchone()

    #rec_id = record[0]
    #rec_test_name = record[1].strip()
    #rec_class_name = record[2]
    #rec_status = record[3]
   

    #print ("I am printing here "+ str(val_id))
    #print (rec_test_name)

   
    self.geometry("800x400") 
    self.title(title)

    w = self.winfo_reqwidth()
    h = self.winfo_reqheight()
    ws = self.winfo_screenwidth()
    hs = self.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    self.geometry('+%d+%d' % (x, y))
    

    #self.geometry("600x250")
   
     
    
   
    #t= tk.Label(self, text = f"Add Question to {rec_test_name}",font=(font_all))
    #t.pack(side = TOP)

    topic="Chemistry"
    topic_lbl= tk.Label(self, text = f"Topic: {topic}",font=('Helvetica', 13))
    topic_lbl.pack()


    question_title_lbl = tk.Label(self, text = "Question 1", font=('Helvetica', 11)) 
    question_title_lbl.pack()
    #scroll = tk.Scrollbar(self) 

    question="Your cooperative society need a professional \n software application to store and manage your transaction record as your record grows and data operation and retrieval becomes more complex and difficult with Microsoft excel spreadsheet."
    question_lbl=tk.Label(self, text=question, anchor="w", justify="left")
    question_lbl.pack()

    lbl6 = tk.Label(self,   text = "\n Select Correct Option", font=('Helvetica', 11))
    lbl6.pack()


    check1 = tk.IntVar()
    check2 = tk.IntVar()
    check3 = tk.IntVar()
    check4 = tk.IntVar()

    #ent6.set('A')
    r1 = tk.Checkbutton(self, text="A. Your cooperative society need a professional", variable=check1)   
    r2 = tk.Checkbutton(self, text="B. Your cooperative society", variable=check2)
    r3 = tk.Checkbutton(self, text="C. Software application to store and manage", variable=check3)
    r4 = tk.Checkbutton(self, text="D. Record grows and data operation", variable=check4)
    r1.pack()
    r2.pack()  
    r3.pack()
    r4.pack()
  
   
    
    def donothing():
        x = 0

    b= tk.Button(self, text = "Next", command = lambda: donothing())
    b.pack()
    #--------------------------------------------------------------

    #def add_data():
        

        
          
 


if __name__ == "__main__":
    self = Start()
    self.mainloop()     
