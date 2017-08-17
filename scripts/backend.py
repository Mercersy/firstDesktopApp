import sqlite3

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS myProj (id INTEGER PRIMARY KEY, \
                    title TEXT, pdate DATE, skills TEXT, details TEXT)")
        self.conn.commit()

    def insert(self, title, date, skills, details):
        self.cur.execute("INSERT INTO myProj VALUES (NULL, ?, ?, ?, ?)", \
                    (title, date, skills, details))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM myProj")
        rows = self.cur.fetchall()
        return rows

    def search(self, title = "", date = "", skills = "", details = ""):
        self.cur.execute("SELECT * FROM myProj WHERE title LIKE ? AND pdate LIKE ? AND \
                    skills LIKE ? AND details LIKE ?", ('%' + title + '%', \
                    '%' + date + '%', '%' + skills + '%', '%' + details + '%'))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM myProj where id = ?", (id,))
        self.conn.commit()

    def update(self, id, title, date, skills, details):
        self.cur.execute("UPDATE myProj SET title = ?, pdate = ?, skills = ?, details = ?\
                    WHERE id = ?", (title, date, skills, details, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
