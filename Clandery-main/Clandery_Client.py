import socket
import tkinter as tk
import tkinter.messagebox as mb
import tkinter.font as tkFont
from tkcalendar import Calendar
import calendar
import datetime
import json

logged_user, status_code = " ", " "

def display_system():
    global root1, fontstyle, cal, user_company
    root1 = tk.Tk()
    root1.title("Clandery")
    root1.iconphoto(True, tk.PhotoImage(file='lillogo.png'))
    root1.geometry("1600x800")
    root1.resizable(width=False, height=False)
    message = "rank#get"
    server.send(message.encode())
    user_rank = server.recv(1024).decode() # Getting user's rank
    message = "name#get"
    server.send(message.encode())
    user_name = server.recv(1024).decode()  # Getting user's personal name
    message = "company#get"
    server.send(message.encode())
    user_company = server.recv(1024).decode()  # Getting user's personal name
    fontstyle = tkFont.Font(family="Lucida Grande", size=20)

    # logo
    img = tk.PhotoImage(file="logo.png")
    logo_panel1 = tk.Label(root1, image=img)
    logo_panel1.image = img
    logo_panel1.place(x=0, y=0)

    # logout
    log_out_button = tk.Button(root1, text='Logout', height=2, width=10, command=lambda: root1.destroy())
    log_out_button.place(x=1510, y=10)

    # logged user
    show_user_logged = tk.Label(root1, text="Hello " + user_name + ",", font=fontstyle)
    show_user_logged.place(x=2, y=135)

    # logged user's rank
    show_user_rank = tk.Label(root1, text="Rank: " + str(user_rank), font=fontstyle)
    show_user_rank.place(x=2, y=175)


    # logged user's company
    show_company = tk.Label(root1, text="Company: " + str(user_company), font=fontstyle)
    show_company.place(x=2, y=215)


    # show calender
    server.send("get_date".encode())
    date_message = server.recv(1024).decode().split("-")
    current_year = int(date_message[0])
    current_month = int(date_message[1])
    current_day = int(date_message[2])
    current_date = datetime.date(current_year, current_month, current_day)
    cal = Calendar(root1, selectmode='day', year=current_year, month=current_month, day=current_day)
    cal.place(x=320, y=150, width=600, height=600)
    for row in cal._calendar:
        for lbl in row:
            lbl.bind('<Double-1>', get_cal_date)
    # show events
    if current_month < 10:
        current_month = str(current_month)
        current_month.replace('0', "")
        current_month = int(current_month)
        current_date = f"{str(current_year)}-{current_month}-{current_day}"
    chosen_date = current_date
    refresh(root1, chosen_date, fontstyle, cal, user_company)

    # buttons for admins and owners
    if user_rank == "Admin" or user_rank == "Owner":
        reg_button = tk.Button(root1, text='Create New User', height=2, width=15, command=lambda: (register(user_company)))
        reg_button.place(x=1388, y=10)
        del_button = tk.Button(root1, text='Delete User', height=2, width=10, command=lambda: (delete(user_company)))
        del_button.place(x=1300, y=10)
        add_event_button = tk.Button(root1, text='Add Event', height=2, width=10, command=lambda: (add_event(root1, chosen_date, fontstyle, cal, user_company)))
        add_event_button.place(x=1212, y=10)
        remove_event_button = tk.Button(root1, text='Remove Event', height=2, width=12, command=lambda: (remove_event(chosen_date, root1, cal, user_company)))
        remove_event_button.place(x=1110, y=10)
    if user_rank == "Owner" or user_rank == "Admin" and user_company == "Clandery":
        company_add_button = tk.Button(root1, text='Add Company', height=2, width=12, command=lambda: (add_company()))
        company_add_button.place(x=1005, y=10)
        company_remove_button = tk.Button(root1, text='Remove Company', height=2, width=15,command=lambda: (remove_company()))
        company_remove_button.place(x=880, y=10)
    refresh_button = tk.Button(root1, text='Refresh', height=2, width=8,command=lambda: (refresh(root1, chosen_date, fontstyle, cal, user_company)))
    refresh_button.place(x=985, y=102)
    next_button = tk.Button(root1, text='Next Day', height=2, width=9, command=lambda: (next_day_events(current_date, root1, fontstyle, cal, user_company)))
    next_button.place(x=1360, y=102)
    prev_button = tk.Button(root1, text='Prev Day', height=2, width=9,command=lambda: (prev_day_events(current_date, root1, fontstyle, cal, user_company)))
    prev_button.place(x=1070, y=102)
    root1.mainloop()

def get_cal_date(event):
    month, day, year = cal.get_date().split("/")
    year = int(year)
    year = 2000 + year
    chosen_date = f"{year}-{month}-{day}"
    refresh(root1, chosen_date, fontstyle, cal, user_company)

