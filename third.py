#Password generator function
def generate_password():
 try:
   repeat = int(repeat_entry.get())
   length = int(length_entry.get())
 except:
   messagebox.showerror(message="Please key in the required inputs")
   return
 #Check if user allows repetition of characters
 if repeat == 1:
   password = random.sample(character_string,length)
 else:
   password = random.choices(character_string,k=length)
 #Since the returned value is a list, we convert to a string using join
 password=''.join(password)
 #Declare a string variable
 password_v = StringVar()
 password="Created password: "+str(password)
 #Assign the password to the declared string variables
 password_v.set(password)
 #Create a read only entry box to view the output, position using place
 password_label = Entry(password_gen, bd=0, bg="gray85", textvariable= password_v, state="readonly")
 password_label.place(x=10, y=140, height=50, width=320)