import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import time,sys
from PIL import Image, ImageTk
from tkinter.constants import NW
import os
from playsound import playsound


def set_alarm():
    alarm_time = user_input.get()
    while True:
        current_time = time.strftime('%H:%M:%S')
        if current_time == alarm_time:
            messagebox.showinfo("Alarm", "Time to wake up!")
            playsound("JackSparrow_Bgm.mp3")
            break



root = tk.Tk()
root.title("Alarm Clock")
root.geometry("622x350")
canvas=tk.Canvas(root,width=622,height=350)

# Load the image and resize it to match the canvas dimensions
image = Image.open("alarm.jpg")
image = image.resize((622, 350))
image=ImageTk.PhotoImage(Image.open("alarm.jpg"))


# Create a Canvas widget with the resized image
canvas = tk.Canvas(root, width=622, height=350)
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()
header=tk.Frame(root)


box1=tk.Frame(root)
box1.place(x=250,y=180)
box2=tk.Frame(root)
box2.place(x=265,y=230)

#label
box3=tk.Frame(root)
box3.place(x=220,y=120)
comment=tk.Button(box3,text="Enter alarm time (HH:MM:SS):",font=('Arial Narrow',12))
comment.grid(row=0,column=2)

#Input Time

user_input=tk.Entry(box1,font=('Arial Narrow',20),width=10)
user_input.grid(row=0,column=2)

#Set Alarm Button

start_button=tk.Button(box2,text="Set Alarm",font=('Arial Narrow',16,'bold'),command=set_alarm)
start_button.grid(row=2,column=2)





root.mainloop()