def next_day_events(current_date, root1, fontstyle, cal, company):
    global chosen_date
    chosen_date = current_date
    year, month, day = chosen_date.split("-")
    year = int(year)
    month = int(month)
    day = int(day)
    try:
        datetime.datetime(year, month, day + 1)
        chosen_date = f"{year}-{month}-{int(day+1)}"
        year = int(year)
        month = int(month)
        day = int(day+1)
        ref_date = datetime.datetime(year, month, day)
        cal.selection_set(ref_date)
    except:
        if int(month) == 12 and int(day) == 31:
            chosen_date = f"{year+1}-{1}-{1}"
            year = int(year + 1)
            month = 1
            day = 1
            ref_date = datetime.datetime(year, month, day)
            cal.selection_set(ref_date)
        else:
            chosen_date = f"{year}-{int(month+1)}-{1}"
            year = int(year)
            month = int(month+1)
            day = 1
            ref_date = datetime.datetime(year, month, day)
            cal.selection_set(ref_date)
    refresh(root1, chosen_date, fontstyle, cal, company)

def prev_day_events(current_date, root1, fontstyle, cal, company):
    chosen_date = current_date
    year, month, day = str(chosen_date).split("-")
    year = int(year)
    month = int(month)
    day = int(day)
    try:
        datetime.datetime(year, month, day - 1)
        chosen_date = f"{year}-{month}-{int(day - 1)}"
        ref_date = datetime.datetime(year, month, day - 1)
        cal.selection_set(ref_date)
    except:
        if int(month) == 1 and int(day) == 1:
            chosen_date = f"{year - 1}-{12}-{31}"
            ref_date = datetime.datetime(int(year - 1), 12, 31)
            cal.selection_set(chosen_date)
        else:
            chosen_date = f"{year}-{int(month - 1)}-{calendar.monthrange(year, month - 1)[1]}"
            ref_date = datetime.datetime(int(year), int(month-1), calendar.monthrange(year, month - 1)[1])
            cal.selection_set(ref_date)
    refresh(root1, chosen_date, fontstyle, cal, company)


def remove_event(chosen_date, root1, cal, company):
    global root2
    root2 = tk.Toplevel()
    root2.title("Remove an event")
    root2.geometry("800x600")
    fontstyle = tkFont.Font(family="Lucida Grande", size=20)

    # logo
    img = tk.PhotoImage(file="logo.png")
    logo_panel2 = tk.Label(root2, image=img)
    logo_panel2.image = img
    logo_panel2.place(x=0, y=0)

    # event name
    event_name_label = tk.Label(root2, text="Event Name", font=fontstyle)
    event_name_box = tk.Entry(root2, bg="grey", font=fontstyle)
    event_name_label.place(x=318, y=250)
    event_name_box.place(x=250, y=290)

    # remove button
    remove_button = tk.Button(root2, text='Remove Event', height=2, width=20, command=lambda: (removing_event(event_name_box.get(), chosen_date, root1, fontstyle, cal, company)))
    remove_button.place(x=325, y=335)


def remove_company():
    global root2
    root2 = tk.Toplevel()
    root2.title("Remove an company")
    root2.geometry("800x600")
    fontstyle = tkFont.Font(family="Lucida Grande", size=20)

    # logo
    img = tk.PhotoImage(file="logo.png")
    logo_panel2 = tk.Label(root2, image=img)
    logo_panel2.image = img
    logo_panel2.place(x=0, y=0)

    # company name
    company_name_label = tk.Label(root2, text="Company Name", font=fontstyle)
    company_name_box = tk.Entry(root2, bg="grey", font=fontstyle)
    company_name_label.place(x=318, y=250)
    company_name_box.place(x=250, y=290)

    # remove button
    remove_button = tk.Button(root2, text='Remove Company', height=2, width=20, command=lambda: (removing_company(company_name_box.get())))
    remove_button.place(x=325, y=335)


