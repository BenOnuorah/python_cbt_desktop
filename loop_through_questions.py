from tkinter import *
from tkinter import ttk
# from openpyxl.workbook import Workbook
# from openpyxl import load_workbook


# initiate variables
global root1
global response
# answers to be saved somewhere
answers = {"governance": [],
           "eligibility": [],
           "operations": [],
           "monitoring": [],
           "continuing_improvement": []
           }
# prepared question lists
questions = {"governance": ['A', 'B'],
             "eligibility": ['C', 'D'],
             "operations": ['E', 'F'],
             "monitoring": ['G', 'H'],
             "continuing_improvement": ['I', 'J']
             }

# initiate the main window
root1 = Tk()
# create main window label
label1 = Label(root1, text="Question Tool")
# add the lable to the root window
label1.pack()


# define exit button
def Exit():
    root1.destroy()


def selection(parent, label_obj):
    global response
    global questions
    global answers
    user_choice = response.get()
    if user_choice == "":
        # do something if no answer is selected
        print("No answer selected!")
    else:
        print("User Selected:  " + label_obj["text"])
        print("User Selected:  " + user_choice)
        # get question category
        label_obj_name = label_obj.winfo_name()
        # update answers
        answers[label_obj_name].append({label_obj["text"]: user_choice})
        # check if we have run out of questions
        if len(answers[label_obj_name]) == len(questions[label_obj_name]):
            # clear parent tab
            for i in parent.winfo_children():
                i.destroy()
            msg = ttk.Label(parent, text="Done")
            msg.grid(column=0, row=0, padx=30, pady=30)
            print(answers[label_obj_name])
            print(answers)
            # optional: reset response for new tab
            response.set("")
        else:
            # iterating through the list of questions
            # The questions must be different or not repeated in the same category.
            # get the next question in the list
            next_question = questions[label_obj_name][len(answers[label_obj_name])]
            # get next question text
            label_obj["text"] = next_question
            # optional: reset response for next question
            response.set("")
            # or set default selection
            # response.set("YES")


def create_labels_and_buttons(parent, label_text, label_name):
    """Create a separate label and buttons for each tab.

    The response object is global to all tabs.
    Added a label name to distinguish which category the question belongs to.
    """
    global response
    lb = ttk.Label(parent, text=label_text, name=label_name)
    lb.grid(column=0, row=0, padx=30, pady=30)
    rb1 = ttk.Radiobutton(parent, text="Yes", value="YES", variable=response)
    rb1.grid(column=0, row=5, padx=10, pady=10)
    rb2 = ttk.Radiobutton(parent, text="No", value="NO", variable=response)
    rb2.grid(column=0, row=10, padx=10, pady=10)
    # you can pass the arguments to the function like here
    ttk.Button(parent, text="Next",
               command=lambda: selection(parent, lb)).grid(column=0, row=20, padx=10, pady=10)
    






def Start_Button():
    global response
    global questions
    global answers
    root1.destroy()
    root = Tk()
    root.title("Question Tool")
    tabControl = ttk.Notebook(root)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)
    tabControl.add(tab1, text='1) Governance')
    tabControl.add(tab2, text='2) Eligibility')
    tabControl.add(tab3, text='3) Operations')
    tabControl.add(tab4, text='4) Monitoring')
    tabControl.add(tab5, text='5) Continuing Improvement')
    tabControl.pack(expand=1, fill="both")
    # response for buttons
    response = StringVar()
    # apply the questions as labels
    create_labels_and_buttons(parent=tab1, label_text=questions["governance"][0], label_name="governance")
    create_labels_and_buttons(parent=tab2, label_text=questions["eligibility"][0], label_name="eligibility")
    create_labels_and_buttons(parent=tab3, label_text=questions["operations"][0], label_name="operations")
    create_labels_and_buttons(parent=tab4, label_text=questions["monitoring"][0], label_name="monitoring")
    create_labels_and_buttons(parent=tab5, label_text=questions["continuing_improvement"][0],
                              label_name="continuing_improvement")

    root.mainloop()


# add start and stop buttons
Start_Button = Button(root1, text="Click to Begin", padx=10, pady=10, command=Start_Button)
Start_Button.pack()
Exit_Button = Button(root1, text="Exit", padx=10, pady=10, command=Exit)
Exit_Button.pack()
# call main loop
root1.mainloop()