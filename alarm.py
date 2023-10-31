import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import time,sys
from PIL import Image, ImageTk
from tkinter.constants import NW
import os


def set_alarm():
    alarm_time = user_input.get()
    while True:
        current_time = time.strftime('%H:%M:%S')
        if alarm_time=="":
            messagebox.askretrycancel("Error Message","Please Enter Value")
        else:
            if current_time == alarm_time:
                messagebox.showinfo("Alarm", "Time to wake up!")
                #playsound("JackSparrow_Bgm.mp3")
                break



root = tk.Tk()
root.title("Alarm Clock")
root.geometry("622x350")
canvas=tk.Canvas(root,width=622,height=350)

# Load the image and resize it to match the canvas dimensions
image = Image.open("alarm1.jpg")
image = image.resize((622, 350))
image=ImageTk.PhotoImage(Image.open("alarm1.jpg"))


# Create a Canvas widget with the resized image
canvas = tk.Canvas(root, width=622, height=350)
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

header=tk.Frame(root)

#label
label = tk.Label(root, text="Enter alarm time (HH:MM:SS):")
label.pack()
box3=tk.Frame(root)
box3.place(x=200,y=150)



box1=tk.Frame(root)

box1.place(x=250,y=180)

box2=tk.Frame(root)

box2.place(x=250,y=260)

#Time taken by User as Input

user_input=tk.Entry(box1,font=('Arial Narrow',20),width=10)
user_input.grid(row=0,column=2)

#Set Alarm Button

start_button=tk.Button(box2,text="Set Alarm",font=('Arial Narrow',16,'bold'),command=set_alarm)

start_button.grid(row=2,column=2)





root.mainloop()