def refresh(root1, chosen_date, fontstyle, cal, company):
    fontstyle1 = tkFont.Font(family="Lucida Grande", size=12)
    events_frame = tk.Canvas(root1, width=550, height=750)
    events_frame.create_rectangle(0, 0, 550, 700, fill="white", outline='black')
    events_frame.place(x=975, y=90)
    events_text = tk.Label(root1, text="Today's events", font=fontstyle, background='white')
    events_text.place(x=1161, y=95)
    current_text = tk.Label(root1, text=f"Date : {chosen_date}", font=fontstyle1, background='white')
    current_text.place(x=1185, y=135)
    refresh_button = tk.Button(root1, text='Refresh', height=2, width=8,command=lambda: (refresh(root1, chosen_date, fontstyle, cal, company)))
    refresh_button.place(x=985, y=102)
    next_button = tk.Button(root1, text='Next Day', height=2, width=9, command=lambda: (next_day_events(chosen_date, root1, fontstyle, cal, company)))
    next_button.place(x=1360, y=102)
    prev_button = tk.Button(root1, text='Prev Day', height=2, width=9, command=lambda: (prev_day_events(chosen_date, root1, fontstyle, cal, company)))
    prev_button.place(x=1070, y=102)
    server.send(f"get_events#{chosen_date}#{company}".encode())
    events = json.loads(server.recv(1024).decode())
    if events == "no_events":
        no_events_text = tk.Label(root1, text="No Events today", font=fontstyle, background='white')
        no_events_text.place(x=1140, y=160)
    else:
        events = sorted(events, key=sort_events)
        if range(len(events) <= 17):
            for i in range(len(events)):

                event_name = events[i][0]
                event_date = events[i][1]
                event_time = events[i][2]

                event_name_text = tk.Label(root1, text=event_name, font=fontstyle, background='white')
                event_name_text.place(x=990, y=156 + (i * 35))
                event_date_text = tk.Label(root1, text=event_date, font=fontstyle, background='white')
                event_date_text.place(x=1183, y=156 + (i * 35))
                event_time_text = tk.Label(root1, text=event_time, font=fontstyle, background='white')
                event_time_text.place(x=1435, y=156 + (i * 35))
        else:
            for i in range(17):
                event_name = events[i][0]
                event_date = events[i][1]
                event_time = events[i][2]

                event_name_text = tk.Label(root1, text=event_name, font=fontstyle, background='white')
                event_name_text.place(x=990, y=156 + (i * 35))
                event_date_text = tk.Label(root1, text=event_date, font=fontstyle, background='white')
                event_date_text.place(x=1183, y=156 + (i * 35))
                event_time_text = tk.Label(root1, text=event_time, font=fontstyle, background='white')
                event_time_text.place(x=1435, y=156 + (i * 35))

def sort_events(event):
    hour, min = event[2].split(":")
    date_time = datetime.time(int(hour), int(min))
    return date_time

def removing_event(name, chosen_date, root1, fontstyle, cal, company):
    if name != "" and len(name) > 2:
        message = f"delete_event#{name}#{company}"
        server.send(message.encode())
        answer = server.recv(1024).decode().split("#")
        answer[1] = answer[1].replace("\'", "")
        answer[1] = answer[1].replace("(", "")
        answer[1] = answer[1].replace(")", "")
        answer[1] = answer[1].replace(",", "")
        deleted_date = answer[1]
        deleted_date = deleted_date.replace("[", "")
        deleted_date = deleted_date.replace("]", "")
        if answer[0] == "event_deleted":
            success_msg = "The event has been deleted successfully!"
            mb.showinfo(title="Event Deleted", message=success_msg)
            if deleted_date == chosen_date:
                refresh(root1, chosen_date, fontstyle, cal, company)
            root2.destroy()
        elif answer[0] == "event_not_exist":
            fail_msg = "There is no event on this name"
            mb.showinfo(title="Please try again", message=fail_msg)
    elif name != "" and len(name) <= 2:
        fail_msg = "Please give a longer name"
        mb.showinfo(title="Please fix the name", message=fail_msg)
    else:
        fail_msg = "Please fill the name box"
        mb.showinfo(title="Please fill", message=fail_msg)


def removing_company(name):
    if name != "" and len(name) > 2 and name != "Clandery":
        message = f"delete_company#{name}"
        server.send(message.encode())
        answer = server.recv(1024).decode().split("#")
        if answer[0] == "company_deleted":
            success_msg = "Company successfully deleted"
            mb.showinfo(title="Success!", message=success_msg)
        elif answer[0] == "company_not_exist":
            fail_msg = "There is no company on this name"
            mb.showinfo(title="Please try again", message=fail_msg)
        elif answer[0] == "company_clandery":
            fail_msg = "Company can't be deleted"
            mb.showinfo(title="Please try again", message=fail_msg)
    elif name != "" and len(name) <= 2:
        fail_msg = "Please give a longer name"
        mb.showinfo(title="Please fix the name", message=fail_msg)
    else:
        fail_msg = "Please fill the name box"
        mb.showinfo(title="Please fill", message=fail_msg)


