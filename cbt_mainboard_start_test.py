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
THEME_COLOR = "#375362"

global response
#global question
#question="Your cooperative society need a professional software application to store and manage your transaction record as your record grows and data operation and retrieval becomes more complex and difficult with Microsoft excel spreadsheet."
question=""

class Start(tk.Toplevel):

  #def __init__(self, *args, title="Take Test", **kwargs):   
  #  super().__init__(*args, **kwargs)  
 

       

  def __init__(self, master, *args, title="Take Test", **kwargs):   
    super().__init__(*args, master,  **kwargs)
 
    val_id = self.master.val_id

    
    rec =  my_conn.execute("SELECT * FROM cbt_test WHERE id="+str(val_id)+" ")
    record = rec.fetchone()

    rec_id = record[0]
    rec_test_name = record[1].strip()
    rec_class_name = record[2]
    rec_status = record[3]

    #-------------------------------
    rec = my_conn.execute("SELECT * FROM cbt_questions WHERE test_id="+str(rec_id)+" ORDER By id")
    record = rec.fetchall()
   
    
    def next_question(next):
        queston_id = next
        print (queston_id)
        
        for row in record:
            quest_id = row[0]
            rec_question = row[2].strip()
            rec_opt1 = row[3]
            rec_opt2 = row[4]
            rec_opt3 = row[5]
            rec_opt4 = row[6]
            rec_correct = row[7]
            rec_explain = row[8]

            question=rec_question
            lbl_question["text"] = question  

            r1_lbl["text"] = (f"A. {rec_opt1}")
            r2_lbl["text"] = (f"B. {rec_opt2}")
            r3_lbl["text"] = (f"C. {rec_opt3}")
            r4_lbl["text"] = (f"D. {rec_opt4}")
    
    #-------------------------------------
   
    self.title(title)
    self.geometry('{}x{}'.format(700, 450))

    # create all of the main containers
    top_frame = Frame(self, bg='white', width=450, height=50, pady=3)
    center = Frame(self, bg='gray2', width=50, height=40, padx=3, pady=3)
    btm_frame = Frame(self, bg='white', width=450, height=45, padx=3, pady=3)
    #btm_frame2 = Frame(self, bg='lavender', width=450, height=60, pady=3)

    # layout all of the main containers
    self.grid_rowconfigure(1, weight=1)
    self.grid_columnconfigure(0, weight=1)

    top_frame.grid(row=0, sticky="ew")
    center.grid(row=1, sticky="nsew")
    btm_frame.grid(row=3, sticky="ew")


    # create the widgets for the top frame -------------------
    topic=rec_test_name
    main_topic = Label(top_frame, bg='white', text = f"Topic: {topic}",font=('Helvetica', 15))
    sub_topic = Label(top_frame, bg='white', text = "Question 1",font=('Helvetica', 11))
   

    # layout the widgets in the top frame
    main_topic.grid(row=0, columnspan=3)
    sub_topic.grid(row=1, column=0)


    center.grid_rowconfigure(0, weight=1)
    center.grid_columnconfigure(1, weight=1)

    ctr_left = Frame(center, bg='white', width=400, height=190)
    ctr_mid = Frame(center, bg='#d3dded', height=190, padx=3, pady=3)


    #question="Your cooperative society need a professional software application to store and manage your transaction record as your record grows and data operation and retrieval becomes more complex and difficult with Microsoft excel spreadsheet."
    lbl_question = tk.Label(ctr_left, bg='white',  text=question, wraplength=400, justify="left")
    lbl_question.grid(row=0, column=0)   

    #---------------------------- Objects in the (center frame- ctr_mid) --------------------------------
    lbl_instruction = tk.Label(ctr_mid, bg='#d3dded',  text = "Select Correct Option", font=('Helvetica', 11))
    lbl_instruction.grid(row=2, column=1)

    check = IntVar()

    # option A ---------------------------------------------------
    r1 = tk.Radiobutton(ctr_mid, variable=check, value=1)  
    r1.grid(row=3, column=0)
    r1_lbl = tk.Label(ctr_mid, bg='#d3dded', text = "A. ... ")
    r1_lbl.grid(row=3, column=1)

    # option B ---------------------------------------------------
    r2 = tk.Radiobutton(ctr_mid, variable=check, value=2)  
    r2.grid(row=4, column=0)
    r2_lbl = tk.Label(ctr_mid, bg='#d3dded', text = "B. ... ")
    r2_lbl.grid(row=4, column=1)

    # option C ---------------------------------------------------
    r3 = tk.Radiobutton(ctr_mid, variable=check, value=3)  
    r3.grid(row=5, column=0)
    r3_lbl = tk.Label(ctr_mid, bg='#d3dded', text = "C. ... ")
    r3_lbl.grid(row=5, column=1)


    # option D ---------------------------------------------------
    r4 = tk.Radiobutton(ctr_mid, variable=check, value=4)  
    r4.grid(row=6, column=0)
    r4_lbl = tk.Label(ctr_mid, bg='#d3dded', text = "D. ... ")
    r4_lbl.grid(row=6, column=1)


    ctr_left.grid(row=0, column=0, sticky="ns")
    ctr_mid.grid(row=0, column=1, sticky="nsew")
    #ctr_right.grid(row=0, column=2, sticky="ns")

    #b1 = Button(ctr_mid, text = "Previous")
    #b2 = Button(ctr_mid, text = "Next")

    rec2 = my_conn.execute("SELECT * FROM cbt_questions WHERE test_id="+str(rec_id)+" ORDER By id")
    record2 = rec2.fetchall()
    for row in record2:
        next = row[0]

        
   

    b1 = Button(btm_frame, text = "Previous")
    b2 = Button(btm_frame, text = "Next", command=next_question(next))


    b1.grid(row = 0, column = 0, sticky="ns")
    b2.grid(row = 0, column = 1, sticky="nsew")


    #=========================================================

    

       
        #return score

  
if __name__ == "__main__":
    self = Start()
    self.mainloop()    
    
