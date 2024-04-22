#print("Opened database successfully");
from doctest import master
import tkinter  as tk 
from tkinter import ttk, messagebox
from tkinter import * 

from database import connect_db
my_conn = connect_db()


import cbt_result_detail

size_all = 30
font_all='Arial 10'



class List(tk.Toplevel):
  def __init__(self, master, *args, title="Result List", **kwargs):   
    super().__init__(*args, master, **kwargs)

    #--------------------------------------
    test_id = self.master.test_id
    login_id = self.master.login_id
    batch_num = self.master.batch_num
    
    rec =  my_conn.execute("SELECT * FROM cbt_test WHERE id="+str(test_id)+"")
    record = rec.fetchone()
    rec_id = record[0]
    topic = record[1].strip()
    #---------------------------------

    self.title(title)

    w = self.winfo_reqwidth()
    h = self.winfo_reqheight()
    ws = self.winfo_screenwidth()
    hs = self.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    self.geometry('+%d+%d' % (x, y))

    # Create GUI elements
    self.task_label = tk.Label(self, text="Test List")
    self.task_label.pack()

   
    self.treev = ttk.Treeview(self, selectmode ='browse') 
    self.treev.pack(side='left',expand=True, fill='both') 

    verscrlbar = ttk.Scrollbar(self,  
                        orient ="vertical",  
                        command = self.treev.yview) 

    verscrlbar.pack(side ='right', fill ='y')   
    self.treev.configure(yscrollcommand = verscrlbar.set) 

    #self.treev["columns"] = ('1', '2', '3') 
    self.treev["columns"] = ('1') 

    self.treev['show'] = 'headings'

    self.treev.column("1", width = 90, anchor ='c') 
    #self.treev.column("2", width = 90, anchor ='c') 
    #self.treev.column("3", width = 90, anchor ='c') 
   


    self.treev.heading("1", text ="Attemp Num.") 
    #self.treev.heading("2", text ="Total Correct")
    #self.treev.heading("3", text ="Total Wrong")
    

    #lb.pack(side="left",fill="both", expand=True)
    '''
    self.h1 = tk.Button(self, text="Title 1   ", command=donothing)
    self.h1.pack()
    self.h2 = tk.Button(self, text="Title 1   ", command=donothing)
    self.h2.pack(side="top")
    '''
    

    self.detail_button = tk.Button(self, text="Detail", command=self.load_detail)
    self.detail_button.pack()
    
    self.refresh_button = tk.Button(self, text="Refresh", command=self.load_record)
    self.refresh_button.pack()

    self.load_record()


  def load_record(self):
      #self.record_listbox.delete(0, tk.END)
      #self.treev.delete(0, tk.END)

      test_id = self.master.test_id
      login_id = self.master.login_id
      batch_num = self.master.batch_num
      rec = my_conn.execute(f"SELECT batch_number, your_answer, id, question_id FROM cbt_test_score WHERE user_id={login_id} AND test_id={test_id} ORDER By id DESC")
      record = rec.fetchall()

      self.treev.delete(*self.treev.get_children())

      last_num=0  
      total_correct=0
      
      for row in record:
          res_batch_number = row[0]
          res_your_answer = row[1]
          res_id = row[2]
          question_id = row[3]

          '''
          #your_choice=""
          if res_your_answer == '1':
            #your_choice = f"A. ({res_id}) {ques_option1}"
          elif res_your_answer == '2':  
            #your_choice = f"B. {ques_option2}"
          elif res_your_answer == '3':  
            #your_choice = f"C. {ques_option3}"
          elif res_your_answer == '4':  
            #your_choice = f"D. {ques_option4}" 
          '''

          #---------------------------------
          
          rec5 = my_conn.execute(f"SELECT right_option FROM cbt_questions WHERE test_id={test_id} AND id={question_id} ")
          record5 = rec5.fetchall()

          for row5 in record5:
            right_option = row5[0]

            if right_option == res_your_answer:
                total_correct=total_correct+1

          #self.treev.insert("", 'end', values =(res_batch_number, total_correct, res_id))

          if last_num != res_batch_number:
                last_num=res_batch_number  
                #self.treev.insert("", 'end', values =(res_batch_number, total_correct, res_id))
                self.treev.insert("", 'end', values =(res_batch_number))
         

           


  def refresh(self):
      #self.weight_entry.delete(0, "end")
      self.treev.delete("0", "end")


  
  def load_detail(self):
      # Get selected item to Edit
      selected_item = self.treev.selection()
      if selected_item:    
            sel_id = self.treev.item(selected_item)['values'][0]  
            #sel_id = self.treev.item(selected_item)['values'][0]  
            #print (sel_id)
            loginid = self.master.login_id

            self.login_id=loginid
            self.val_id=sel_id
            self.test_id = self.master.test_id

            cbt_result_detail.Detail(self)
            #cbt_edit_test.EditTest(data=sel_id)
      else:
          messagebox.showwarning("Warning", "Please select a record")

      
     
      
      

if __name__ == "__main__":
    self = List()
    self.mainloop()
    