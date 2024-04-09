import tkinter as tk
import sqlite3
from tkinter import messagebox
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

#class DatabaseApp:
class DatabaseApp(tk.Toplevel):
    def __init__(self, root):
        self.root = root
        self.root.title("SQLite Database Example")
        self.root.geometry("600x300")

        # Create a database or connect to an existing one
        self.conn = sqlite3.connect(dir_path+'/cbt_app.db')
        self.cursor = self.conn.cursor()

        # Create a table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cbt_class_name (id INTEGER PRIMARY KEY, class_name TEXT)''')
        self.conn.commit()

        # Create GUI elements
        self.task_label = tk.Label(root, text="Class name:")
        self.task_label.pack()

        self.task_entry = tk.Entry(root)
        self.task_entry.pack()

        self.add_button = tk.Button(root, text="Add", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root)
        self.task_listbox.pack()

        self.delete_button = tk.Button(root, text="Delete", command=self.delete_task)
        self.delete_button.pack()

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.cursor.execute("INSERT INTO cbt_class_name (class_name) VALUES (?)", (task,))
            self.conn.commit()
            self.load_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please input a task.")

   
    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        self.cursor.execute("SELECT * FROM cbt_class_name")
        tasks = self.cursor.fetchall()
        for row in tasks:
            self.task_listbox.insert(tk.END, row[0], row[1])
   
    def delete_task(self):
        selected_task = self.task_listbox.get(tk.ACTIVE)
        if selected_task:
            self.cursor.execute("DELETE FROM cbt_class_name WHERE class_name=?", (selected_task,))
            self.conn.commit()
            self.load_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a Class to delete.")


    def __del__(self):
        self.conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()
