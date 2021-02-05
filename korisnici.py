import sqlite3

class Baza:
    def __init__(self, korisnici):
        self.conn = sqlite3.connect(korisnici)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS korisnici (id INTEGER PRIMARY KEY, ime text, prezime text, username text, password text, brojtel text, email text, level INT)")
        self.conn.commit()

    ##   self.cur.execute("SELECT * FROM korisnici")

    def insert(self, ime, prezime, username, password, brojtel, email, level):
        self.cur.execute("INSERT INTO korisnici VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)", (ime, prezime, username, password, brojtel, email, level))
        self.conn.commit()

    def update(self, id, ime, prezime, username, password, brojtel, email, level):
        self.cur.execute("UPDATE korisnici SET ime = ?, prezime = ?, username = ?, password = ?, brojtel = ?, email = ?, level = ? WHERE id = ?",
                         (ime, prezime, username, password, brojtel, email, level, id))
        self.cur.commit()

   # def provjera(self, username, password):
    #    self.cur.execute('SELECT * from korisnici WHERE username="%s" AND password="%s"' % (user, pw))

    def __del__(self):
        self.conn.close()