
from tkinter import *
from tkinter import messagebox
from korisnici import Baza
import sqlite3
from datetime import date


korisnici = Baza('glavanabaza.db')


# kreiramo program
app = Tk()

app.title('ProjectX - Log in')
app.iconbitmap('projx.ico')

user = ""
################################################################

def login():
    if not username_text.get() or not password_text.get(): # provjeravamo da li su oba polja popunjena..
        messagebox.showerror(title="Prazna polja", message="Niste popunili sva polja!")
        return
    global user
    user = username_text.get()
    pw = password_text.get()
    conn =  sqlite3.connect('glavanabaza.db')
    c = conn.cursor()
    c.execute('SELECT * from korisnici WHERE username="%s" AND password="%s"' % (user, pw))
    if c.fetchone() is not None:
        c.execute('SELECT level FROM korisnici WHERE username = ?', (user,))
        res = c.fetchone() # posto ovo returna kao tuple...
        level = res[0]     # uzimam prvi item iz tuple-a        
        if level == 1340:      # ako je admin
            print("Otvaram admin panel")
            messagebox.showinfo(title="Admin log in", message="Uspjesno ste se logovali kao administrator\nOtvaram Admin Panel...")
            app.destroy()
            AdminPanel()
        else:
            poruka = f"Uspjesno ste se logovali {user}\nUgodan ostatak dana.."
            messagebox.showinfo(title="Uspjesan login", message=poruka)
            app.destroy()
            UserPanel()
        #app.destroy()
        #AdminPanel()

    else:
        print("Neuspjesan login")
        messagebox.showerror(title="Neuspješan login..",
                             message="Korisnicko ime i lozinka nisu pronadjeni u našoj bazi podataka..."
                                     "\n\n\nUkoliko nemate račun možete to uraditi klikom na dugme \tRegistracija")
        return

def ComingSoon():
    messagebox.showinfo(title="Coming Soon", message="This feature is coming soon.. ")

def UserPanel():
    print("OVDJE SE OTVARA userpanel")
    pro = Tk()
    pro.title('ProjectX - UserPanel')
    pro.iconbitmap('projx.ico')

    adminLabel =Label(pro, text="Main menu", font=("Courier",20))
    adminLabel.grid(row=0, pady = 30, padx = 70)

    novikorisnik = Button(pro, text="Edit time sheet", width=25, command=ComingSoon, bg='#22b7e0') 
    novikorisnik.grid(row=1)

    edituser = Button(pro, text ="Take shipping Notes Picture", width=25, command = ComingSoon, bg='#22b7e0') # DODAJ KOMANDU...
    edituser.grid(row = 2, pady = 7)

    timesheets = Button(pro, text="Open Time Sheets", width = 25, command=ComingSoon, bg='#22b7e0')# DODAJ KOMANDU
    timesheets.grid(row=3)

    req_appovals = Button(pro, text="Create Request", width=25, command=ComingSoon, bg='#22b7e0')
    req_appovals.grid(row= 4, pady= 7)

    VacationCalenda = Button(pro, text="Vacation Calendar", width=25, command= ComingSoon, bg='#22b7e0')
    VacationCalenda.grid(row= 5)

    usern_label = Label(pro, text=f"Username: {user}")
    usern_label.grid(row = 9 ,pady = 15,sticky=W)

    datetime = Label(pro, text=date.today())
    datetime.grid(row=9, sticky=E)

    



def AdminPanel():
    print("OVDJE SE OTVARA AdminPanel")
    pro = Tk()
    pro.title('ProjectX - AdminPanel')
    pro.iconbitmap('projx.ico')

    adminLabel =Label(pro, text="Dobrodosli na Admin Panel!\nMain menu", font=("Courier",20))
    adminLabel.grid(row=0, pady = 30, padx = 30)

    novikorisnik = Button(pro, text="Create New User", width=30, command=registracija, bg='#22b7e0') 
    novikorisnik.grid(row=1)

    edituser = Button(pro, text ="Edit User", width=30, command = ComingSoon, bg='#22b7e0') # DODAJ KOMANDU...
    edituser.grid(row = 2, pady = 7)

    timesheets = Button(pro, text="Time Sheets", width = 30, command=ComingSoon, bg='#22b7e0')# DODAJ KOMANDU
    timesheets.grid(row=3)

    req_appovals = Button(pro, text="Audit File", width=30, command=ComingSoon, bg='#22b7e0')
    req_appovals.grid(row= 4, pady= 7)

    VacationCalenda = Button(pro, text="Vacation Calendar", width=30, command= ComingSoon, bg='#22b7e0')
    VacationCalenda.grid(row= 5)

    exp_time_sheets = Button(pro, text="Export Time Sheets", width=30, command= ComingSoon, bg='#22b7e0')
    exp_time_sheets.grid(row= 6, pady= 7)

    req_appovals = Button(pro, text="Requests & Approvals", width=30, command= ComingSoon, bg='#22b7e0')
    req_appovals.grid(row= 7)

    saveButton = Button(pro, text="Save & Exit", width = 45, command=ComingSoon, bg='#22b7e0')
    saveButton.grid(row = 8, padx = 10 ,pady = 10)

    usern_label = Label(pro, text=f"Username: {user}")
    usern_label.grid(row = 9 ,sticky=W)

    datetime = Label(pro, text=date.today())
    datetime.grid(row=9, sticky=E)


