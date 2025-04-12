#PythonGeeks -fun to add new contact
def AddContact():
    if Name.get()!="" and Number.get()!="":
        contactlist.append([Name.get() ,Number.get()])
        print(contactlist)
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Add New Contact")
 
    else:
        messagebox.showerror("Error","Please fill the information")
 
def UpdateDetail():
    if Name.get() and Number.get():
        contactlist[Selected()] = [Name.get(), Number.get()]
   
        messagebox.showinfo("Confirmation", "Successfully Update Contact")
        EntryReset()
        Select_set()
 
    elif not(Name.get()) and not(Number.get()) and not(len(select.curselection())==0):
        messagebox.showerror("Error", "Please fill the information")
 
    else:
        if len(select.curselection())==0:
            messagebox.showerror("Error", "Please Select the Name and \n press Load button")
        else:
            message1 = """To Load the all information of \n
                          selected row press Load button\n.
                          """
            messagebox.showerror("Error", message1)