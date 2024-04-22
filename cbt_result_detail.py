#print("Opened database successfully");
from doctest import master
import tkinter  as tk 
from tkinter import ttk, messagebox
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
    #self.geometry('+%d+%d' % (x, y))

    self.geometry("600x250")
   
    # Create the main window
    
   
    loginid = self.master.login_id
    batch_num = self.master.val_id #batch num
    test_id = self.master.test_id
    

    '''
    loginid = 1
    batch_num=5
    test_id=5
    '''
    print (f"loginid{loginid}, batch_num{batch_num}, test_id{test_id}")

    

    t= tk.Label(self, text = title,font=('Helvetica', 13))
    t.pack(side = TOP)

   

    rec1 = my_conn.execute(f"SELECT * FROM cbt_test WHERE id={test_id}")
    record1 = rec1.fetchone()
    test_name = record1[1]
    class_name = record1[2]
    pass_percent = record1[4]

    lbl1 = tk.Label(self, text = f"Subject: {test_name}", width=size_all, font=(font_all))   
    #blank_lbl1 = tk.Label(self, text = "\n")    
    lbl1.pack()   
    #blank_lbl1.pack()
    
    
   

    
    
    
    #--------------------------------------------------------------

    self.treev = ttk.Treeview(self, selectmode ='browse') 
    

    verscrlbar = ttk.Scrollbar(self,  orient ="vertical",  command = self.treev.yview) 

    verscrlbar.pack(side ='right', fill ='y')   
    self.treev.configure(yscrollcommand = verscrlbar.set) 

    self.treev["columns"] = ('1', '2', '3', '4', '5') 

    self.treev['show'] = 'headings'

    self.treev.column("1", width = 90, anchor ='c') 
    self.treev.column("2", width = 90, anchor ='c') 
    self.treev.column("3", width = 90, anchor ='c') 
    self.treev.column("4", width = 90, anchor ='c') 
    self.treev.column("5", width = 90, anchor ='c') 


    self.treev.heading("1", text ="Question") 
    self.treev.heading("2", text ="Answer")
    self.treev.heading("3", text ="Your Choice")
    self.treev.heading("4", text ="Result") 
    self.treev.heading("5", text ="Explanation") 

    count=0
    total_correct=0
    rec5 = my_conn.execute(f"SELECT id, question, question1, question2, question3, question4, right_option, explanation FROM cbt_questions WHERE test_id={test_id} ORDER By id")
    record5 = rec5.fetchall()
    #self.treev.delete(*self.treev.get_children())
    for row in record5:
        count=count+1
        ques_id = row[0]
        ques_question = row[1].strip()
        ques_option1 = row[2]
        ques_option2 = row[3]
        ques_option3 = row[4]
        ques_option4 = row[5]
        ques_correct = row[6]
        ques_explain = row[7]

        answer=""
        if ques_correct == '1':
          answer = f"A. {ques_option1}"
        elif ques_correct == '2':  
          answer = f"B. {ques_option2}"
        elif ques_correct == '3':  
          answer = f"C. {ques_option3}"
        elif ques_correct == '4':  
          answer = f"D. {ques_option4}"    

        #--------------------- User Answer ------------------------------
        
        rec = my_conn.execute(f"SELECT * FROM cbt_test_score WHERE user_id={loginid} AND test_id={test_id} AND batch_number={batch_num} AND question_id={ques_id} ORDER By id")
        record = rec.fetchall()
        for row1 in record: 
          res_id = row1[0]
          res_user_id = row1[1]
          res_question_id = row1[2]
          res_test_id = row1[3]
          res_your_answer = row1[4]
          res_batch_id = row1[5]

          your_choice=""
          if res_your_answer == '1':
            your_choice = f"A. {ques_option1}"
          elif res_your_answer == '2':  
            your_choice = f"B. {ques_option2}"
          elif res_your_answer == '3':  
            your_choice = f"C. {ques_option3}"
          elif res_your_answer == '4':  
            your_choice = f"D. {ques_option4}"  

          
        #--------------------------------------------------------------
        if ques_correct == res_your_answer:
          result = "Correct"
          total_correct=total_correct+1
        else:
          result = "Wrong"  

        #your_choice = "Here"
       
        explain = ques_explain

        self.treev.insert("", 'end', values =(ques_question, answer, your_choice,result, explain)) 


  #===============================================================
    total_questions=count 
    #total_correct=1
    #total_wrong=0
    #pass_percent=50 #50%
    total_wrong = total_questions-total_correct


    achived_percent = (total_correct / total_questions) * 100

   

    lbl1 = tk.Label(self, text = f"Total Question: {total_questions}") 
    lbl1.pack() 

    lbl2 = tk.Label(self, text = f"Total Correct: {total_correct}") 
    lbl2.pack()   

    lbl3 = tk.Label(self, text = f"Total Wrong: {total_wrong}") 
    lbl3.pack() 

    lbl4 = tk.Label(self, text = f"Pass Percent : {pass_percent}%") 
    lbl4.pack() 

    lbl5 = tk.Label(self, text = f"Achieved Percent : {achived_percent}%") 
    lbl5.pack()

    if achived_percent < pass_percent:        
        lbl6 = tk.Label(self, text = "FAIL", font=(40), bg='#fff', fg='red') 
        lbl6.pack()
    else:
        lbl6 = tk.Label(self, text = "PASS", font=(40), bg='#fff', fg='blue') 
        lbl6.pack()
     
    #b= tk.Button(self, text = "Login", command = lambda: validate_login())
    #b.pack()
    self.treev.pack(side='left',expand=True, fill='both') 

    
    
    

if __name__ == "__main__":
    self = Detail()
    self.mainloop()
    