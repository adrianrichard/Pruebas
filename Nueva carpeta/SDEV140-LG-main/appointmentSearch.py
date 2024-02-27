from tkinter import *
import sqlite3

conn = sqlite3.connect('appointment_information.db')
c = conn.cursor()

# defining function to open appointment form in new window
def app_find():
    find_window = Toplevel()
    find_window.title("Search for a Scheduled Appointment")
    find_window.configure(background="#F0E68C")
    find_window.geometry("600x400")

    # Customer Name field
    # Customer First Name field
    customer_first_name_label = Label(find_window, text="Enter Your First Name: ", bg="#F0E68C")
    customer_first_name_entry = Entry(find_window, width=50)
    customer_first_name_label.grid(row=2, column=1, sticky='E', pady=(10, 0))
    customer_first_name_entry.grid(row=2, column=2, sticky='NSEW', pady=(10, 0))

    # Customer Last Name Field
    customer_last_name_label = Label(find_window, text="Enter Your Last Name: ", bg="#F0E68C")
    customer_last_name_entry = Entry(find_window, width=50)
    customer_last_name_label.grid(row=3, column=1, sticky='E', pady=(10, 0))
    customer_last_name_entry.grid(row=3, column=2, sticky='NSEW', pady=(10, 0))

    # Customer Phone Number
    phone_entry_label = Label(find_window, text="Enter Your Phone Number: ", bg="#F0E68C")
    phone_entry_label.grid(row=4, column=1, sticky='E', pady=(10, 0))
    phone_entry = Entry(find_window, width=25)
    phone_entry.grid(row=4, column=2, columnspan=4, sticky='NSEW', pady=(10, 0))

    # Customer Email Address
    email_entry_label = Label(find_window, text="Enter Your Email Address: ", bg="#F0E68C")
    email_entry_label.grid(row=5, column=1, sticky='E', pady=(10, 0))
    email_entry = Entry(find_window, width=25)
    email_entry.grid(row=5, column=2, columnspan=4, sticky='NSEW', pady=(10, 0))

    # Searching database using customer input
    def data_retrieval():
        c.execute('SELECT * FROM appointments WHERE first_name LIKE ? AND last_name LIKE ?'
                  'AND phone_number LIKE ? AND email LIKE ?',
                  (customer_first_name_entry.get(), customer_last_name_entry.get(), phone_entry.get(), email_entry.get(),))
        get_records = c.fetchone()
        search_win = Toplevel()
        search_win.configure(background="#F0E68C")
        search_win.geometry("600x400")
        search_display = Text(search_win, height = 200, width = 200)
        search_display.pack()
        search_display.insert("1.0", get_records)
        conn.commit()
        conn.close()

    # Function to clear text on submission
    def clear_text():
        text.delete(0, END)

    new_search = Button(find_window, text="Search", width=10, background="#BC8F8F", foreground="black",
                        command=lambda: [data_retrieval(), clear_text()])
    new_search.grid(row=6, column=2, sticky='NSEW', pady=(10, 0))

