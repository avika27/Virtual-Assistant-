import sqlite3
import csv

# Connect to SQLite DB
conn = sqlite3.connect("Deepa.db")

# Cursor to execute SQL
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS deepa_virtual_assistant (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(300),
    path VARCHAR(1000)
)
""")

# Insert new app path into table
#cursor.execute("""
#INSERT INTO deepa_virtual_assistant (name, path)
#VALUES (?, ?)
#""", ("ONENOTE", "C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe"))

cursor.execute("""
CREATE TABLE IF NOT EXISTS web_command (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(300),
    URL VARCHAR(1000)
)
""")

#cursor.execute("""
#INSERT INTO deepa_virtual_assistant(name, path)
#VALUES (?, ?)
#""", ("calculator", "start calc")) 

#cursor.execute("""
#DELETE FROM deepa_virtual_assistant WHERE name = 'calculator'
#""")
#cursor.execute("""
#UPDATE deepa_virtual_assistant SET name = 'devcpp' WHERE name = 'Dev-Cpp';

#""")
# whatsapp automation banane ke contacts  table bnaya 
cursor.execute  ("""
CREATE TABLE IF NOT EXISTS  contacts( id integer primary key, name VARCHAR(200),mobile_no VARCHAR (255),email VARCHAR(300) NULL)
                 


""")
# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# google contacts ko import krne ke liye 
#desired_columns_indices = [0, 20] ## eska mtlb hai humhe itne hi columns chaihye 0- and 20 chaihye 

# Read data from CSV and insert into SQLite table for the desired columns
#with open('contacts.csv', 'r', encoding='utf-8') as csvfile: ## file open kiya in read mode aur utf-8 mtlb wooh emoji wagera ko dekhta hai 
  #  csvreader = csv.reader(csvfile) ## esse hum ek column ek time pe hi  row ko dekh skte hai 
   # for row in csvreader:
    #    selected_data = [row[i] for i in desired_columns_indices]
        # esse hum haar row ko traverse kr rahe hau aur bol rahe hai ki humhe bas column 0 and 30 ki values chaihye aur usse store krdo 
     #   cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))
# end mein email ke aage null esliye aaya kyunki yeah optional hai mtlb hum email hum null likh skte hai 

cursor.execute ("""
  INSERT INTO contacts ('name','mobile_no') VALUES ('nonu','8595530981')                
""")

#''')
#### 5. Search Contacts from database 
query = 'chokelal'
query = query.strip().lower()

cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
results = cursor.fetchall()
print(results[0][0])
# Save changes
conn.commit()

# Close connection
conn.close()
