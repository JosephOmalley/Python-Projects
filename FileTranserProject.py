# Upon execution of this program all files that were modified in the past 24 hours will be transfered to recieving folder
# 3.9.0 version of python
# author Joseph Omalley


import shutil
import os.path as path
import datetime
from datetime import timedelta
import time
import os
#source file
source = "/Users/Josep/Desktop/SourceFolder/"
#destination folder
dest = "/Users/Josep/Desktop/EndFolder/"
files = os.listdir(source)
#command to see of list was created correctly
print(files)
#for loop that links list of files to directory(pFiles),instantiates a pTime that holds 24 hours ago, instantiates a variable (mTime) that finds when our files were edited last,
#instantiates variable (cDateT) that changes epoch time to readable time stamp, and finally an if comparision decides whether or not to move files. 
for i in files:
    pFiles = os.path.join(source, i)
    pTime = datetime.datetime.now()-timedelta(hours = 24)
    mTime = os.path.getmtime(pFiles)
    cDateT = datetime.datetime.fromtimestamp(mTime)
    if pTime < cDateT:
        shutil.move(source+i, dest)
       

