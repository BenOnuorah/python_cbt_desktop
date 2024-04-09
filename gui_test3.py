import tkinter as tk
from tkinter import *
import sqlite3
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

my_conn = sqlite3.connect(dir_path+'/cbt_app.db')

root = Tk()
root.title('Question')


question=""
count = 0
question_num_count=""
   
 
#next=1    
#def next_question(next):

limit=0
offset=1


rec =  my_conn.execute("SELECT * FROM cbt_test WHERE id=1")
record = rec.fetchone()
rec_id = record[0]
rec_test_name = record[1].strip()
question=rec_test_name


def loop_question():
        global count
        global limit
        global offset
        
        # ---------------------------------------------------
        # option A radio
        r1 = tk.Radiobutton(ctr_mid, variable=check, value=1)  
        r1.grid(row=3, column=0)

         # option B radio
        r2 = tk.Radiobutton(ctr_mid, variable=check, value=2)  
        r2.grid(row=4, column=0)

        # option C radio
        r3 = tk.Radiobutton(ctr_mid, variable=check, value=3)  
        r3.grid(row=5, column=0)

        # option D radio
        r4 = tk.Radiobutton(ctr_mid, variable=check, value=4)  
        r4.grid(row=6, column=0)
        #--------------------------------------------------
       

        sql_query="SELECT * FROM cbt_questions WHERE test_id=1 ORDER By id LIMIT ?, ?"
        rec = my_conn.execute(sql_query,(limit, offset))
        #rec = my_conn.execute(sql_query,(count, count))
        record = rec.fetchall()

       
      
        answers=[]

        lbl_instruction["text"]="Select the correct option"
        
        for row in record:
            #----------------------------------
            limit=limit+1

            count = count + 1
            #print (count)

            question_num_count=f"Question {count}"
            sub_topic["text"]=question_num_count


            print (f"limit:{limit}, offset:{offset}")
            #------------------------------
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


            selected_option = check.get()
            msg = f"You selected the option {selected_option}"
            check.set(None)

            #insert score to the database....
            print (count)
            print (msg)

            #if row
       
        if len(record) == 0:   
            b2["text"]="End"
            count = count
            sub_topic["text"]=f"Question {count}"
            
            print ('End of record')   

       
        #label.config(text=selected)    
        


#root.withdraw()
#root.update_idletasks()  # Update "requested size" from geometry manager
#x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
#y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
#root.geometry("+%d+%d" % (x, y))

root.geometry('{}x{}'.format(700, 450))

# create all of the main containers
top_frame = Frame(root, bg='white', width=450, height=50, pady=3)
center = Frame(root, bg='gray2', width=50, height=40, padx=3, pady=3)
btm_frame = Frame(root, bg='white', width=450, height=45, padx=3, pady=3)
#btm_frame2 = Frame(root, bg='lavender', width=450, height=60, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")
btm_frame.grid(row=3, sticky="ew")
#btm_frame2.grid(row=4, sticky="ew")


# create the widgets for the top frame -------------------
topic="Chemistry"
main_topic = Label(top_frame, bg='white', text = f"Topic: {topic}",font=('Helvetica', 15))
sub_topic = Label(top_frame, bg='white', text = question_num_count,font=('Helvetica', 11))

#width_label = Label(top_frame, text='Width:')
#length_label = Label(top_frame, text='Length:')



# button widget


 

# layout the widgets in the top frame
main_topic.grid(row=0, columnspan=3)
sub_topic.grid(row=1, column=0)


#length_label.grid(row=1, column=2)
#entry_W.grid(row=1, column=1)
#entry_L.grid(row=1, column=3)

# create the center widgets

'''

'''    

center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

ctr_left = Frame(center, bg='white', width=400, height=190)
ctr_mid = Frame(center, bg='#d3dded', height=190, padx=3, pady=3)
#ctr_right = Frame(center, bg='green', width=100, height=190, padx=3, pady=3)


#question="Your cooperative society need a professional software application to store and manage your transaction record as your record grows and data operation and retrieval becomes more complex and difficult with Microsoft excel spreadsheet."

lbl_question = tk.Label(ctr_left, bg='white',  text =question, wraplength=400, justify="left")
lbl_question.grid(row=0, column=0)    



#---------------------------- Objects in the (center frame- ctr_mid) --------------------------------
lbl_instruction = tk.Label(ctr_mid, bg='#d3dded',  font=('Helvetica', 11))
lbl_instruction.grid(row=2, column=1)

check = IntVar()
#check2 = tk.IntVar()
#check3 = tk.IntVar()
#check4 = tk.IntVar()

# option A ---------------------------------------------------
r1_lbl = tk.Label(ctr_mid, bg='#d3dded', wraplength=200, anchor="w", justify="left")
r1_lbl.grid(row=3, column=1, stick="nsew")

# option B label ---------------------------------------------------
r2_lbl = tk.Label(ctr_mid, bg='#d3dded', wraplength=200, anchor="w", justify="left")
r2_lbl.grid(row=4, column=1, stick="nsew")

# option C label ---------------------------------------------------
r3_lbl = tk.Label(ctr_mid, bg='#d3dded', wraplength=200,  anchor="w", justify="left")
r3_lbl.grid(row=5, column=1, stick="nsew")


# option D lable---------------------------------------------------
r4_lbl = tk.Label(ctr_mid, bg='#d3dded', wraplength=200, anchor="w", justify="left")
r4_lbl.grid(row=6, column=1, stick="nsew")


ctr_left.grid(row=0, column=0, sticky="ns")

#if count > 0:
    #ctr_mid.grid(row=0, column=1, sticky="nsew", text="Hello")
    #ctr_mid.grid_forget()
#else:   
ctr_mid.grid(row=0, column=1, sticky="nsew")


#ctr_right.grid(row=0, column=2, sticky="ns")

#b1 = Button(ctr_mid, text = "Previous")
#b2 = Button(ctr_mid, text = "Next")

  

#b1 = Button(btm_frame, text = "Previous", command=lambda:loop_question())
#b1 = Button(btm_frame, text = "Previous")
#b2 = Button(btm_frame, text = "Next", command=loop_question())


b2 = Button(btm_frame, text = "Next", command=lambda:loop_question())

#b2 = Button( text = "Next", command=lambda:loop_question())


#b1.grid(row = 0, column = 0, sticky="ns")
b2.grid(row = 10, column = 3, sticky="nsew")

#selection = "You selected the option " + str(check.get())
#label.config(text = selection)

root.mainloop()