def add_company():
    global root2
    root2 = tk.Toplevel()
    root2.title("Register a new company")
    root2.geometry("800x700")
    fontstyle = tkFont.Font(family="Lucida Grande", size=20)

    # logo
    img = tk.PhotoImage(file="logo.png")
    logo_panel2 = tk.Label(root2, image=img)
    logo_panel2.image = img
    logo_panel2.pack(side="top", anchor="nw")

    # company name
    company_label = tk.Label(root2, text="Company Name:", font=fontstyle)
    company_box = tk.Entry(root2, bg="grey", font=fontstyle)
    company_label.pack()
    company_box.pack()

    # user name
    user_label = tk.Label(root2, text="Username:", font=fontstyle)
    user_box = tk.Entry(root2, bg="grey", font=fontstyle)
    user_label.pack()
    user_box.pack()

    # personal name
    name_label = tk.Label(root2, text="Personal name:", font=fontstyle)
    name_box = tk.Entry(root2, bg="grey", font=fontstyle)
    name_label.pack()
    name_box.pack()

    # email
    email_label = tk.Label(root2, text="Email:", font=fontstyle)
    email_box = tk.Entry(root2, bg="grey", font=fontstyle)
    email_label.pack()
    email_box.pack()

    # password
    pass_label1 = tk.Label(root2, text="Password:", font=fontstyle)
    pass_box1 = tk.Entry(root2, bg="grey", font=fontstyle, show="*")
    pass_label1.pack()
    pass_box1.pack()

    # confirm password
    pass_label2 = tk.Label(root2, text="Confirm Password:", font=fontstyle)
    pass_box2 = tk.Entry(root2, bg="grey", font=fontstyle, show="*")
    pass_label2.pack()
    pass_box2.pack()

    # create button
    create_button = tk.Button(root2, text='Create User', height=2, width=20, command=lambda: (create_company(company_box.get(), user_box.get(), name_box.get(), email_box.get(), pass_box1.get(), pass_box2.get())))
    create_button.pack()

    root2.mainloop()  # run tkinter display

def create_company(company, username, name, email, password, confirm_password):
    message = f"add_company#{username}#{name}#{email}#{password}#{confirm_password}#{company}"
    if username != "" and name != "" and email != "" and password != "" and confirm_password != "":
        server.send(message.encode())
        answer = server.recv(1024).decode()
        answer = answer.split("#")
        if answer[0] == "True":
            success_msg = "User has been created successfully!"
            mb.showinfo(title="New User Created", message=success_msg)
            root2.destroy()
        else:
            if answer[1] == "username" and answer[2] == "email":
                fail_msg = "Username and email already exist"
                mb.showinfo(title="Please try again", message=fail_msg)
            elif answer[1] == "username" and answer[2] != "email":
                fail_msg = "Username already exist"
                mb.showinfo(title="Please try again", message=fail_msg)
            elif answer[1] == "email" and answer[2] != "username":
                fail_msg = "Email already exist"
                mb.showinfo(title="Please try again", message=fail_msg)
            elif answer[1] == "company" and answer[2] != "username" and answer[2] != "email":
                fail_msg = "Company already exist"
                mb.showinfo(title="Please try again", message=fail_msg)
            elif answer[1] == "company" and answer[2] == "username":
                fail_msg = "Company and username already exist"
                mb.showinfo(title="Please try again", message=fail_msg)
            elif answer[1] == "company" and answer[2] == "email":
                fail_msg = "Company and email already exist"
                mb.showinfo(title="Please try again", message=fail_msg)
            elif answer[1] == "username" and answer[2] == "email" and answer[3] == "company":
                fail_msg = "Company, Username and email already exist"
                mb.showinfo(title="Please try again", message=fail_msg)
            elif answer[1] == "password":
                fail_msg = "Both passwords aren't the same"
                mb.showinfo(title="Please try again", message=fail_msg)
            elif answer[1] == "passwordlen":
                fail_msg = "Password length should be under 15 chars"
                mb.showinfo(title="Please try again", message=fail_msg)
            elif answer[1] == "email_false":
                fail_msg = "It's not a vaild mail"
                mb.showinfo(title="Please try again", message=fail_msg)
            elif answer[1] == "pass":
                fail_msg = "It's not a vaild password, password can't contain symbols such as !,* and etc"
                mb.showinfo(title="Please try again", message=fail_msg)
    else:
        fail_msg = "Please fill all the boxes"
        mb.showinfo(title="Please try again", message=fail_msg)


