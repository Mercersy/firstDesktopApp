import sqlite3

def connect():
    conn = sqlite3.connect("projs.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS myProj (id INTEGER PRIMARY KEY, \
                title TEXT, pdate DATE, skills TEXT, details TEXT)")
    conn.commit()
    conn.close()

def insert(title, date, skills, details):
    conn = sqlite3.connect("projs.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO myProj VALUES (NULL, ?, ?, ?, ?)", \
                (title, date, skills, details))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("projs.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM myProj")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title = "", date = "", skills = "", details = ""):
    conn = sqlite3.connect("projs.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM myProj WHERE title LIKE ? AND pdate LIKE ? AND \
                skills LIKE ? AND details LIKE ?", ('%' + title + '%', \
                '%' + date + '%', '%' + skills + '%', '%' + details + '%'))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("projs.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM myProj where id = ?", (id,))
    conn.commit()
    conn.close()

def update(id, title, date, skills, details):
    conn = sqlite3.connect("projs.db")
    cur = conn.cursor()
    cur.execute("UPDATE myProj SET title = ?, pdate = ?, skills = ?, details = ?\
                WHERE id = ?", (id, title, date, skills, details))
    conn.commit()
    conn.close()


connect()
#insert('ert', '2016-08', 'Python', 'qweqwe')
#print(view())
#print(search(title = "rt"))
