# www.plus2net.com
# download updated script at https://www.plus2net.com/python/tkinter-sqlite-insert.php
import sqlite3
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

my_conn = sqlite3.connect(dir_path+'/cbt_app.db')

#print("Opened database successfully");
import tkinter  as tk 
#from tkinter import * 
from tkinter import ttk, messagebox 


#def create_test():
#class SecondWindow(tk.Toplevel):

import cbt_edit_test, cbt_add_question, cbt_manage_questions


def donothing():
   x = 0

class ManageTest(tk.Toplevel):

    

    def __init__(self,*args, title="Create new test", **kwargs):   
        super().__init__(*args, **kwargs)

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
        self.treev.heading("4", text ="Status") 
        self.treev.heading("5", text ="Num. Questions") 

        #lb.pack(side="left",fill="both", expand=True)
        '''
        self.h1 = tk.Button(self, text="Title 1   ", command=donothing)
        self.h1.pack()
        self.h2 = tk.Button(self, text="Title 1   ", command=donothing)
        self.h2.pack(side="top")
        '''
        #self.record_listbox.pack(side="left",fill="both", expand=True)

        self.delete_button = tk.Button(self, text="Delete", command=self.delete_task)
        self.delete_button.pack()

        self.edit_button = tk.Button(self, text="Edit", command=self.edit)
        self.edit_button.pack()

        self.add_question_button = tk.Button(self, text="Add Question", command=self.add_question)
        self.add_question_button.pack()
        
        self.manage_question_button = tk.Button(self, text="Manage Questions", command=self.manage_question)
        self.manage_question_button.pack()

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
            rec_status = row[3]

            #count_question=0

            #count number of questions....
            rec = my_conn.execute('SELECT * FROM cbt_questions WHERE test_id=?', (rec_id,))
            count_question = len(rec.fetchall())
            #count_question = rec.rowcount

            ''' Use for login
            my_conn.execute('SELECT * FROM cbt_questions WHERE test_id=?', (rec_id,))
            row = my_conn.fetchone()
            if row is None:
                raise ValueError('No such user found')

            result = "Name = {}, Password = {}".format(row["username"], row["password"])
            '''

            self.treev.insert("", 'end', values =(rec_id, rec_test_name, rec_class_name, rec_status, count_question)) 


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

            my_conn.execute("DELETE FROM cbt_test WHERE id="+str(sel_id)+" ")
            my_conn.commit()
        
            self.treev.delete(selected_item)
        else:
            messagebox.showwarning("Warning", "Please select a record to delete.")

   

    def add_question(self):
        # Get selected item to Edit
        selected_item = self.treev.selection()
        if selected_item:    
            sel_id = self.treev.item(selected_item)['values'][0]    
            #print (sel_id)

            self.val_id=sel_id
            cbt_add_question.AddQuestion(self)
            #cbt_edit_test.EditTest(data=sel_id)
        else:
            messagebox.showwarning("Warning", "Please select a test to add question.")

    def manage_question(self):
        # Get selected item to Edit
        selected_item = self.treev.selection()
        if selected_item:    
            sel_id = self.treev.item(selected_item)['values'][0]    
            #print (sel_id)

            self.val_id=sel_id
            cbt_manage_questions.ManageQuestion(self)           
        else:
            messagebox.showwarning("Warning", "Please select a test to add question.")

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
    def OnDoubleClick(self):
        # First check if a blank space was selected

        
        entryIndex = self.treev.focus()
        if '' == entryIndex: return

        # Set up window
        tk.Toplevel()
        self.title("Edit Entry")
        self.attributes("-topmost", True) #-alpha, -topmost, -zoomed, -fullscreen, or -type

        ####
        # Set up the window's other attributes and geometry
        ####

        # Grab the entry's values
        for child in self.treev.get_children():
            if child == entryIndex:
                values = self.treev.item(child)["values"]
                break

        col1Lbl = tk.Label(self, text = "Value 1: ")
        col1Ent = tk.Entry(self)
        col1Ent.insert(0, values[0]) # Default is column 1's current value
        col1Lbl.grid(row = 0, column = 0)
        col1Ent.grid(row = 0, column = 1)

        col2Lbl = tk.Label(self, text = "Value 2: ")
        col2Ent = tk.Entry(self)
        col2Ent.insert(0, values[1]) # Default is column 2's current value
        col2Lbl.grid(row = 0, column = 2)
        col2Ent.grid(row = 0, column = 3)

        col3Lbl = tk.Label(self, text = "Value 3: ")
        col3Ent = tk.Entry(self)
        col3Ent.insert(0, values[2]) # Default is column 3's current value
        col3Lbl.grid(row = 0, column = 4)
        col3Ent.grid(row = 0, column = 5)

        def UpdateThenDestroy():
            if ConfirmEntry(self.treev, col1Ent.get(), col2Ent.get(), col3Ent.get()):
                self.destroy()

        okButt = tk.Button(self, text = "Ok")
        okButt.bind("<Button-1>", lambda e: UpdateThenDestroy())
        okButt.grid(row = 1, column = 4)

        canButt = tk.Button(self, text = "Cancel")
        canButt.bind("<Button-1>", lambda c: self.destroy())
        canButt.grid(row = 1, column = 5)

        #-----------    
        def ConfirmEntry(treeView, entry1, entry2, entry3):
            ####
            # Whatever validation you need
            ####

            # Grab the current index in the tree
            currInd = treeView.index(treeView.focus())

            # Remove it from the tree
            #DeleteCurrentEntry(treeView)

            # Put it back in with the upated values
            treeView.insert('', currInd, values = (entry1, entry2, entry3))

            return True
    '''

if __name__ == "__main__":
    self = ManageTest()
    self.mainloop()     