def add_event(root1, chosen_date, fontstyle, cal, company):
    global root2
    root2 = tk.Toplevel()
    root2.title("Add a new event")
    root2.geometry("800x600")

    # logo
    img = tk.PhotoImage(file="logo.png")
    logo_panel2 = tk.Label(root2, image=img)
    logo_panel2.image = img
    logo_panel2.place(x=0, y=0)

    # event name
    event_name_label = tk.Label(root2, text="Event Name", font=fontstyle)
    event_name_box = tk.Entry(root2, bg="grey", font=fontstyle)
    event_name_label.place(x=318, y=110)
    event_name_box.place(x=250, y=150)

    # date
    day_label = tk.Label(root2, text="Day", font=fontstyle)
    day_label.place(x=245, y=210)
    month_label = tk.Label(root2, text="Month", font=fontstyle)
    month_label.place(x=350, y=210)
    year_label = tk.Label(root2, text="Year", font=fontstyle)
    year_label.place(x=483, y=210)
    days_choices = []
    for i in range(calendar.monthrange(2022, 1)[1]):
        days_choices.append(i + 1)
    day = tk.StringVar(root2)
    day.set(days_choices[0])
    cb_days = tk.OptionMenu(root2, day, *days_choices)
    cb_days.place(x=250, y=265)

    month_choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    month = tk.StringVar(root2)
    month.set(month_choices[0])
    cb_month = tk.OptionMenu(root2, month, *month_choices)
    cb_month.place(x=368, y=265)

    year = tk.StringVar(root2)
    year_now = datetime.datetime.now().year
    year_choices = []
    for i in range(11):
        year_choices.append(year_now)
        year_now += 1
    year.set(year_choices[0])
    cb_year = tk.OptionMenu(root2, year, *year_choices)
    cb_year.place(x=485, y=265)

    # time
    time_label = tk.Label(root2, text="Time", font=fontstyle)
    time_label.place(x=360, y=320)
    hour = tk.StringVar(root2)
    hour_choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    hour.set(hour_choices[0])
    cb_hour = tk.OptionMenu(root2, hour, *hour_choices)
    cb_hour.place(x=340, y=370)

    min = tk.StringVar(root2)
    min_choices = ["00", ]
    for i in range(59):
        if i+1 < 10:
            min_choices.append("0" + str(i+1))
        else:
            min_choices.append(str(i + 1))
    min.set(min_choices[0])
    cb_min = tk.OptionMenu(root2, min, *min_choices)
    cb_min.place(x=405, y=370)
    time_label = tk.Label(root2, text=":", font=fontstyle)
    time_label.place(x=390, y=365)

    # add button
    add_button = tk.Button(root2, text='Add Event', height=2, width=20, command=lambda: (adding_event(event_name_box.get(), day.get(), month.get(), year.get(), hour.get(), min.get(), root1, chosen_date, fontstyle, cal, company)))
    add_button.place(x=325, y=425)


def adding_event(name, day, month, year, hour, min, root1, chosen_date, fontstyle, cal, company):
    date = f"{year}-{month}-{day}"
    time = f"{hour}:{min}"
    if name != "" and date != "" and time != "" and len(name) > 2 and len(name) < 13:
        message = f"add_event#{name}#{date}#{time}#{company}"
        server.send(message.encode())
        message = server.recv(1024).decode().split("#")
        if message[0] == "event_added":
            success_msg = "Event has been created successfully!"
            mb.showinfo(title="New Event Created", message=success_msg)
            if int(day) == datetime.datetime.now().day and int(month) == datetime.datetime.now().month and int(year) == datetime.datetime.now().year:
                refresh(root1, chosen_date, fontstyle, cal, company)
            root2.destroy()
        elif message[0] == "name_exist":
            fail_msg = "There is an event called on this name which is more then 2 chars"
            mb.showinfo(title="Please change event name", message=fail_msg)
        elif message[0] == "invaild_time":
            fail_msg = "Please make sure that the event time is in the future"
            mb.showinfo(title="Please try again", message=fail_msg)
        elif message[0] == "invaild_date":
            fail_msg = "Invaild date, please change to a vaild date"
            mb.showinfo(title="Please try again", message=fail_msg)
    elif name != "" and date != "" and time != "" and len(name) <= 2:
        fail_msg = "Please give the event longer name"
        mb.showinfo(title="Please try again", message=fail_msg)
    elif name != "" and date != "" and time != "" and len(name) >= 13:
        fail_msg = "Please give the event shorter name which is less then 13 chars"
        mb.showinfo(title="Please try again", message=fail_msg)
    else:
        fail_msg = "Please fill all the boxes"
        mb.showinfo(title="Please try again", message=fail_msg)


def register(company):
    global root2
    root2 = tk.Toplevel()
    root2.title("Register a new user")
    root2.geometry("800x600")
    fontstyle = tkFont.Font(family="Lucida Grande", size=20)

    # logo
    img = tk.PhotoImage(file="logo.png")
    logo_panel2 = tk.Label(root2, image=img)
    logo_panel2.image = img
    logo_panel2.pack(side="top", anchor="nw")

    # user name
    user_label = tk.Label(root2, text="Username:", font=fontstyle)
    user_box = tk.Entry(root2, bg="grey", font=fontstyle)
    user_label.pack()
    user_box.pack()

    # personal name
    name_label = tk.Label(root2, text="Personal name:", font=fontstyle)
    name_box = tk.Entry(root2, bg="grey", font=fontstyle)
    name_label.pack()
    name_box.pack()

    # email
    email_label = tk.Label(root2, text="Email:", font=fontstyle)
    email_box = tk.Entry(root2, bg="grey", font=fontstyle)
    email_label.pack()
    email_box.pack()

    # password
    pass_label1 = tk.Label(root2, text="Password:", font=fontstyle)
    pass_box1 = tk.Entry(root2, bg="grey", font=fontstyle, show="*")
    pass_label1.pack()
    pass_box1.pack()

    # confirm password
    pass_label2 = tk.Label(root2, text="Confirm Password:", font=fontstyle)
    pass_box2 = tk.Entry(root2, bg="grey", font=fontstyle, show="*")
    pass_label2.pack()
    pass_box2.pack()

    # create button
    create_button = tk.Button(root2, text='Create User', height=2, width=20,command=lambda: (create_user(user_box.get(), name_box.get(), email_box.get(), pass_box1.get(), pass_box2.get(), company)))
    create_button.pack()

    root2.mainloop()  # run tkinter display


