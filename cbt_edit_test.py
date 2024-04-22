# www.plus2net.com
# download updated script at https://www.plus2net.com/python/tkinter-sqlite-insert.php
from multiprocessing import Value

from database import connect_db
my_conn = connect_db()

#print("Opened database successfully");
import tkinter  as tk
from tkinter import messagebox 
from tkinter import * 

size_all = 30
font_all='Arial 15'

class EditTest(tk.Toplevel):
 def __init__(self, master, *args, title="Edit test", **kwargs):   
    super().__init__(*args, master,  **kwargs)

    #self.master = master 

    val_id = self.master.val_id

    
    rec =  my_conn.execute("SELECT * FROM cbt_test WHERE id="+str(val_id)+" ")
    record = rec.fetchone()

    rec_id = record[0]
    rec_test_name = record[1].strip()
    rec_class_name = record[2]
    rec_status = record[3]
    percentage = record[4]
    instruction = record[5]
   

    #print ("I am printing here "+ str(val_id))
    #print (rec_test_name)

   
    #self.geometry("600x300") 
    self.title(title)

    w = self.winfo_reqwidth()
    h = self.winfo_reqheight()
    ws = self.winfo_screenwidth()
    hs = self.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    self.geometry('+%d+%d' % (x, y))
    

    #self.geometry("600x250")
   
     
    
   
    t= tk.Label(self, text = "Edit test",font=('Helvetica', 16))
    t.pack(side = TOP)

    

    lbl1 = tk.Label(self, text = "Test Name", anchor="w", justify="left", width=size_all, font=(font_all))
    ent1 = tk.Entry(self, width=size_all, font=(font_all))    
    ent1.insert(0, rec_test_name) 
    blank_lbl1 = tk.Label(self, text = "\n")


    lbla = tk.Label(self, text = "Pass Percentage", anchor="w", justify="left", width=size_all, font=(font_all))
    enta = tk.Entry(self, width=size_all, font=(font_all))    
    enta.insert(0, percentage) 
    blank_lbla = tk.Label(self, text = "\n")


    lblb = tk.Label(self, text = "Instruction", anchor="w", justify="left", width=size_all, font=(font_all))
    entb = tk.Entry(self, width=size_all, font=(font_all))    
    entb.insert(0, instruction) 
    blank_lblb = tk.Label(self, text = "\n")


    lbl2 = tk.Label(self, text = "Class", anchor="w", justify="left", width=size_all, font=(font_all))
    #ent2 = tk.Entry(self, width=size_all, font=(font_all))
    #ent2.insert(0, rec_class_name) 
    #blank_lbl2 = tk.Label(self, text = "\n")
    
    lbl3 = tk.Label(self, text = "Status", anchor="w", justify="left", width=size_all, font=(font_all))
    ent3 = tk.Entry(self, width=size_all, font=(font_all))
    ent3.insert(0, rec_status) 
    blank_lbl3 = tk.Label(self, text = "\n")

    # add list box for selection of class
    options = StringVar(self)
    options.set("") # default value

    
    rec_cls = my_conn.execute("SELECT distinct(class_name) as class FROM cbt_class_name")
    #my_list = [r for r, in rec_cls] (working )
    #opt1 = OptionMenu(self, options, *my_list) (worling)


    process_menu=[]
    record_cls = rec_cls.fetchall()
    for row in record_cls:
        process_menu.append(row[0])
        #data.append(row[1]) 

    #opt1 = OptionMenu(self, options, "Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6")
    opt1 = OptionMenu(self, options, *process_menu)

    options.set(rec_class_name)

    opt1.config(width=40)
    blank_lbl4 = tk.Label(self, text = "\n")

    

    lbl1.pack()
    ent1.pack()
    blank_lbl1.pack()

    lbla.pack()
    enta.pack()
    blank_lbla.pack()

    lblb.pack()
    entb.pack()
    blank_lblb.pack()

    lbl3.pack()
    ent3.pack()
    blank_lbl3.pack()

    lbl2.pack()
    opt1.pack()
    blank_lbl4.pack()

    def donothing():
        x = 0

    b= tk.Button(self, text = "Edit", command = lambda: add_update())
    b.pack()
    #--------------------------------------------------------------


    def add_update():
        
            record_id=rec_id 
            test_name=ent1.get()            
            test_class=options.get()
            test_status=ent3.get()

            pass_percent=enta.get()
            instruct=entb.get()
            

            # read name
            #class_name=options.get()    # read class       
            #test_status=radio_v.get()   # read gender 

            print ("--------------")
            print (record_id)
            print (test_name)
            print (test_class)
            print (test_status)  

            #UPDATE messages SET name='$volume_title', detail='$message_edit'  WHERE id = '$edit_id'    
            my_conn.execute(f"UPDATE cbt_test SET pass_percent='{pass_percent}', instruction='{instruct}', test_name='{test_name}', class_name='{test_class}', test_status='{test_status}' WHERE id={record_id} ")
            my_conn.commit() 

            messagebox.showinfo("Record updated", "Your record is now updated.")
            
            
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
    self = EditTest(10)
    self.mainloop()     
