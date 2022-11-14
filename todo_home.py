#!/usr/bin/env python
# coding: utf-8

# In[8]:


from tkinter import *
import pandas as pd
from tkinter import ttk
import tkinter.messagebox   
    
def home_module(fCent):
    
    root=Frame(fCent,bg="grey")
    root.pack()

    def entertask():    
        # Task input variables
        task_entry=entrybox.get()
        task_hour=hour_entry.get()
        task_minut=minut_entry.get()
        task_second=second_entry.get()
        task_date=date_entry.get()
        task_month=month_entry.get()
        task_year=year_entry.get()

        if(task_entry=="" or task_hour=="" or task_minut=="" or task_second=="" or 
           task_date=="" or task_month=="" or task_year==""):
            tkinter.messagebox.showwarning(title="Warning!",message="Please Enter All Deatails of Task")
        
        else:
            input_text=f"[({task_hour}:{task_minut}:{task_second})({task_date}/{task_month}/{task_year})] → {task_entry}"
            listbox_task.insert(0,input_text)
            
            # sending data to excel file
            task = f"{task_entry}"
            time = f"{task_hour}:{task_minut}:{task_second}"
            date = f"{task_date}/{task_month}/{task_year}"
            task_status = "0"

            try:
                dd=pd.read_excel('TASK1.xlsx')
                dd.loc[len(dd.index)] = [task,time,date,task_status]
                dd.to_excel('TASK1.xlsx', index=False)

            except:
                df = pd.DataFrame([[task,time,date,task_status]], columns=['Task', 'Time', 'Date','Task Status'])
                df.to_excel('TASK1.xlsx', index=False)
                
            # deleting entry boxes    
            entrybox.delete(0,END)
            hour_entry.delete(0,END)
            minut_entry.delete(0,END)
            second_entry.delete(0,END)
            date_entry.delete(0,END)
            month_entry.delete(0,END)
            year_entry.delete(0,END)


    #function to facilitate the delete task from the Listbox
    def deletetask():
        #selects the slected item and then deletes it 
        selected=listbox_task.curselection()
        listbox_task.delete(selected[0])
    #Executes this to mark completed 

    def markcompleted():
        marked=listbox_task.curselection()
        temp=marked[0]
        #store the text of selected item in a string
        temp_marked=listbox_task.get(marked)
        #update it 
        temp_marked=temp_marked+" ✔"
        #delete it then insert it 
        listbox_task.delete(temp)
        listbox_task.insert(temp,temp_marked)
    
    
    # Creating Frame for Task Entry and Buttons
    task_upper=Frame(root,bg="grey")
    task_upper.pack(pady=20)
    
     # task entry box and label
    entry_frame=Frame(task_upper)
    entry_frame.pack()
    entry_label= Label(entry_frame,text="Enter Task",font="Helvetica 20 bold")
    entrybox = Entry(entry_frame,width=35,font="Helvetica 20")
    entry_label.grid(row=0, column=1, padx=10, pady=10)
    entrybox.grid(row=0, column=2, padx=10, pady=10)
    
    
    # Task Date Time Frame
    task_datetime = Frame(task_upper)
    task_datetime.pack()
    # Task Date Time Details
    # TIME
    hour_label = Label(task_datetime,text="Time →", width=12, font="Helvetica 20 bold")
    minut_label = Label(task_datetime,text=":", font="Helvetica 20 bold")
    second_label = Label(task_datetime,text=":", font="Helvetica 20 bold")
    hour_entry = Entry(task_datetime,width=2, font="Helvetica 20")
    minut_entry = Entry(task_datetime,width=2, font="Helvetica 20")
    second_entry = Entry(task_datetime,width=2, font="Helvetica 20")
    # DATE
    date_label = Label(task_datetime,text="Date →", width=12, font="Helvetica 20 bold")
    month_label = Label(task_datetime,text="/", font="Helvetica 20 bold")
    year_label = Label(task_datetime,text="/", font="Helvetica 20 bold")
    date_entry = Entry(task_datetime,width=2, font="Helvetica 20")
    month_entry = Entry(task_datetime,width=2, font="Helvetica 20")
    year_entry = Entry(task_datetime,width=4, font="Helvetica 20")
    #griding date time
    hour_label.grid(row=0, column=1, padx=10, pady=10)
    hour_entry.grid(row=0, column=2, pady=10)
    minut_label.grid(row=0, column=3, padx=1, pady=10)
    minut_entry.grid(row=0, column=4, pady=10)
    second_label.grid(row=0, column=5, padx=1, pady=10)
    second_entry.grid(row=0, column=6, pady=10)
    date_label.grid(row=0, column=7, padx=10, pady=10)
    date_entry.grid(row=0, column=8, pady=10)
    month_label.grid(row=0, column=9, padx=1, pady=10)
    month_entry.grid(row=0, column=10, pady=10)
    year_label.grid(row=0, column=11, padx=1, pady=10)
    year_entry.grid(row=0, column=12, padx=1, pady=10)
    
    # task entry buttons grid
    button_frame=Frame(task_upper, bg="grey")
    button_frame.pack(padx=20,pady=20)
    
    #Button widget 
    entry_button=Button(button_frame,text="Add task", fg="black", font="Helvetica 14 bold",width=20,command=entertask)
    delete_button=Button(button_frame,text="Delete selected task", fg="black", font="Helvetica 14 bold",width=20,command=deletetask)
    mark_button=Button(button_frame,text="Mark as completed ", fg="black", font="Helvetica 14 bold",width=20,command=markcompleted)
    
    entry_button.grid(row=0,column=1)
    delete_button.grid(row=0,column=2, padx=10)
    mark_button.grid(row=0,column=3)
    
    
    #Frame widget to hold the listbox and the scrollbar
    frame_task=Frame(root)
    frame_task.pack()

    #to hold items in a listbox
    listbox_task=Listbox(frame_task,bg="black",fg="white",height=20,width=60,font = "Helvetica 18 bold")  
    listbox_task.pack(side=tkinter.LEFT)

    #Scrolldown in case the total list exceeds the size of the given window 
    scrollbar_task=Scrollbar(frame_task)
    scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
    listbox_task.config(yscrollcommand=scrollbar_task.set)
    scrollbar_task.config(command=listbox_task.yview)
    

#     mainloop()


# fCent = Tk()
# fCent.title("TO-DO List")    
    
# home_module(fCent)