def create_user(username, name, email, password, confirm_password, company):
    message = f"check_exist#{username}#{name}#{email}#{password}#{confirm_password}#{company}"
    if username != "" and name != "" and email != "" and password != "" and confirm_password != "":
        server.send(message.encode())
        answer = server.recv(1024).decode()
        answer = answer.split("#")
        if answer[0] == "True":
            success_msg = "User has been created successfully!"
            mb.showinfo(title="New User Created", message=success_msg)
            root2.destroy()
        else:
            if answer[1] == "username" and answer[2] == "email":
                fail_msg = "Username and email already exist"
                mb.showinfo(title="Please try again", message=fail_msg)
            elif answer[1] == "username" and answer[2] != "email":
                fail_msg = "Username already exist"
                mb.showinfo(title="Please try again", message=fail_msg)
            elif answer[1] == "email" and answer[2] != "username":
                fail_msg = "Email already exist"
                mb.showinfo(title="Please try again", message=fail_msg)
            elif answer[1] == "password":
                fail_msg = "Both passwords aren't the same"
                mb.showinfo(title="Please try again", message=fail_msg)
            elif answer[1] == "passwordlen":
                fail_msg = "Password length should be under 15 chars"
                mb.showinfo(title="Please try again", message=fail_msg)
            elif answer[1] == "email_false":
                fail_msg = "It's not a vaild mail"
                mb.showinfo(title="Please try again", message=fail_msg)
            elif answer[1] == "pass":
                fail_msg = "It's not a vaild password, password can't contain symbols such as !,* and etc"
                mb.showinfo(title="Please try again", message=fail_msg)
    else:
        fail_msg = "Please fill all the boxes"
        mb.showinfo(title="Please try again", message=fail_msg)


def delete(company):
    global root2
    root2 = tk.Toplevel()
    root2.title("Delete a user")
    root2.geometry("450x450")
    fontstyle = tkFont.Font(family="Lucida Grande", size=20)

    # logo
    img = tk.PhotoImage(file="logo.png")
    logo_panel2 = tk.Label(root2, image=img)
    logo_panel2.image = img
    logo_panel2.pack(side="top", anchor="nw")

    # user name
    user_label = tk.Label(root2, text="Username:", font=fontstyle)
    user_box = tk.Entry(root2, bg="grey", font=fontstyle)
    user_label.pack()
    user_box.pack()

    # delete button
    delete_button = tk.Button(root2, text='Delete User', height=2, width=20,command=lambda: (delete_user(user_box.get(), company)))
    delete_button.pack()

    root2.mainloop()  # run tkinter display


def delete_user(username, company):
    message = f"deleteuser#{username}#{company}"
    if username != "":
        server.send(message.encode())
        answer = server.recv(1024).decode()
        answer = answer.split("#")
        if answer[0] == "True":
            success_msg = f"The User {username} has been deleted successfully!"
            mb.showinfo(title="User deleted", message=success_msg)
            root2.destroy()
        elif answer[0] == "No_User":
            fail_msg = "This user exist but he is not in your company"
            mb.showinfo(title="Please try again", message=fail_msg)
        else:
            fail_msg = "This user does not exist"
            mb.showinfo(title="Please try again", message=fail_msg)
    else:
        fail_msg = "Please write a username"
        mb.showinfo(title="Please try again", message=fail_msg)

def forgot_screen():
    global root_pass, logo_pass_panel, user_pass_label, user_pass_box, email_pass_label, email_pass_box, reset_pass_button
    root_pass = tk.Toplevel()
    root_pass.title("Forgot Password")
    root_pass.geometry("450x450")
    fontstyle = tkFont.Font(family="Lucida Grande", size=20)

    # logo
    img = tk.PhotoImage(file="logo.png")
    logo_pass_panel = tk.Label(root_pass, image=img)
    logo_pass_panel.image = img
    logo_pass_panel.pack(side="top", anchor="nw")

    # user name
    user_pass_label = tk.Label(root_pass, text="Username:", font=fontstyle)
    user_pass_box = tk.Entry(root_pass, bg="grey", font=fontstyle)
    user_pass_label.pack()
    user_pass_box.pack()

    # email
    email_pass_label = tk.Label(root_pass, text="Email:", font=fontstyle)
    email_pass_box = tk.Entry(root_pass, bg="grey", font=fontstyle)
    email_pass_label.pack()
    email_pass_box.pack()

    # send button
    reset_pass_button = tk.Button(root_pass, text='Send', height=2, width=20,command=lambda: (send_forgot_pass(user_pass_box.get(), email_pass_box.get())))
    reset_pass_button.pack()

