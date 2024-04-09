import tkinter as tk

class SecondWindow(tk.Toplevel):
    def __init__(self, *args, title="Other Window", **kwargs):
        super().__init__(*args, **kwargs)
    
        self.title(title)
        self.geometry("500x200")
        self.wm_transient()

        tk.Label(self, font=(None, 20), text= \
            "This is a toplevel window.\n"
            "Create this after the main window.") \
            .pack(padx=20, pady=20)



       
'''
if __name__ == "__main__":
    #root = tk.Tk()
    self = SecondWindow()
    self.mainloop()           
'''