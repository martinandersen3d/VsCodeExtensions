import sqlite3
import os.path
import json
#Connection to the DB
try:
    # Make sure to find the file.db in the script directory
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
    db_path = os.path.join(BASE_DIR, "state.vscdb")
    conn = sqlite3.connect(db_path)

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)



# Execute query on the sqlite DB
cur = conn.cursor()
cur.execute("SELECT t.value FROM ItemTable t WHERE t.key = 'extensionsIdentifiers/disabled';")

# Extract data and convert it to json
rows = cur.fetchall()
data=str(rows[0])[2:-3]
result="{\"data\":" +  data + "}"
print('----------- ')
json_data=json.loads(result)

list=json_data["data"]
print(type(list))
file_output = ""
for o in list:
    id = o["id"]
    file_output = file_output + id + "\n" 

    print(id)
print(list)
# for row in rows[0]:
#         print(str(row))
#         print(' ')
        

# close the DB connection 
conn.close() 



file = open("text.txt", "w") 
file.write(file_output) 
file.close() 