def display_pass_verification():
    global logo_panel_vef, code_pass_label, code_pass_label1, code_pass_box, send_pass_button

    # initiate and display all objects on screen
    fontstyle = tkFont.Font(family="Lucida Grande", size=16)
    fontstyle1 = tkFont.Font(family="Lucida Grande", size=14)

    # logo
    img = tk.PhotoImage(file="logo.png")
    logo_panel_vef = tk.Label(root_pass, image=img)
    logo_panel_vef.image = img
    logo_panel_vef.pack(side="top", anchor="nw")

    # Code Verify Text
    code_pass_label = tk.Label(root_pass, text=" Verification Code Has been sent to your email", font=fontstyle)
    code_pass_label1 = tk.Label(root_pass, text=" Please enter the code in order to reset your password", font=fontstyle1)
    code_pass_box = tk.Entry(root_pass, bg="grey", font=fontstyle)

    # login button
    send_pass_button = tk.Button(root_pass, text='Enter', height=2, width=20, command=lambda: (send_pass_code(code_pass_box.get())))

    code_pass_label.pack()
    code_pass_label1.pack()
    code_pass_box.pack()
    send_pass_button.pack()

def change_password_screen():
    global root_pass, logo_pass_panel, user_pass_label, user_pass_box, email_pass_label, email_pass_box, reset_pass_button

    fontstyle = tkFont.Font(family="Lucida Grande", size=20)
    # logo
    img = tk.PhotoImage(file="logo.png")
    logo_change_panel = tk.Label(root_pass, image=img)
    logo_change_panel.image = img
    logo_change_panel.pack(side="top", anchor="nw")

    # pass1
    show_pass_button1 = tk.Button(root_pass, text='Show Password', height=1, width=12, command=lambda: show_pass(show_pass_button1, pass1_box))
    pass1_label = tk.Label(root_pass, text="Password:", font=fontstyle)
    pass1_box = tk.Entry(root_pass, bg="grey", font=fontstyle, show="*")
    pass1_label.pack()
    show_pass_button1.pack()
    pass1_box.pack()

    # pass2
    show_pass_button2 = tk.Button(root_pass, text='Show Password', height=1, width=12, command=lambda: show_pass(show_pass_button2, pass2_box))
    pass2_label = tk.Label(root_pass, text="Confirm Password:", font=fontstyle)
    pass2_box = tk.Entry(root_pass, bg="grey", font=fontstyle, show="*")
    pass2_label.pack()
    show_pass_button2.pack()
    pass2_box.pack()

    # send button
    reset_pass_button = tk.Button(root_pass, text='Change', height=2, width=20, command=lambda: (send_new_pass(pass1_box.get(), pass2_box.get())))
    reset_pass_button.pack()

def send_new_pass(pass1, pass2):
    message = "newpass#" + str(username_change) + "#" + str(pass1) + "#" + str(pass2)
    server.send(message.encode())  # Sending the data to the server
    status_reset = server.recv(1024).decode()
    if status_reset == "True":
        success_msg = "Password has changed successfully!"
        mb.showinfo(title="Congrats", message=success_msg)
        root_pass.destroy()
    elif status_reset == "False#password":
        fail_msg = "The Passwords don't match!"
        mb.showinfo(title="Operation Failed", message=fail_msg)
    elif status_reset == "False#passwordlen":
        fail_msg = "One or Both of the passwords are too long"
        mb.showinfo(title="Operation Failed", message=fail_msg)


def send_pass_code(code):
    message = "passcode#" + str(code)
    server.send(message.encode())  # Sending the data to the server
    status_code = server.recv(1024).decode()
    if status_code == "True":
        logo_panel_vef.destroy()
        code_pass_label.destroy()
        code_pass_label1.destroy()
        code_pass_box.destroy()
        send_pass_button.destroy()
        change_password_screen()
    else:
        fail_msg = "The code was incorrect"
        mb.showinfo(title="Please try again", message=fail_msg)

def send_forgot_pass(username, email):
    global username_change
    username_change = username
    message = "resetpass#" + str(username) + "#" + str(email)
    server.send(message.encode())  # Sending the data to the server
    status_reset = server.recv(1024).decode()
    if status_reset == "True":
        forgot_pass_off()
        display_pass_verification()
    else:
        fail_msg = "The details are incorrect"
        mb.showinfo(title="Please try again", message=fail_msg)

def forgot_pass_off(): # clearing the info
    logo_pass_panel.destroy()
    user_pass_label.destroy()
    user_pass_box.destroy()
    email_pass_label.destroy()
    email_pass_box.destroy()
    reset_pass_button.destroy()

