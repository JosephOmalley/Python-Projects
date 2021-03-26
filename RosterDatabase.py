import sqlite3

with sqlite3.connect("roster_database") as connection:
    c = connection.cursor()
    peopleValues = (('JEAN-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('AK\'NOT', 'Mangalore', -5))
    c.execute("DROP TABLE IF EXISTS People")
    c.executescript("CREATE TABLE IF NOT exists People(name TEXT,species TEXT,IQ INT)")
    c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)
    c.execute("UPDATE People SET species = 'Human' WHERE species = 'Meat Popsicle'")     
    
    connection.commit()


    
def DisplayN_IQ():
    with sqlite3.connect("roster_database") as connection:
        c = connection.cursor()
        c.execute("SELECT name, IQ FROM People")
        for row in c.fetchall():
            print(row)
DisplayN_IQ()
