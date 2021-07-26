import sqlite3

def connection():
    conn = sqlite3.connect("contact_book.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,name text,email_id text,number integer,second_number integer)")
    conn.commit()
    conn.close()

def entry(name,email_id,number,second_number):
    conn =sqlite3.connect("contact_book.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(name,email_id,number,second_number))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("contact_book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    row = cur.fetchall()
    conn.close()
    return row

def search(name="",email_id="",number="",second_number=""):
    conn = sqlite3.connect("contact_book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE name =? OR email_id=? OR number=? OR second_number=?",(name,email_id,number,second_number))
    row = cur.fetchall()
    conn.close()
    return row

def delete(id):
    conn =sqlite3.connect("contact_book.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,name,email_id,number,second_number):
    conn = sqlite3.connect("contact_book.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET name=?,email_id=?,number=?,second_number=? WHERE id=?",(name,email_id,number,second_number,id))
    conn.commit()
    conn.close()


