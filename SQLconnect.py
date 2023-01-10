import sqlite3

connect = sqlite3.connect('data.db')

# connect.execute("DROP TABLE IF EXISTS CUSTOMER")
# connect.execute('''CREATE TABLE CUSTOMER
#             (ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL,
#             AGE INT NOT NULL);''')

connect.execute("INSERT INTO CUSTOMER(ID, NAME, AGE) VALUES(1, 'ZACH', 24)")

all_data = connect.execute('''SELECT * FROM CUSTOMER''')
for row in all_data:
    print(row)

connect.close()
