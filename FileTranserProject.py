import shutil
import os

#source file
source = "/Users/Josep/Desktop/SourceFolder/"

#destination folder
#
dest = "/Users/Josep/Desktop/EndFolder/"
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, dest)

    

