
import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call


def input():
    mysqlDB = mysql.connector.connect(host="localhost", user="root", password="", database="grocermarket")
    cursor = mysqlDB.cursor()
    usename = un.get()
    password = pw.get()

    sql = "SELECT * FROM userAdmin WHERE named = %s AND passW = %s"
    cursor.execute(sql, [(usename), (password)])
    r = cursor.fetchall()

    if r:
        messagebox.showinfo("","Login Successful")
        root.destroy()
        return True
    else:
        messagebox.showinfo(""," INCORRECT USERNAME AND PASSWORD")
        return False

root = Tk()
root.title("Login (test)")
root.geometry("400x300")
global un
global pw

Label(root, text="USERNAME").place(x = 30, y = 30)
Label(root, text="PASSWORD").place(x = 30, y = 60)

un = Entry(root)
un.place(x=140, y=30)

pw = Entry(root)
pw.place(x=140, y=60)
pw.config(show="*")

Button(root, text="Login", command=input, height = 5, width = 25).place(x=30, y=130)

root.mainloop()