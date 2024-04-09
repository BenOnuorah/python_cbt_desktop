# www.plus2net.com
# download updated script at https://www.plus2net.com/python/tkinter-sqlite-insert.php
import sqlite3
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

my_conn = sqlite3.connect(dir_path+'/cbt_app.db')

#print("Opened database successfully");
import tkinter  as tk 
from tkinter import * 

import re

#def create_test():
#class SecondWindow(tk.Toplevel):

def donothing():
   x = 0

class ManageTest(tk.Toplevel):
    def __init__(self, *args, title="Create new test", **kwargs):   
        super().__init__(*args, **kwargs)

        #self = tk.Tk()
        self.geometry("600x300") 
        self.title(title)

        # Create GUI elements
        self.task_label = tk.Label(self, text="Test Record")
        self.task_label.pack()

        #self.task_entry = tk.Entry(self)
        #self.task_entry.pack()

        #self.add_button = tk.Button(self, text="Add", command=donothing)
        #self.add_button.pack()

        scrollbar = tk.Scrollbar(self, orient="vertical")
        self.record_listbox = tk.Listbox(self, width=50, height=20, yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        #lb.pack(side="left",fill="both", expand=True)
        '''
        self.h1 = tk.Button(self, text="Title 1   ", command=donothing)
        self.h1.pack()
        self.h2 = tk.Button(self, text="Title 1   ", command=donothing)
        self.h2.pack(side="top")
        '''
        self.record_listbox.pack(side="left",fill="both", expand=True)

        self.delete_button = tk.Button(self, text="Delete ", command=donothing)
        self.delete_button.pack()

        self.edit_button = tk.Button(self, text="Edit   ", command=donothing)
        self.edit_button.pack()

        self.load_record()
    
   
    def load_record(self):
        self.record_listbox.delete(0, tk.END)
        rec = my_conn.execute("SELECT * FROM cbt_test")
        record = rec.fetchall()

        self.record_listbox.insert(tk.END, "ID    TEST NAME         CLASS NAME    STATUS")

        for row in record:
            rec_id = row[0]
            rec_test_name = row[1].strip()

            #s = rec_test_name+" \n \t \t\t \t "

            #rec_test_name = s
            rec_class_name = row[2]
            rec_status = row[3]
            #self.record_listbox.insert(tk.END, row[0], row[1], row[2])
            self.record_listbox.insert(tk.END, f"{rec_id}     {rec_test_name}     {rec_class_name}       {rec_status}")
            #self.record_listbox.insert("end", "item #%s" % row)
            
            
    #--------------------------------------------------------------

    #my_str.set("Output")
    '''
    def add_data():
        flag_validation=True # set the flag 

        test_name=t1.get("1.0",END) # read name
        class_name=options.get()    # read class
        #my_mark=t3.get("1.0",END) # read mark
        test_status=radio_v.get()   # read gender 
        # length of my_name , my_class and my_gender more than 2 
        if(len(test_name) < 2 or len(class_name)<2  or len(test_status) < 2 ):
                flag_validation=False 
        #try:
        #    val = int(my_mark) # checking mark as integer 
        #except:
        #    flag_validation=False 
        



        if(flag_validation):
            my_str.set("Adding data...")
            try:
                #print("Connected to database successfully")
                my_data=(None,test_name,class_name,test_status)
                my_query="INSERT INTO cbt_test values(?,?,?,?)"
                my_conn.execute(my_query,my_data)
                my_conn.commit()               
               
                l5.grid() 
                l5.config(fg='green') # foreground color 
                l5.config(bg='white') # background color 

                #my_str.set("ID:" + str(id[0]))
                my_str.set("Recorded added")

                l5.after(3000, lambda: l5.grid_remove() )
                t1.delete('1.0',END)  # reset the text entry box
                #t3.delete('1.0',END)  # reset the text entry box   

            except sqlite3.Error as my_error:
                l5.grid() 
                #return error
                l5.config(fg='red')   # foreground color
                l5.config(bg='yellow') # background color
                print(my_error)
                my_str.set(my_error)    

        else:
            l5.grid() 
            l5.config(fg='red')   # foreground color
            l5.config(bg='yellow') # background color
            my_str.set("Please enter ")
            l5.after(3000, lambda: l5.grid_remove() )

       '''

if __name__ == "__main__":
    self = ManageTest()
    self.mainloop()     
