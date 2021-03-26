#Author: Joseph Omalley
#
#This is a small program that takes in a str from the user then opens it
#in an html file.
import tkinter
from tkinter import *
import webbrowser

#this function takes in the Entry box's input and stores it in a var(value).
#once stored and executed the program writes and opens the html file with the
#input provied by user. 
def launchPage():
    f = open("demof.html", "w")
    value = En.get()
    f.write("<html>\n<body>\n<h1>\n" + value +"</h1>\n</body>\n</html>")
    f.close()

    webbrowser.open("demof.html")
# This is the The GUI with three widgets/elements.

#create window 
root = Tk()
root.minsize(220,150)
root.maxsize(220,150)
root.title("Upload text to an HTML doc")
#create label
Lb = Label(root, text="Enter text:")
Lb.grid(row=0, column=0, padx=(27,0), pady=(10,10))
# create entry box
En = Entry(root)
En.grid(row=1, column=0, padx=(27,0), pady=(10,10))

#button that run "lanuchPage()" function
Bt = Button(root, text="Submit to show on html doc!", command=launchPage)
Bt.grid(row=2, column=0, padx=(27,0), pady=(10,10)) 
root.mainloop()
