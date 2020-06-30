import sqlite3

conn = sqlite3.connect('customer.db')

#crear cursor
c = conn.cursor()

#crear una tabla
#c.execute("""CREATE TABLE customers (
#    first_name text,
#    last_name text,
#    email text
#)""")

#muchos_customers = [
#                    ('Momo', 'Espirit', 'momo@espirit.com'),
#                    ('Zai', 'Espirit', 'zai@espirit.com'),
#                    ('Adri', 'Fraust', 'adri@fraust.com')
#                    ]
#c.executemany("INSERT INTO customers VALUES (?, ?, ?)", muchos_customers)

#Query database
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

for item in items:
    print(item)


#print("comando ejecutado exitosamente")
conn.commit()

conn.close()
