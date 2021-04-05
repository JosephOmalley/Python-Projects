#
# Author: Joseph D Omalley
#
# This is a simple app that keeps track of student's first and last name, phonenumber,
# email, current course. With a button to upload new information, and a button to delete old one.


#import built in modules 
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3

#import user-modules
import StrackerGui
import StrackerFunc



# Tkinter's frame class is what our Gui class will inherit from
class GuiScreen(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #Set up master frames
        self.master = master
        self.master.minsize(600,315) #(Height, Width)
        self.master.maxsize(600,315) #(Height, Width)
        self.master.title("The Kinter PhoneBook Demo")
        self.master.configure(bg="#F0F0F0")
        arg = self.master
        

        StrackerGui.load_gui(self)
        


        
if __name__ == "__main__":
    root = tk.Tk()
    app = GuiScreen(root)
    root.mainloop()
    
