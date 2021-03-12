import sqlite3
#connects to db and saves the connection point as "conn"
conn = sqlite3.connect("fileList.db")


with conn:
    cur = conn.cursor() #sets cursor as "cur" this binds connection 
    cur.execute("CREATE TABLE IF NOT EXISTS files ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        filename TEXT)")#creates table in db "files"
    conn.commit() #makes changes stable
conn.close() #ends connection with db


#reestablished connection with "fileList.db"
conn = sqlite3.connect("fileList.db")

#tuple of file names
filelist = ("information.docx", "Hello.txt", "myImage", \
            "mymovie.mpg", "world.txt", "data.pdf", "myphoto.jpg")

for x in filelist:
    if x.endswith("txt"):
        with conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO files(filename) VALUES (?)', (x,)) #note that the trailing comma allows the tuple to be appended
            print(x)

#closes connection
conn.close()
                
