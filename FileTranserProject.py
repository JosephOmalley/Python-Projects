import shutil
import os.path as path
import datetime
import timedelta
import time
import os
#source file
source = "/Users/Josep/Desktop/SourceFolder/"



#destination folder
#
#dest = "/Users/Josep/Desktop/EndFolder/"
files = os.listdir(source)
print(files)

for i in files:
    i = 0
    files
    print(path.getmtime(files[i]))
          
  






"""print(modificationTime)
now = datetime.now()
for i in files:
    time = path.getmtime(i)
    if time < timedelta(hours=24):
    #we are saying move the files represented by 'i' to their new destination
        shutil.move(source+i, dest)
    else:
        pass
        
"""
    
