#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from tkinter import ttk
import pandas as pd

def all_saved_task(fCent):
    
    root=Frame(fCent,bg="grey")
    root.pack()
    
    # Add Record
    def add_record():
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="lightblue")

        global count
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text="", values=(name_box.get(), id_box.get(), topping_box.get()), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text="", values=(name_box.get(), id_box.get(), topping_box.get()), tags=('oddrow',))

        count += 1

        # Clear the boxes
        name_box.delete(0, END)
        id_box.delete(0, END)
        topping_box.delete(0, END)

    # Remove all records
    def remove_all():
        for record in my_tree.get_children():
            my_tree.delete(record)

    # Remove one selected
    def remove_one():
        x = my_tree.selection()[0]
        my_tree.delete(x)

    # Remove many selected
    def remove_many():
        x = my_tree.selection()
        for record in x:
            my_tree.delete(record)

    # Select Record
    def select_record():
        # Clear entry boxes
        name_box.delete(0, END)
        id_box.delete(0, END)
        topping_box.delete(0, END)

        # Grab record number
        selected = my_tree.focus()
        # Grab record values
        values = my_tree.item(selected, 'values')

        #temp_label.config(text=values[0])

        # output to entry boxes
        name_box.insert(0, values[0])
        id_box.insert(0, values[1])
        topping_box.insert(0, values[2])


    # Save updated record
    def update_record():
        # Grab record number
        selected = my_tree.focus()
        # Save new data
        my_tree.item(selected, text="", values=(name_box.get(), id_box.get(), topping_box.get()))

        # Clear entry boxes
        name_box.delete(0, END)
        id_box.delete(0, END)
        topping_box.delete(0, END)

    # Create Binding Click function
    def clicker(e):
        select_record()

    # Move Row up
    def up():
        rows = my_tree.selection()
        for row in rows:
            my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

    # Move Row Down
    def down():
        rows = my_tree.selection()
        for row in reversed(rows):
            my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)
    
    
#     root = Tk()
#     root.title('Codemy.com - TreeView')
#     # root.iconbitmap('c:/gui/codemy.ico')
#     root.geometry("800x600")

    # Add some style
    style = ttk.Style()
    #Pick a theme
    style.theme_use("default")
    # Configure our treeview colors

    style.configure("Treeview", 
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3"
        )
    # Change selected color
    style.map('Treeview', 
        background=[('selected', 'blue')])
    
    # Frame Start from here
    add_frame = Frame(root,bg="grey")
    add_frame.pack(pady=20)
    
    #Labels
    nl = Label(add_frame, text="Task",bg="grey",font="Helvetica 20 bold")
    nl.grid(row=0, column=0)

    il = Label(add_frame, text="Time",bg="grey",font="Helvetica 20 bold")
    il.grid(row=0, column=1)

    tl = Label(add_frame, text="Date",bg="grey",font="Helvetica 20 bold")
    tl.grid(row=0, column=2)

    #Entry boxes
    name_box = Entry(add_frame, width=30,font="Helvetica 20")
    name_box.grid(row=1, column=0)

    id_box = Entry(add_frame, width=10,font="Helvetica 20")
    id_box.grid(row=1, column=1)

    topping_box = Entry(add_frame, width=10,font="Helvetica 20")
    topping_box.grid(row=1, column=2)
    
    # Button Frame Start from here
    button_frame = Frame(root)
    button_frame.pack(pady=20)
    
    # Buttons
    move_up = Button(button_frame, text="Move Up", width=20, command=up)
    move_up.grid(row=0, column=1)
    move_down = Button(button_frame, text="Move Down", width=20, command=down)
    move_down.grid(row=0, column=2)
    select_button = Button(button_frame, text="Select Task", width=20, command=select_record)
    select_button.grid(row=0, column=3)
    update_button = Button(button_frame, text="Update Task", width=20, command=update_record)
    update_button.grid(row=0, column=4)
    add_record = Button(button_frame, text="Add Record", width=20, command=add_record)
    add_record.grid(row=1, column=1)
    # Remove all
    remove_all = Button(button_frame, text="Remove All Records", width=20, command=remove_all)
    remove_all.grid(row=1, column=2)
    # Remove One
    remove_one = Button(button_frame, text="Remove One Selected", width=20, command=remove_one)
    remove_one.grid(row=1, column=3)
    # Remove Many Selected
    remove_many = Button(button_frame, text="Remove Many Selected", width=20, command=remove_many)
    remove_many.grid(row=1, column=4)
    
    
    
    # Create Treeview Frame
    tree_frame = Frame(root)
    tree_frame.pack(pady=20)

    # Treeview Scrollbar
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    # Create Treeview
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
    # Pack to the screen
    my_tree.pack()

    #Configure the scrollbar
    tree_scroll.config(command=my_tree.yview)

    # Define Our Columns
    my_tree['columns'] = ("Task", "Time", "Date","Task Status")

    # Formate Our Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Task", anchor=W, width=350)
    my_tree.column("Time", anchor=CENTER, width=120)
    my_tree.column("Date", anchor=W, width=120)
    my_tree.column("Task Status", anchor=W, width=130)

    # Create Headings 
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("Task", text="Task", anchor=W)
    my_tree.heading("Time", text="Time", anchor=CENTER)
    my_tree.heading("Date", text="Date", anchor=W)
    my_tree.heading("Task Status", text="Task Status", anchor=W)

    # Reading Excel File
    try:
        # Create a dataframe
        df = pd.read_excel("TASK1.xlsx")
        
    except FileNotFoundError:
        tkinter.messagebox.showwarning(title="Warning!",message="No Task Added")
    data=df.to_numpy().tolist()


    # Create striped row tags
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    global count
    count=0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('oddrow',))

        count += 1


    # Bindings
    #my_tree.bind("<Double-1>", clicker)
    my_tree.bind("<ButtonRelease-1>", clicker)
#     print(my_tree.selection())
#     mainloop()

# all_saved_task()

