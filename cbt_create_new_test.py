
#print("Opened database successfully");
import tkinter  as tk 
from tkinter import * 
import sqlite3 
from database import connect_db
my_conn = connect_db()


#def create_test():
#class SecondWindow(tk.Toplevel):

class CreateTest(tk.Toplevel):
  def __init__(self, *args, title="Create new test", **kwargs):   
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
    
    #my_conn.execute('''CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, 
    #Name TEXT, Class TEXT, Score TEXT, Gender TEXT)''')
    #my_conn.commit()

    # add one Label --- top
    l0 = tk.Label(self,  text='Create Test', font=('Helvetica', 16), width=30,anchor="c" )  
    l0.grid(row=1,column=1,columnspan=4) 


    my_str = tk.StringVar()
    l5 = tk.Label(self,  textvariable=my_str, width=30 )  
    l5.grid(row=3,column=2) 


    # entry 1
    l1 = tk.Label(self,  text='Test Name: ', width=20, anchor="c" )  
    l1.grid(row=5,column=1) 

    t1 = tk.Text(self,  height=1, width=30) 
    t1.grid(row=5,column=2) 

    #entry 2
    l2 = tk.Label(self,  text='Class: ', width=20 )  
    l2.grid(row=6,column=1) 

    # add list box for selection of class
    options = StringVar(self)
    options.set("") # default value
    opt1 = OptionMenu(self, options, "Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6")
    opt1.config(width=20)
    opt1.grid(row=6,column=2)

    #entry 3
    '''
    l3 = tk.Label(self,  text='Mark: ', width=20 )  
    l3.grid(row=7,column=1) 

    t3 = tk.Text(self,  height=1, width=30,bg='white') 
    t3.grid(row=7,column=2) 
    '''

    #enry 4
    
    lbl_gender = tk.Label(self,  text='Status: ', width=10 )  
    lbl_gender.grid(row=8,column=1) 
    radio_v = tk.StringVar()

    radio_v.set('once')
    r1 = tk.Radiobutton(self, text='Take one time', variable=radio_v, value='once')
    r1.grid(row=8,column=2)
    r2 = tk.Radiobutton(self, text='Take multiple times', variable=radio_v, value='multiple')
    r2.grid(row=8,column=3)


    b1 = tk.Button(self,  text='Add Record', width=20, command=lambda: add_data())  
    b1.grid(row=10,column=2) 



    #--------------------------------------------------------------

    #my_str.set("Output")
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
                #x=my_conn.execute('''select last_insert_rowid()''')
                #id=x.fetchone()
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

       
''''
if __name__ == "__main__":
    self = CreateTest()
    self.mainloop()     
'''