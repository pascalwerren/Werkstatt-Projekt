from tkinter import *
import os
import sqlite3

def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()

def delete8():
    screen8.destroy()

def delete7():
    screen7.destroy()
  
def login_sucess():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("Erfolgreich angemeldet")
  screen3.geometry("300x100")
  Label(screen3, text = f"Willkommen zurück {userlogged}").pack()
  Button(screen3, text = "Name ändern", command=changename).pack()
  Button(screen3, text = "Passwort ändern", command=changepasswort).pack()
  Button(screen3, text = "Account löschen", command=deleteuser).pack()

def deleteuser():
    global screen8
    screen8 = Toplevel(screen)
    screen8.title("Fehler")
    screen8.geometry("300x100")
    Label(screen8, text = "Benutzer wurde erfolgreich gelöscht").pack()
    Button(screen8, text = "OK", command =delete8).pack()

    command = f"DELETE FROM users WHERE username = '{userlogged}'"
    cursor.execute(command)
    delete2()
    connection.commit()

def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Fehler")
  screen4.geometry("300x100")
  Label(screen4, text = "Das Passwort stimmt nicht!").pack()
  Button(screen4, text = "OK", command =delete3).pack()

def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Fehler")
  screen5.geometry("300x100")
  Label(screen5, text = "Benutzer konnte nicht gefunden werden").pack()
  Button(screen5, text = "OK", command =delete4).pack()

def namechanged():
  global screen9
  screen9 = Toplevel(screen)
  screen9.title("Erfolgreich!")
  screen9.geometry("600x100")
  Label(screen9, text = "Der Name wurde erfolgreich geändert. Beim nächsten einloggen wird der alte Name nicht mehr gehen!").pack()

def pwchanged():
  global screen10
  screen10 = Toplevel(screen)
  screen10.title("Erfolgreich!")
  screen10.geometry("600x100")
  Label(screen10, text = "Das Passwort wurde erfolgreich geändert. Beim nöchsten einloggen wird das alte nicht mehr gehen!").pack()

def changenameindb():
    newname1 = newnamestr.get()
    global userlogged
    oldname = userlogged
    command = f"UPDATE users SET username = '{newname1}' WHERE username = '{oldname}'"
    cursor.execute(command)
    namechanged()
    connection.commit
    userlogged = newname1

def changepasswort():
    global screen7
    global newpw
    screen7 = Toplevel(screen)
    screen7.title("Passwort ändern")
    screen7.geometry("300x100")

    newpw = StringVar()

    Label(screen7, text = "Neues Passwort").pack()
    newpw = Entry(screen7)
    newpw.pack()
    Label(screen7, text = "", textvariable = newpw).pack()
    Button(screen7, text = "Ändern", width = 10, height = 1, command=changepw).pack()

def changepw():
    newpw1 = newpw.get()
    global passwordlogged
    oldpw = passwordlogged
    command = f"UPDATE users SET password = '{newpw1}' WHERE password = '{oldpw}'"
    cursor.execute(command)
    pwchanged()
    connection.commit
    passwordlogged = newpw1
def changename():
  global screen6
  global newnamestr
  global newname
  screen5 = Toplevel(screen)
  screen5.title("Name ändern")
  screen5.geometry("300x100")

  newnamestr = StringVar()

  Label(screen5, text = "Neuer Name").pack()
  newname = Entry(screen5, textvariable = newnamestr)
  newname.pack()
  Label(screen5, text = "").pack()
  Button(screen5, text = "Ändern", width = 10, height = 1, command = changenameindb).pack()

  
def register_user():  
  name = username.get()
  pw = password.get()

  command = f"INSERT INTO users (user_id, username, password) VALUES (NULL, '{name}','{pw}')"
  cursor.execute(command)

  connection.commit()


  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registrierung erfolgreich!", fg = "green" ,font = ("calibri", 11)).pack()

def login_verify():
  
  global userlogged
  global passwordlogged
  username1 = username_verify.get()
  userlogged = username1
  password1 = password_verify.get()
  passwordlogged = password1
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  if userindb(username1):
      if getpw(username1) == password1:
          login_sucess()
      else:
          password_not_recognised()
  else:
      user_not_found()
  


def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Registrieren")
  screen1.geometry("300x250")
  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "").pack()
  Label(screen1, text = "Benutzername").pack()
 
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Passwort").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Registrieren", width = 10, height = 1, command = register_user).pack()

def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Anmelden")
  screen2.geometry("300x250")
  Label(screen2, text = "").pack()

  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1

  Label(screen2, text = "Benutzername").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Passwort").pack()
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen2, text = "").pack()
  Button(screen2, text = "Anmelden", width = 10, height = 1, command = login_verify).pack()

def getpw(username):
    getpw = f"""SELECT password FROM users WHERE username = '{username}'"""

    for row in cursor.execute(getpw):
        pw = row[0]
    return pw
  
def userindb(username):
    userindb = f"SELECT COUNT(*) FROM users WHERE username = '{username}'"

    for row in cursor.execute(userindb):
        isin = row[0]

    if isin >= 1:
        return True
    else:
        return False


def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x190")
  screen.title("Start")
  Label(text = "").pack()
  Button(text = "Anmelden", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Registrieren",height = "2", width = "30", command = register).pack()

  screen.mainloop()

connection = sqlite3.connect("loginregister.db")

cursor = connection.cursor()

tabelle_accounts = """
CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY, username TEXT, password TEXT);"""
cursor.execute(tabelle_accounts)

connection.commit()
main_screen()