def registracija():
    #pro.destroy()
    top = Tk()
    top.title('ProjectX - Create new User')
    top.iconbitmap('projx.ico')

    def regklik():
        
        korisnickoIme = koime_entry.get()
        sifraNaRegistraciji = sifra_entry.get()
        conn =  sqlite3.connect('glavanabaza.db')
        c = conn.cursor()
        c.execute('SELECT * from korisnici WHERE username="%s"' % (korisnickoIme))
        if c.fetchone() is not None:
            messagebox.showerror(title="Greska!", message="U nasoj bazi podataka već postoji račun sa tim usernameom.")
            print("Postojeci username pri registraciji!")
            return
        if not ime_entry.get() or not ime_entry.get() or not koime_entry.get() or not sifra_entry.get() or not brtel_entry.get():
            messagebox.showerror(title="Prazna polja", message="Niste popunili sva polja! Popunite sva obavezna polja!")
            return
        korisnici.insert(ime_entry.get(),
                         prezime_entry.get(),
                         koime_entry.get(),
                         sifra_entry.get(),
                         brtel_entry.get(),
                         email_entry.get(),
                         level_entry.get())
        messagebox.showinfo(title="Uspješna registracija!", message="Uspješno ste registrovali novi račun u našoj bazi podataka\nSada se možete logovati.")
        top.destroy()


    register_label = Label(top, text="Project X - Registracija.\n Popunite data polja da bi registrovali novi račun..", font=('bold', 12),padx= 5)
    register_label.grid(row = 0, columnspan= 4,pady = 25,padx=5)

    ime_label = Label(top, text="Unesite vaše ime:")
    ime_label.grid(row = 1, column= 0)
    ime_entry= Entry(top)
    ime_entry.grid(row = 1, column= 1, padx= 15)

    prezime_label = Label(top, text="Unesite prezime:")
    prezime_label.grid(row=1, column=2)
    prezime_entry= Entry(top)
    prezime_entry.grid(row=1, column =3, padx=15)

    koime_label = Label(top, text="Unesite korisničko ime:")
    koime_label.grid(row=2, column=0)
    koime_entry=Entry(top)
    koime_entry.grid(row=2, column=1,padx=15)

    sifra_label= Label(top, text="Unesite željenu šifru:")
    sifra_label.grid(row=2, column=2)
    sifra_entry=Entry(top,show='*')
    sifra_entry.grid(row=2, column=3, pady=28)

    brtel_label = Label(top, text="Unesite broj telefona:")
    brtel_label.grid(row=3, column=0)
    brtel_entry=Entry(top)
    brtel_entry.grid(row=3,column=1)

    email_label=Label(top, text="Unesite e-mail(opcionalno):")
    email_label.grid(row=3,column=2)
    email_entry=Entry(top)
    email_entry.grid(row=3, column=3)

    level_label=Label(top, text="Unesite user level:")
    level_label.grid(row=4, column=1, pady=20)
    level_entry=Entry(top)
    level_entry.grid(row=4, column=2)

    regbutton= Button(top, text="Registruj se", width=20, bg="#22b7e0", command=regklik)
    regbutton.grid(row=5, columnspan=4, pady=30)

    top.mainloop()





################################################################ -- kreiramo početni label
login_label = Label(app, text="ProjectX - LogIn.\n Unesite svoje korisničko ime i šifru", font=('bold', 12),padx= 5)
login_label.grid(row = 0, column = 0, columnspan=1,pady = 25,padx=5)

################################################################# -- kreiramo label i entry za korisničko ime aka username..
username_label = Label(app, text="Unesite svoje korisničko ime:", font=('bold', 10))
username_label.grid(row = 1, column = 0, columnspan= 1, pady= 10)
username_text = StringVar()
username_entry = Entry(app, textvariable=username_text)
username_entry.grid(row = 2, column = 0, columnspan = 1, pady= 10)
################################################################# -- kreiramo label i entry za password
password_label = Label(app, text="Unesite svoju lozinku:", font=('bold', 10))
password_label.grid(row=3, column = 0, pady=10)
password_text = StringVar()
password_entry= Entry(app, textvariable= password_text, show='*')
password_entry.grid(row= 4, column=0, pady=10)
################################################################# -- kreiramo dugmice "login" i "register"..
login_button = Button(app, text="Login...", width=12, command=login) # command=login nemoj zaboravit dodat
login_button.grid(row= 6 , column = 0, padx=15, pady= 20)



# pokrecemo applikaciju
app.mainloop()
