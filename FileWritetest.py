
import tkinter
from tkinter import *
import webbrowser




def launchPage():
    f = open("demof.html", "w")
    f.write("<html>\n<body>\n<h1>\nHello,world</h1>\n</body>\n</html>")
    f.close()

    webbrowser.open("demof.html")
# left just finished GUI
root = Tk()
root.minsize(220,150)
root.title("Upload text to an HTML doc")

Lb = Label(root, text="Enter text:")
Lb.grid(row=0, column=0, padx=(27,0), pady=(10,10))

En = Entry(root)
En.grid(row=1, column=0, padx=(27,0), pady=(10,10)) 

Bt = Button(root, text="Submit to show on html doc!")
Bt.grid(row=2, column=0, padx=(27,0), pady=(10,10)) 
root.mainloop()
