# www.plus2net.com
# download updated script at https://www.plus2net.com/python/tkinter-sqlite-insert.php

#print("Opened database successfully");
import tkinter  as tk 
#from tkinter import * 
from tkinter import ttk, messagebox 

from database import connect_db
my_conn = connect_db()

#def create_test():
#class SecondWindow(tk.Toplevel):


import cbt_result_list, cbt_mainboard_start_test



#global loginid
#loginid = ""


def donothing():
   x = 0

class AllTest(tk.Toplevel):

    

    def __init__(self,master, *args, title="Test Mainboard", **kwargs):   
        super().__init__(*args, master, **kwargs)

        #global loginid
        

        #print (loginid)
        #self = tk.Tk()
        #self.geometry("600x300") 
        self.title(title)

        w = self.winfo_reqwidth()
        h = self.winfo_reqheight()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.geometry('+%d+%d' % (x, y))

        # Create GUI elements
        self.task_label = tk.Label(self, text="Test Record")
        self.task_label.pack()

        #self.task_entry = tk.Entry(self)
        #self.task_entry.pack()

        # added **kwargs
   


        #self.add_button = tk.Button(self, text="Add", command=donothing)
        #self.add_button.pack()

        #scrollbar = tk.Scrollbar(self, orient="vertical")
        #self.record_listbox = tk.Listbox(self, width=50, height=20, yscrollcommand=scrollbar.set)
        #scrollbar.pack(side="right", fill="y")


        self.treev = ttk.Treeview(self, selectmode ='browse') 
        self.treev.pack(side='left',expand=True, fill='both') 

        verscrlbar = ttk.Scrollbar(self,  
                           orient ="vertical",  
                           command = self.treev.yview) 
  
        verscrlbar.pack(side ='right', fill ='y')   
        self.treev.configure(yscrollcommand = verscrlbar.set) 

        self.treev["columns"] = ('1', '2', '3', '4', '5') 

        self.treev['show'] = 'headings'
  
        self.treev.column("1", width = 90, anchor ='c') 
        self.treev.column("2", width = 90, anchor ='c') 
        self.treev.column("3", width = 90, anchor ='c') 
        self.treev.column("4", width = 90, anchor ='c') 
        self.treev.column("5", width = 90, anchor ='c') 


        self.treev.heading("1", text ="ID") 
        self.treev.heading("2", text ="Names")
        self.treev.heading("3", text ="Class")
        self.treev.heading("4", text ="Num. Questions") 
        self.treev.heading("5", text ="My Attempts") 

        #lb.pack(side="left",fill="both", expand=True)
        '''
        self.h1 = tk.Button(self, text="Title 1   ", command=donothing)
        self.h1.pack()
        self.h2 = tk.Button(self, text="Title 1   ", command=donothing)
        self.h2.pack(side="top")
        '''
        #self.record_listbox.pack(side="left",fill="both", expand=True)

        self.delete_button = tk.Button(self, text="Take Test", command=self.test_start)
        self.delete_button.pack()

        self.edit_button = tk.Button(self, text="My Result", command=self.test_result)
        self.edit_button.pack()
        
        self.edit_button = tk.Button(self, text="Refresh", command=self.load_record)
        self.edit_button.pack()

        self.load_record()
    
   
    def load_record(self):
        #self.record_listbox.delete(0, tk.END)
        #self.treev.delete(0, tk.END)

        rec = my_conn.execute("SELECT * FROM cbt_test")
        record = rec.fetchall()

        self.treev.delete(*self.treev.get_children())

        for row in record:
             

            rec_id = row[0]
            rec_test_name = row[1].strip()
            rec_class_name = row[2]
            #rec_status = row[3]
            rec_status=0
            #count_question=0

            #count number of questions....
            rec = my_conn.execute('SELECT * FROM cbt_questions WHERE test_id=?', (rec_id,))
            count_question = len(rec.fetchall())
            #count_question = rec.rowcount

            #number of attempts of login user
            loginid = self.master.loginid
            batch_sql=(f"SELECT batch_number FROM cbt_test_score WHERE user_id={loginid} AND test_id={rec_id} ORDER By id")
            batch_query = my_conn.execute(batch_sql)           
            batch_record = batch_query.fetchall()
            for batch_row in batch_record:
                rec_status = batch_row[0]
             
            ''' Use for login
            my_conn.execute('SELECT * FROM cbt_questions WHERE test_id=?', (rec_id,))
            row = my_conn.fetchone()
            if row is None:
                raise ValueError('No such user found')

            result = "Name = {}, Password = {}".format(row["username"], row["password"])
            '''

            self.treev.insert("", 'end', values =(rec_id, rec_test_name, rec_class_name, count_question, rec_status)) 


    def refresh(self):
        #self.weight_entry.delete(0, "end")
        self.treev.delete("0", "end")

    

    def test_start(self):
        # Get selected item to Edit
        selected_item = self.treev.selection()
        if selected_item:    
            sel_id = self.treev.item(selected_item)['values'][0]  

            number_of_questions = self.treev.item(selected_item)['values'][3] 
            if number_of_questions==0:
                messagebox.showwarning("Warning", "Selected test has no question.")
            else:   
                #print (sel_id)
                loginid = self.master.loginid
                self.login_id=loginid
                self.val_id=sel_id
                cbt_mainboard_start_test.Start(self)
                #cbt_edit_test.EditTest(data=sel_id)
        else:
            messagebox.showwarning("Warning", "Please select a test to add question.")

    
    def test_result(self):
        # Get selected item to Edit
        selected_item = self.treev.selection()
        if selected_item:    
            sel_id = self.treev.item(selected_item)['values'][0]    
            #print (sel_id)

            loginid = self.master.loginid

            self.test_id=sel_id #test id
            self.login_id=loginid
            #self.test_id=val_id
            self.batch_num=self.treev.item(selected_item)['values'][4] 

            cbt_result_list.List(self)
            #cbt_edit_test.EditTest(data=sel_id)
        else:
            messagebox.showwarning("Warning", "Please select a test to add question.")

   
    
    

   
if __name__ == "__main__":
    self = AllTest()
    self.mainloop()     
