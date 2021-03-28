# Upon execution of this program all files that were modified in the past 24 hours will be transfered to recieving folder
# 3.9.0 version of python
# author Joseph Omalley
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import shutil
import os.path as path
import datetime
from datetime import timedelta
import time
import os
#source folder is defined by the selSource() function and is run by the select source button in the gui

#destination folder is defined by the selDest() function and is run by the select dest button in the gui


#command to see of list was created correctly

#for loop that links list of files to directory(pFiles),instantiates a pTime that holds 24 hours ago, instantiates a variable (mTime) that finds when our files were edited last,
#instantiates variable (cDateT) that changes epoch time to readable time stamp, and finally an if comparision decides whether or not to move files. 

           
root = Tk()
root.title("Check Files")
root.minsize(350,200)
#trailing slash need at the end of sPath
def selSource():
    global files
    global sPath
    sPath = filedialog.askdirectory()
    sPath += '/'
    e1.insert(END, sPath)
    files = os.listdir(sPath)

def selDest():
    global dest
    dPath = filedialog.askdirectory()
    e2.insert(END, dPath)
    dest = dPath

def checkFile():
    for i in files:
        pFiles = os.path.join(sPath, i)
        pTime = datetime.datetime.now()-timedelta(hours = 24)
        mTime = os.path.getmtime(pFiles)
        cDateT = datetime.datetime.fromtimestamp(mTime)
        if pTime < cDateT:
            shutil.move(sPath+i, dest)

bB1 = Button(root, text="Select Source",command = selSource)
bB2 = Button(root, text="Select Dest",command = selDest)
cB = Button(root, text="Check for files...",command = checkFile)
clB = Button(root, text="Close Program")



e1= Entry(root)

e2=Entry(root)

bB1.grid(row=0, column=0,rowspan=1,columnspan=2, padx = (27,10) , pady= (50,0),sticky=N+E+W)

bB2.grid(row=1, column=0,rowspan=1,columnspan=2, padx = (27,10) , pady= (10,0),sticky=N+E+W)

e1.grid(row=0, column=2,rowspan=1,columnspan=4, padx = (27,0) , pady= (50,0),sticky=N+E+W)

e2.grid(row=1, column=2, rowspan=1,columnspan=4, padx = (27,0) , pady= (10,0),sticky=N+E+W)

cB.grid(row=2, column=0,rowspan=2,columnspan=2, padx = (27,10) , pady= (10, 0),sticky=N+E+W)

clB.grid(row=2, column=2,rowspan=2,columnspan=4, padx = (27,0) , pady= (10, 0),sticky=N+E+W)



    
    
root.mainloop()