def display_login():  # displaying the window of login into the system
    global log_button, user_label, user_box, pass_label, pass_box, logo_panel_login, show_pass_button, forgot_password_button
    # initiate and display all objects on screen
    root.resizable(width=False, height=False)
    root.iconphoto(True, tk.PhotoImage(file='lillogo.png'))
    fontstyle = tkFont.Font(family="Lucida Grande", size=20)

    # logo
    img = tk.PhotoImage(file="logo.png")
    logo_panel_login = tk.Label(root, image=img)
    logo_panel_login.image = img
    logo_panel_login.place(x=0, y=0)

    # user name
    user_label = tk.Label(root, text="Username:", font=fontstyle)
    user_box = tk.Entry(root, bg="grey", font=fontstyle)
    user_label.place(x=235, y=140)
    user_box.place(x=150, y=180)

    # password
    pass_label = tk.Label(root, text="Password:", font=fontstyle)
    pass_box = tk.Entry(root, bg="grey", font=fontstyle, show="*")
    pass_label.place(x=235, y=225)
    pass_box.place(x=150, y=265)

    # show password
    show_pass_button = tk.Button(root, text='Show Password', height=1, width=12, command=lambda: show_pass(show_pass_button, pass_box))
    show_pass_button.place(x=465, y=270)

    # forgot password
    forgot_password_button = tk.Button(root, text='forgot password', height=1, width=12, command=lambda: forgot_screen())
    forgot_password_button.place(x=355, y=310)

    # login button
    log_button = tk.Button(root, text='Login', height=2, width=20, command=lambda: (login(user_box.get(), pass_box.get())))
    log_button.place(x=227, y=370)


def show_pass(pass_button, pass_box):
    if pass_box['show'] == '':
        pass_box['show'] = '*'
        pass_button.config(text="Show Password")
    else:
        pass_box['show'] = ''
        pass_button.config(text="Hide Password")


def login_frame_off():
    user_label.place_forget()
    user_box.place_forget()
    pass_label.place_forget()
    pass_box.place_forget()
    show_pass_button.place_forget()
    forgot_password_button.place_forget()
    log_button.place_forget()
    logo_panel_login.place_forget()


def display_verification():
    # initiate and display all objects on screen
    fontstyle = tkFont.Font(family="Lucida Grande", size=20)

    # logo
    img = tk.PhotoImage(file="logo.png")
    logo_panel_verify = tk.Label(root, image=img)
    logo_panel_verify.image = img
    logo_panel_verify.pack(side="top", anchor="nw")

    # Code Verify Text
    code_label = tk.Label(root, text=" Verification Code Has been sent to your email", font=fontstyle)
    code_label1 = tk.Label(root, text=" Please enter the code to login into your account", font=fontstyle)
    code_box = tk.Entry(root, bg="grey", font=fontstyle)

    # login button
    send_button = tk.Button(root, text='Login', height=2, width=20, command=lambda: (send_code(code_box.get())))

    code_label.pack()
    code_label1.pack()
    code_box.pack()
    send_button.pack()


def send_code(code):
    global status_code
    message = "code#" + str(code)
    server.send(message.encode())  # Sending the data to the server
    status_code = server.recv(1024).decode()
    if status_code == "True":
        success_msg = f"Hello {logged_user}, Code was correct!"
        mb.showinfo(title="login succeed!", message=success_msg)
        root.destroy()
    else:
        fail_msg = "The code was incorrect"
        mb.showinfo(title="Please try again", message=fail_msg)


def login(user, password):
    global logged_user
    if user != "" and password != "":
        message = "login#"+str(user)+"#"+str(password)
        server.send(message.encode())  # Sending the data to the server
        status = server.recv(1024).decode() # Getting data from the server
        if status == "True":
            logged_user = user
            success_msg = f"Hello {logged_user}, you logged in successfully!"
            mb.showinfo(title="login succeed!", message=success_msg)
            login_frame_off()
            display_verification()
        elif status == "False_logged":
            warning_msg = "User already logged into our system"
            mb.showwarning(title="Please try again!", message=warning_msg)
        else:
            warning_msg = "Please try again!"
            mb.showwarning(title="Incorrect username or password", message=warning_msg)
    else:
        fail_msg = "Please make sure you have entered username and password in both fields!"
        mb.showinfo(title="Enter username and password", message=fail_msg)


if __name__ == '__main__':
    # Socket settings
    server = socket.socket (socket.AF_INET, socket.SOCK_STREAM)  # setting the socket
    server.connect(('127.0.0.1', 25565))  # joining the main command server
    print("Connected to the server successfully!")
    root = tk.Tk()
    root.title("Clandery Login")
    root.geometry("600x450")
    display_login()
    root.mainloop()  # run tkinter display
    if logged_user != " " and status_code == "True":
        display_system()
    server.close()
