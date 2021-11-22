import random

# importing everything from tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import Frame, Label, Style

Main_window = tk.Tk()
Main_window.title("Fun Friday!!")
Main_window.attributes('-fullscreen',True)

bg = PhotoImage(file="back.png")
label1 = Label(Main_window, image=bg)
label1.place(x=0, y=0)

label = tk.Label(Main_window, text="Yeah!! Today is Fun Friday!!", fg="black",
                 font=("Showcard Gothic", 30), bg="white")
label.pack(pady=50)

Tasks = {'Inqlaab Zindabad' : 'Bhagat Singh',
             'Tum Muje Khoon Do, Mai Tumhe Azadi Dunga': 'Subhash Chandra Bose',
             'Karo ya Maro' : 'Mahatma Gandhi',
             'Sare Jahan Se Achha Hindustan Hamara': 'Muhammad Iqbal',
             'Vande Mataram' : 'Bankim Chandra Chatterjee',
         'Satyameva Jayate' : 'Pandit Madan Mohan Malviya',
             'Swaraj mera janamsiddh adhikar hai, aur mai ise lekar rahunga': 'Bal Gangadhar Tilak',
             'Ab bhi jiska khoon nahi khaula khoon nahi vo paani hai, jo desh ke kaam na aaye vo bekaar jawani hai' : 'Chandrashekar Azad',
             'Sarfaroshi ki tamanna ab hamare dil me hai, dekhna hai zor kitna baazu-e-qaatil me hai' : 'Ramprasad Bismil',
'Aaram haram hai' : 'Jawaharlal Nehru','Khoon se khelenge Holi gar Vatan mushkil main hai' : 'Ashfaqullah Khan'}


def display_name():
  while len(Tasks)>0:
      slogan = random.choice(Tasks)
      Tasks.remove(slogan)
      return slogan


def display_task():
    while len(task_list) > 0:
        task = random.choice(task_list)
        return task

def pick_slogan():
    name_label.config(text=display_name())


frame1 = tk.Frame(master=Main_window, width = 1500 ,height=100)
name_label = Label(master=frame1, text="", font=("Snap ITC", 30))
name_label.place(x=0.5, y=0.5)
name_label.pack(pady=20)
pickup_name = Button(master=frame1, text="Slogan", command=pick_name, width=25, font=("Snap ITC", 15))
pickup_name.pack(pady=20)
frame1.pack(pady=20, fill=X)


def freedom_fighter_name():
    task_label.config(text=display_task())


frame2 = tk.Frame(master=Main_window, width = 1500, height=500)
task_label = Label(master=frame2, text="", font=("Snap ITC", 15))
task_label.place(x=0.5, y=0.5)
task_label.pack(pady=20)
pickup_task = Button(master=frame2, text="Freedom Fighter", command=pick_task, width=25, font=("Snap ITC", 15))
pickup_task.pack(pady=20)
frame2.pack(pady=20, fill=X)

# Start the GUI
Main_window.mainloop()




def display_name():
  while len(Name_list)>0:
      name = random.choice(Name_list)
      Name_list.remove(name)
      return name


def display_task():
    while len(task_list) > 0:
        task = random.choice(task_list)
        return task
