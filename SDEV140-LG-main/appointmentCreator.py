from tkinter import *
import tkinter.messagebox
import sqlite3

# defining function to open appointment form in new window
def app_set():
    app_window = Toplevel()
    app_window.title("Create New Appointment")
    app_window.configure(background="#F0E68C")
    app_window.geometry("600x400")

    # Customer First Name field
    customer_first_name_label = Label(app_window, text="Enter Your First Name: ", bg="#F0E68C")
    customer_first_name_entry = Entry(app_window, width=50)
    customer_first_name_label.grid(row=2, column=1, sticky='E', pady=(10, 0))
    customer_first_name_entry.grid(row=2, column=2, sticky='NSEW', pady=(10, 0))

    # Customer Last Name Field
    customer_last_name_label = Label(app_window, text="Enter Your Last Name: ", bg="#F0E68C")
    customer_last_name_entry = Entry(app_window, width=50)
    customer_last_name_label.grid(row=3, column=1, sticky='E', pady=(10, 0))
    customer_last_name_entry.grid(row=3, column=2, sticky='NSEW', pady=(10, 0))

    # Customer Phone Number
    phone_entry_label = Label(app_window, text="Enter Your Phone Number: ", bg="#F0E68C")
    phone_entry_label.grid(row=4, column=1, sticky='E', pady=(10, 0))
    phone_entry = Entry(app_window, width=25)
    phone_entry.grid(row=4, column=2, columnspan=4, sticky='NSEW', pady=(10, 0))

    # Customer Email Address
    email_entry_label = Label(app_window, text="Enter Your Email Address: ", bg="#F0E68C")
    email_entry_label.grid(row=5, column=1, sticky='E', pady=(10, 0))
    email_entry = Entry(app_window, width=25)
    email_entry.grid(row=5, column=2, columnspan=4, sticky='NSEW', pady=(10, 0))

    # Requested Date for Appointment
    date_label = Label(app_window, text="Requested Date (mm/dd/yyyy): ", bg="#F0E68C")
    date_entry = Entry(app_window, width=25)
    date_label.grid(row=6, column=1, sticky='E', pady=(10, 0))
    date_entry.grid(row=6, column=2, sticky='NSEW', pady=(10, 0))

    # Requested Time for Appointment drop down box
    time_label = Label(app_window, text="Available Times: ", bg="#F0E68C")
    time_label.grid(row=7, column=1, sticky='E', pady=(10, 0))
    time_options = ["9:00 AM",
                    "10:00 AM",
                    "11:00 AM",
                    "12:00 PM",
                    "1:00 PM",
                    "2:00 PM",
                    "3:00 PM",
                    "4:00 PM",
                    "5:00 PM"]

    clicked = StringVar()
    drop = OptionMenu(app_window, clicked, *time_options)
    drop.grid(row=7, column=2, sticky='NSEW', pady=(10, 0))

    # Creating function to save collected data
    def enter_data():
        first_name = customer_first_name_entry.get()
        last_name = customer_last_name_entry.get()
        phone_number = phone_entry.get()
        email = email_entry.get()
        date = date_entry.get()
        time = clicked.get()

        connection = sqlite3.connect("appointment_information.db")

        cursor = connection.cursor()

        table_creation = 'CREATE TABLE IF NOT EXISTS appointments (first_name TEXT,' \
                         'last_name TEXT,' \
                         'phone_number INTEGER,' \
                         'email TEXT,' \
                         'date INTEGER,' \
                         'time TEXT) '

        cursor.execute(table_creation)

        data_insert_query = 'INSERT INTO appointments (first_name, last_name, phone_number, email, date, time) ' \
                            'VALUES (?, ?, ?, ?, ?, ?)'
        data_insert_tuple = (first_name, last_name, phone_number, email, date, time)

        cursor = connection.cursor()
        cursor.execute(data_insert_query, data_insert_tuple)
        connection.commit()
        connection.close()
        tkinter.messagebox.showinfo("Attention", "Appointment Scheduled!")

    # function to clear text on submission
    def clear_text():
        text.delete(0, END)

    new_submit = Button(app_window, text="Submit", width=10, background="#BC8F8F", foreground="black",
                        command=lambda: [enter_data(), clear_text()])
    new_submit.grid(row=8, column=2, sticky='NSEW', pady=(10, 0))
