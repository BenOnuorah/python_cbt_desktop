
#print("Opened database successfully");
import tkinter  as tk 
#from tkinter import * 
from tkinter import ttk, messagebox 

from database import connect_db
my_conn = connect_db()


#def create_test():
#class SecondWindow(tk.Toplevel):

import cbt_edit_test, cbt_add_question


def donothing():
   x = 0

class ManageQuestion(tk.Toplevel):

    def __init__(self, master, *args, title="Manage Questions", **kwargs):   
        super().__init__(*args, master,  **kwargs)
 
        val_id = self.master.val_id   

        rec =  my_conn.execute("SELECT * FROM cbt_test WHERE id="+str(val_id)+" ")
        record = rec.fetchone()

        rec_id = record[0]
        rec_test_name = record[1].strip()
 

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

        self.t= tk.Label(self, text = f"Manage {rec_test_name} Questions")
        self.t.pack()

        #self.task_label = tk.Label(self, text="Test Record")
        #self.task_label.pack()

      


        self.treev = ttk.Treeview(self, selectmode ='browse') 
        self.treev.pack(side='left',expand=True, fill='both') 

        verscrlbar = ttk.Scrollbar(self,  
                           orient ="vertical",  
                           command = self.treev.yview) 
  
        verscrlbar.pack(side ='right', fill ='y')   
        self.treev.configure(yscrollcommand = verscrlbar.set) 

        self.treev["columns"] = ('1', '2', '3', '4', '5', '6', '7', '8') 

        self.treev['show'] = 'headings'
  
        self.treev.column("1", width = 90, anchor ='c') 
        self.treev.column("2", width = 90, anchor ='c') 
        self.treev.column("3", width = 90, anchor ='c') 
        self.treev.column("4", width = 90, anchor ='c') 
        self.treev.column("5", width = 90, anchor ='c')
        self.treev.column("6", width = 90, anchor ='c')
        self.treev.column("7", width = 90, anchor ='c')
        self.treev.column("8", width = 90, anchor ='c') 


        self.treev.heading("1", text ="ID") 
        self.treev.heading("2", text ="Question")
        self.treev.heading("3", text ="Opt1")
        self.treev.heading("4", text ="Opt2") 
        self.treev.heading("5", text ="Opt3") 
        self.treev.heading("6", text ="Opt4") 
        self.treev.heading("7", text ="Correct Opt") 
        self.treev.heading("8", text ="Explain") 

      
        def donothing():
            x = 0

        self.delete_button = tk.Button(self, text="Delete", command=self.delete_task)
        self.delete_button.pack()

        self.edit_button = tk.Button(self, text="Edit", command=donothing)
        self.edit_button.pack()
        
        self.edit_button = tk.Button(self, text="Refresh", command=self.load_record(val_id))
        self.edit_button.pack()

        self.load_record(val_id)
    
       
    def load_record(self, val_id):
            sel_id=val_id 

            rec = my_conn.execute("SELECT * FROM cbt_questions WHERE test_id="+str(sel_id)+" ")
            #rec = my_conn.execute('SELECT * FROM cbt_questions')
            record = rec.fetchall()

            self.treev.delete(*self.treev.get_children())

            for row in record:
                

                quest_id = row[0]
                rec_question = row[2].strip()
                rec_opt1 = row[3]
                rec_opt2 = row[4]
                rec_opt3 = row[5]
                rec_opt4 = row[6]
                rec_correct = row[7]
                rec_explain = row[8]

            

                self.treev.insert("", 'end', values =(quest_id, rec_question, rec_opt1, rec_opt2, rec_opt3, rec_opt4, rec_correct, rec_explain)) 


    def refresh(self):
        #self.weight_entry.delete(0, "end")
        self.treev.delete("0", "end")

    def delete_task(self):
        
            selected_item = self.treev.selection()
        
            #for selected_item in selected_items:
                #for i in range(len(self.tasks)):

            if selected_item:    
                sel_id = self.treev.item(selected_item)['values'][0]    
                print (sel_id)

                my_conn.execute("DELETE FROM cbt_questions WHERE id="+str(sel_id)+" ")
                my_conn.commit()
            
                self.treev.delete(selected_item)
            else:
                messagebox.showwarning("Warning", "Please select a record to delete.")

    

    
    def edit(self):
            # Get selected item to Edit
            selected_item = self.treev.selection()
            if selected_item:    
                sel_id = self.treev.item(selected_item)['values'][0]    
                #print (sel_id)

                self.val_id=sel_id
                
                #cbt_edit_test.EditTest(sel_id)
                
                #lambda: cbt_edit_test.EditTest(sel_id)

                #self.rec_id = cbt_edit_test.EditTest(sel_id)
                #self.record_id = 
                #test="Hello"
                #cbt_edit_test.EditTest(self.edit, test)
                #cbt_edit_test.EditTest(self.sel_id)

                #--------------

                #self.edit(cbt_edit_test.EditTest, sel_id)
                #self.master.switch_frame(cbt_edit_test.EditTest, sel_id)


                cbt_edit_test.EditTest(self)

                #cbt_edit_test.EditTest(data=sel_id)
            else:
                messagebox.showwarning("Warning", "Please select a record to edit.")
        
    
    #my_str.set("Output")
    

'''    
if __name__ == "__main__":
    self = ManageQuestion()
    self.mainloop()     
'''