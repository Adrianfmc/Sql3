import sqlite3


# Query the DB and return all the records

def show_all():
    # Conectar a la base de datos
    conn = sqlite3.connect('customer.db')
    # crear cursor
    c = conn.cursor()
    # Query database
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    for item in items:
        print(item)

#Add new record to the table
def add_one(first,last,email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first,last,email))
    conn.commit()
    conn.close()

def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE rowid = (?)", id)
    conn.commit()
    conn.close()

#Add meny new records to the table
def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
    conn.commit()
    conn.close()

# Look up
def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, *  FROM customers WHERE email = (?)", (email,))
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()
