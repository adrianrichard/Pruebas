"""
Realaxx Real Estate Appointment App
Lorelei Gatten
This program is intended to allow users to schedule, search, and re-schedule previously set appointments
with a local real estate company."""

# Import necessary libraries and functions
from tkinter import *
from appointmentCreator import app_set
from appointmentSearch import app_find

# Creating main window and setting selections
main_window = Tk()
main_window.title("Realaxx Real Estate Appointment Scheduler")
main_window.configure(bg="#F0E68C")
main_window.geometry("800x500")

# Banner with Company Name
real_Logo = PhotoImage(file="RealaxxLogo.png")
logo_label = Label(image=real_Logo)
logo_label.grid(row=1, column=3, sticky=NSEW)


# Label to direct user to choose which action to take
question_title = Label(main_window, text="What Would You Like to Do?", background="#F0E68C", borderwidth=25, font=85)
question_title.grid(row=2, column=3, ipadx=10, padx=10)

# Button to schedule new appointment
new_appointment_button = Button(background="#BC8F8F", foreground="black", text="Schedule New Appointment",
                                command=app_set)
new_appointment_button.grid(row=3, column=2, padx=(10, 0))

# Button to search scheduled appointments
search_appointment_button = Button(bg="#BC8F8F", fg="black", text="Search For Appointment",
                                   command=app_find)
search_appointment_button.grid(row=3, column=4, pady=(10, 0))


main_window.mainloop()
