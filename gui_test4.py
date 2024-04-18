import tkinter as tk
from tkinter import messagebox
from tkinter import *

from database import connect_db
my_conn = connect_db()


root = Tk()
root.title('Question')


global count
global limit
global question_id


count = 0
question_num_count=1
question_num_text=""
limit=0
question_id=""




rec =  my_conn.execute("SELECT * FROM cbt_test WHERE id=1")
record = rec.fetchone()
rec_id = record[0]
rec_test_name = record[1].strip()
#question=rec_test_name



cursor = my_conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS cbt_test_score (id INTEGER PRIMARY KEY, 
user_id TEXT, question_id TEXT, test_id TEXT, your_answer TEXT, batch_number TEXT)''')
my_conn.commit()


#-------------------------------------
sql_query="SELECT * FROM cbt_questions WHERE test_id=? ORDER By id LIMIT 0, 1"
rec = my_conn.execute(sql_query,(rec_id,))
record = rec.fetchall()
#lbl_instruction["text"]="Select the correct option"
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
    que1 = (f"A. {rec_opt1}")
    que2 = (f"B. {rec_opt2}")
    que3 = (f"C. {rec_opt3}")
    que4 = (f"D. {rec_opt4}")
    question_id=quest_id

    question_num_text = f"Question :{question_num_count}"
#--------------------------------------------------------------------------------

#when the next button is clicked...
def loop_question():
        global count
        global limit       
        global question_num_count
        global question_id
        
        count = count+1
        limit=limit+1

        question_num_count=question_num_count+1

        if count == 1:
            sub_topic["text"] = f"Question :{question_num_count}"

            #enter the first one
            selected_option = check.get()
            user_id=1
            #question_id=quest_id
            test_id=rec_id
            batch_number=1
            your_answer = selected_option

            cursor.execute("INSERT INTO cbt_test_score (user_id, question_id, test_id, your_answer, batch_number) VALUES (?,?,?,?,?)", (user_id, question_id, test_id, your_answer, batch_number))
            my_conn.commit()

            # load next question-------------------            
            sql_query="SELECT * FROM cbt_questions WHERE test_id=? ORDER By id LIMIT ?, 1"
            rec = my_conn.execute(sql_query,(rec_id, limit))           
            record = rec.fetchall()
            for row in record:
                quest_id = row[0]
                rec_question = row[2].strip()
                rec_opt1 = row[3]
                rec_opt2 = row[4]
                rec_opt3 = row[5]
                rec_opt4 = row[6]               
                question=rec_question
           
            #--------------------------------------------------
            #     
                lbl_question["text"] = question  

                r1_lbl["text"] = (f"A. {rec_opt1}")
                r2_lbl["text"] = (f"B. {rec_opt2}")
                r3_lbl["text"] = (f"C. {rec_opt3}")
                r4_lbl["text"] = (f"D. {rec_opt4}")


                selected_option = check.get()
                msg = f"You selected the option {selected_option}"
                check.set(None)

                question_id=quest_id


        if count > 1:
            
            sub_topic["text"] = f"Question :{question_num_count}"

            selected_option = check.get()
            user_id=1
            #question_id=quest_id
            test_id=rec_id
            batch_number=1
            your_answer = selected_option

            
            cursor.execute("INSERT INTO cbt_test_score (user_id, question_id, test_id, your_answer, batch_number) VALUES (?,?,?,?,?)", (user_id, question_id, test_id, your_answer, batch_number))
            my_conn.commit()

            #print (count)
            #print (msg)

            # ------------------- Load question--------------------------------
                
            sql_query="SELECT * FROM cbt_questions WHERE test_id=? ORDER By id LIMIT ?, 1"
            rec = my_conn.execute(sql_query,(rec_id, limit))           
            record = rec.fetchall()
            for row in record:
                
                print (f"limit:{limit}")
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
               
                user_id=1
                question_id=quest_id
                test_id=rec_id
                batch_number=1
                your_answer = selected_option

        
        
        if len(record) == 0:                  
                root.destroy()
                messagebox.showinfo("Completed", "You have completed your test")
                #cbt_mainboard.AllTest()
                

           


root.geometry('{}x{}'.format(700, 450))

# create all of the main containers
top_frame = Frame(root, bg='white', width=450, height=50, pady=3)
center = Frame(root, bg='gray2', width=50, height=40, padx=3, pady=3)
btm_frame = Frame(root, bg='white', width=450, height=45, padx=3, pady=3)


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
sub_topic = Label(top_frame, bg='white', text=question_num_text,font=('Helvetica', 11))

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


center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

ctr_left = Frame(center, bg='white', width=400, height=190)
ctr_mid = Frame(center, bg='#d3dded', height=190, padx=3, pady=3)
#ctr_right = Frame(center, bg='green', width=100, height=190, padx=3, pady=3)


#question="Your cooperative society need a professional software application to store and manage your transaction record as your record grows and data operation and retrieval becomes more complex and difficult with Microsoft excel spreadsheet."

lbl_question = tk.Label(ctr_left, bg='white',  text=question, wraplength=400, justify="left")
lbl_question.grid(row=0, column=0)    



#---------------------------- Objects in the (center frame- ctr_mid) --------------------------------
lbl_instruction = tk.Label(ctr_mid, bg='#d3dded', text="Select the correct option", font=('Helvetica', 11))
lbl_instruction.grid(row=2, column=1)


check = IntVar()
#check2 = tk.IntVar()
#check3 = tk.IntVar()
#check4 = tk.IntVar()

# option A ---------------------------------------------------
r1_lbl = tk.Label(ctr_mid, bg='#d3dded', text=que1, wraplength=200, anchor="w", justify="left")
r1_lbl.grid(row=3, column=1, stick="nsew")

# option B label ---------------------------------------------------
r2_lbl = tk.Label(ctr_mid, bg='#d3dded', text=que2,  wraplength=200, anchor="w", justify="left")
r2_lbl.grid(row=4, column=1, stick="nsew")

# option C label ---------------------------------------------------
r3_lbl = tk.Label(ctr_mid, bg='#d3dded', text=que3,  wraplength=200,  anchor="w", justify="left")
r3_lbl.grid(row=5, column=1, stick="nsew")


# option D lable---------------------------------------------------
r4_lbl = tk.Label(ctr_mid, bg='#d3dded', text=que4,  wraplength=200, anchor="w", justify="left")
r4_lbl.grid(row=6, column=1, stick="nsew")

# option A radio ---------------------
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
b2 = Button(btm_frame, text = "Next", command=loop_question)

#b2 = Button(btm_frame, text = "Next", command=lambda:loop_question())

#b2 = Button( text = "Next", command=lambda:loop_question())


#b1.grid(row = 0, column = 0, sticky="ns")
b2.grid(row = 10, column = 3, sticky="nsew")

#selection = "You selected the option " + str(check.get())
#label.config(text = selection)

root.mainloop()