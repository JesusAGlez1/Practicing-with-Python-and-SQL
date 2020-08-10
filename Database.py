# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 16:23:32 2020

@author: Strappy
"""
from tkinter import *
from PIL import ImageTk, Image

import sqlite3




root = Tk()
root.geometry("400x250")
root.title("Database")
root.iconbitmap("C://Users/Strappy/Downloads/favicon.ico")

##Database
#Create a database or connect to a new one

conn = sqlite3.connect('Database.db')

#Create a cursor. The cursos is what it does everything for us. VERY IMPORTANT
#Defined c as a variable for the cursor
c = conn.cursor()
'''
c.execute("""CREATE TABLE roomies (
          first_name text,
          last_name text,
          address text,
          city text,
          state text,
          zipcode integer
           )""")
'''

f_name = Entry(root, width=30)
f_name.grid(row=1, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=2, column=1)

address = Entry(root, width=30)
address.grid(row=3, column=1)

city = Entry(root, width=30)
city.grid(row=4, column=1)

state = Entry(root, width=30)
state.grid(row=5, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=6, column=1)

#Create submit function for Database
def submit():
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()



    #Insert into our table
    c.execute("INSERT INTO roomies VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
      {
        'f_name': f_name.get(),
        'l_name': l_name.get(),
        'address': address.get(),
        'city': city.get(),
        'state': state.get(),
        'zipcode': zipcode.get()
      })

    conn.commit()

    conn.close()


    
    #Clear The Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
#Create quuery function
def query():
    conn = sqlite3.connect('Database.db')

    c = conn.cursor()

    #Query the database
    c.execute("SELECT *, oid FROM roomies")
    records = c.fetchall()
    print(records)
    #Loop thru results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + '\n'

        query_label = Label(root, text = print_records)
        query_label.grid(row=9, column=0, columnspan=2)

    conn.commit()
    conn.close()

#Create a Text Box Labels
Space_label = Label(root, text="   ")
Space_label.grid(row=0, column=0)

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=1, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=2, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=3, column=0)

city_label = Label(root, text="City")
city_label.grid(row=4, column=0)

state_label = Label(root, text="State")
state_label.grid(row=5, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=6, column=0)

#Create Submit Button
submit_button = Button(root, text= "Add Record to Database", command=submit)
submit_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)



#Create a query button
query_button = Button(root, text="Show Records", command=query)
query_button.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Commit changes
conn.commit()

#Close Connnection

conn.close()


root.mainloop()
