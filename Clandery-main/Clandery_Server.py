import socket
import json
import datetime
import sqlite3
import threading
import smtplib
import random
import re
import hashlib

id = 0

global server_open

# Class

class Client(object):
    def __init__(self, id):
        self.id = id
        self.code = 0
        self.username = " "
        self.name = " "
        self.email = " "
        self.rank = " "
        self.company = " "

    def set_code(self,code):
        self.code = code

    def set_client_info(self, logged_user, c):
        c.execute("SELECT rank FROM users WHERE username = ?", [logged_user])
        rank = str(c.fetchall()[0])
        # Fixing a bug
        rank = rank.replace("\'", "")
        rank = rank.replace("(", "")
        rank = rank.replace(")", "")
        rank = rank.replace(",", "")

        self.rank = rank

        c.execute("SELECT email FROM users WHERE username = ?", [logged_user])
        email = str(c.fetchall()[0])
        # Fixing a bug
        email = email.replace("\'", "")
        email = email.replace("(", "")
        email = email.replace(")", "")
        email = email.replace(",", "")

        self.email = email

        self.username = logged_user

        c.execute("SELECT realname FROM users WHERE username = ?", [logged_user])
        realname = str(c.fetchall()[0])
        # Fixing a bug
        realname = realname.replace("\'", "")
        realname = realname.replace("(", "")
        realname = realname.replace(")", "")
        realname = realname.replace(",", "")

        self.name = realname

        c.execute("SELECT company FROM users WHERE username = ?", [logged_user])
        company = str(c.fetchall()[0])
        # Fixing a bug
        company = company.replace("\'", "")
        company = company.replace("(", "")
        company = company.replace(")", "")
        company = company.replace(",", "")

        self.company = company

class Server(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server_open = True
        self.client_count = 0
        self.client_list = [" "]

    def start(self):
        global id
        try:
            # Socket settings
            my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket setting
            my_socket.bind((self.ip, self.port))  # binding the server ip
            my_socket.listen(3)  # how much people can join the server
            print("Server Open")  # prints that the server is open
            while True:
                if self.client_count == 0:
                    print("Waiting for clients...")
                client_socket, client_address = my_socket.accept()  # accepting the people if the server is available
                id += 1
                self.client_count += 1  # adding to the count of the clients inside the server when the server accepted new client
                print(f"A new client connected to the server! \nHis address is:{client_socket.getpeername()} \nCurrent number of clients: {self.client_count}")
                client = Client(id)
                self.client_connection(client_socket, client)
        except socket.error as e:
            print(e)


    def client_connection(self, conn, client):  # connecting the client and creating thread for him
        thread_con = threading.Thread(target=self.receive_messages, args=(conn, client,))
        thread_con.daemon = True
        thread_con.start()

    def receive_messages(self, conn, client):
        try:
            # Connect to database
            db = sqlite3.connect('users.db')
            c = db.cursor()
            print("Opened database successfully")
            while self.server_open:
                message = conn.recv(1024).decode()
                if message is None or message == "":
                    raise ConnectionError
                self.handle_messages(conn, message, c, client)
        except ConnectionError:
            if self.client_count > 1:
                try:
                    self.client_list.remove(client.username)
                except:
                    print("this client didn't login yet...")
            else:
                self.client_list = [" "]
            self.client_count -= 1
            print(f"Connection ended, current clients in server: {self.client_count}")
            conn.close()
        print(f"current users: {self.client_list}")

    def check(self, conn, user, password, c, client):
        # check the password that the user typed
        stat = "False"
        password = hashlib.sha256(str.encode(password)).hexdigest()
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (user, password))
        x = c.fetchall()
        if len(x) > 0 and user not in self.client_list:
            client.set_client_info(user, c) # getting the rest of the data about the user
            if self.client_list == [" "]:
                self.client_list = [client.username]
            else:
                self.client_list.append(client.username)
            print(f"current users: {self.client_list}")
            stat = "True"
            self.send_ver_code(conn, c, client)
        elif user in self.client_list:
            stat = "False_logged"
        return stat

    def send_ver_code(self, conn, c, client): # sending the client's logged user's email with verification code in order to login the system

        email_address = 'Clandery2024@outlook.com'
        email_password = 'MorikiHamood123'
        with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(email_address, email_password)

            con_code = random.randint(1000, 10000)
            client.set_code(con_code)

            c.execute("SELECT email FROM users WHERE username = ?", [client.username])
            user_email = str(c.fetchall()[0])
            user_email = user_email.replace("\'", "")
            user_email = user_email.replace("(", "")
            user_email = user_email.replace(")", "")
            user_email = user_email.replace(",", "")

            subject = 'Confirmation Code for Clandery'
            body = f"Hello dear {client.username}, \nRecently you tried logging in into our system \nYour code is: " + str(con_code)

            msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail(email_address, user_email, msg)

            print(f"concode={con_code}")

    def send_reset_code(self, c, client, reset_username): # sending the client's logged user's email with verification code in order to reset the password the system
        global reset_code

        email_address = 'Clandery2024@outlook.com'
        email_password = 'MorikiHamood123'

        with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(email_address, email_password)

            reset_code = random.randint(1000, 10000)

            print("resetuser: "+ reset_username)
            c.execute("SELECT email FROM users WHERE username = ?", [reset_username])
            user_email = str(c.fetchall()[0])
            user_email = user_email.replace("\'", "")
            user_email = user_email.replace("(", "")
            user_email = user_email.replace(")", "")
            user_email = user_email.replace(",", "")

            subject = 'Password Reset Code'
            body = f"Hello dear {reset_username}, \nRecently you requested to restart your password \nYour code is: " + str(reset_code)

            msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail(email_address, user_email, msg)

            print(f"reset_code={reset_code}")

    def check_code(self, conn, code, client):
        status_code = ""
        if code == str(client.code):
            status_code = "True"
        else:
            status_code = "False"
        return status_code

    def handle_messages(self, conn, message, c, client):
        message = message.split("#")

        if message[0] == "login":
            user = message[1]
            password = message[2]
            status = self.check(conn, user, password, c, client)
            conn.send(status.encode())


        elif message[0] == "code":
            code = message[1]
            status_code1 = self.check_code(conn, code, client)
            conn.send(status_code1.encode())


        elif message[0] == "rank":
            conn.send(client.rank.encode())


        elif message[0] == "name":
            conn.send(client.name.encode())


        elif message[0] == "company":
            conn.send(client.company.encode())

        # create a new user

        elif message[0] == "check_exist":
            input_username = message[1]
            input_name = message[2]
            input_email = message[3]
            password = message[4]
            password_hash = hashlib.sha256(str.encode(message[4])).hexdigest()
            confirm_password = message[5]
            company = message[6]
            c.execute("SELECT username FROM users WHERE username = ?", [input_username])
            exist_user = c.fetchall()
            c.execute("SELECT username FROM users WHERE email = ?", [input_email])
            exist_email = c.fetchall()
            regex_mail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if re.fullmatch(regex_mail, input_email):  # checking if email is vaild
                vaild_email = True
            else:
                vaild_email = False
            regex_pass = r'[A-Za-z0-9@#$%^&+=]{8,}'
            print(f"password:{password}\nconfirm:{confirm_password}")
            if re.fullmatch(regex_pass, password):
                vaild_pass = True
            else:
                vaild_pass = False
            if len(password) < 15 and len(confirm_password) < 15 and password == confirm_password:
                passwords = True
            else:
                passwords = False
            if exist_user == [] and exist_email == [] and vaild_email and vaild_pass and len(input_username) <= 12 and passwords:
                conn.send("True#t".encode())
                db = sqlite3.connect('users.db')
                c = db.cursor()
                c.execute(f"""INSERT INTO users (username,password,realname,email,rank,company) VALUES (?, ?, ?, ?, "Member",?)""", (input_username, password_hash, input_name, input_email, company))
                db.commit()
                db.close()

                # Sending welcome email to the new user
                email_address = 'Clandery2024@outlook.com'
                email_password = 'MorikiHamood123'

                with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.ehlo()
                    smtp.login(email_address, email_password)
                    subject = 'Welcome to Clandery'
                    body = f"Hello dear {input_name}, \nWelcome to our system - Clandery\nusername: {input_username}\npassword: {password}\n Thanks for registering!"
                    msg = f'Subject: {subject}\n\n{body}'
                    smtp.sendmail(email_address, input_email, msg)
            else:
                if exist_user != [] and exist_email != []:
                    conn.send("False#username#email".encode())
                elif exist_user != [] and exist_email == []:
                    conn.send("False#username#e".encode())
                elif exist_user == [] and exist_email != []:
                    conn.send("False#email#u".encode())
                elif password != confirm_password:
                    conn.send("False#password#u".encode())
                elif len(password) >= 15 or len(confirm_password) >= 15 or len(password) >= 15 and len(confirm_password) >= 15:
                    conn.send("False#passwordlen#u".encode())
                elif not vaild_email:
                    conn.send("False#email_false".encode())
                elif not vaild_pass:
                    conn.send("False#pass".encode())

        # remove exist user

        elif message[0] == "deleteuser":
            user_company = message[2]
            c.execute("SELECT username FROM users WHERE username = ?", [message[1]])
            exist_user = c.fetchall()
            if exist_user != []:
                c.execute("SELECT company FROM users WHERE username = ?", [message[1]])
                company = str(c.fetchall()[0])
                company = company.replace("\'", "")
                company = company.replace("(", "")
                company = company.replace(")", "")
                company = company.replace(",", "")
                if company == user_company:
                    db = sqlite3.connect('users.db')
                    c = db.cursor()
                    c.execute("""DELETE FROM users WHERE username = ?""", [message[1]])
                    db.commit()
                    db.close()
                    conn.send("True#user#d".encode())
                else:
                    conn.send("No_User#c".encode())
            else:
                conn.send("False#user#d".encode())

        elif message[0] == "promote":
            c.execute("SELECT username FROM users WHERE username = ?", [message[1]])
            exist_user = c.fetchall()
            if exist_user != []:
                db = sqlite3.connect('users.db')
                c = db.cursor()
                c.execute("UPDATE users SET rank = Admin WHERE username = ?", [message[1]])
                db.commit()
                db.close()
                conn.send("promoted#user".encode())
            else:
                conn.send("didnt_promote#user".encode())


        elif message[0] == "get_date":
            conn.send((str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day)).encode())

        elif message[0] == "get_events":
            db_events = sqlite3.connect('users.db')
            c_ev = db_events.cursor()
            if message[2] == "Clandery":
                c_ev.execute("SELECT * FROM events WHERE Date = ?", [message[1]])
            else:
                c_ev.execute("SELECT * FROM events WHERE Date = ? AND Company = ?", (message[1], message[2]))
            events = c_ev.fetchall()
            if events != []:
                conn.send(json.dumps(events).encode())
            else:
                conn.send(json.dumps("no_events").encode())


        elif message[0] == "add_event":
            eventname = message[1]
            date = message[2]
            time = message[3]
            company = message[4]
            hour, minute = message[3].split(":")
            year, month, day = date.split("-")
            db_events = sqlite3.connect('users.db')
            c_ev = db_events.cursor()
            c_ev.execute("SELECT Name FROM events WHERE Name = ? AND Company = ?", (eventname, company))
            exist_name = c_ev.fetchall()
            isValidDate = False
            try:
                if datetime.datetime(int(year), int(month), int(day)) and not exist_name:
                    isValidDate = True
                if isValidDate and int(month) == datetime.datetime.now().month and int(day) > datetime.datetime.now().day and not exist_name:
                    self.Insert_event(conn, eventname, date, time, company)
                elif isValidDate and int(month) == datetime.datetime.now().month and int(day) == datetime.datetime.now().day and int(hour) == datetime.datetime.now().hour and int(minute) > datetime.datetime.now().minute and not exist_name:
                    self.Insert_event(conn, eventname, date, time, company)
                elif isValidDate and int(month) == datetime.datetime.now().month and int(day) == datetime.datetime.now().day and int(hour) > datetime.datetime.now().hour and not exist_name:
                    self.Insert_event(conn, eventname, date, time, company)
                elif isValidDate and int(month) > datetime.datetime.now().month and not exist_name:
                    self.Insert_event(conn, eventname, date, time, company)
                elif isValidDate and int(year) > datetime.datetime.now().year and not exist_name:
                    self.Insert_event(conn, eventname, date, time, company)
                elif exist_name:
                    conn.send("name_exist#fix".encode())
                else:
                    conn.send("invaild_time#fix".encode())
            except:
                conn.send("invaild_date#fix".encode())


        elif message[0] == "delete_event":
            Name = message[1]
            db_events = sqlite3.connect('users.db')
            c_ev = db_events.cursor()
            c_ev.execute("SELECT Name FROM events WHERE Name = ? AND Company = ?", (message[1], message[2]))
            exist_event = c_ev.fetchall()
            c_ev.execute("SELECT Date FROM events WHERE Name = ? AND Company = ?", (message[1], message[2]))
            event_date = c_ev.fetchall()
            if exist_event != []:
                c_ev.execute("""DELETE FROM events WHERE Name = ? AND Company = ?""", (message[1], message[2]))
                db_events.commit()
                db_events.close()
                conn.send(f"event_deleted#{event_date}".encode())
            else:
                conn.send("event_not_exist#fix".encode())

        elif message[0] == "resetpass":
            reset_username = message[1]
            reset_email = message[2]
            db_users = sqlite3.connect('users.db')
            c = db_users.cursor()
            c.execute("SELECT realname FROM users WHERE username = ? AND email = ?", (reset_username, reset_email))
            exist_user = c.fetchall()
            if exist_user != []:
                self.send_reset_code(c, client, reset_username)
                conn.send("True".encode())
                db_users.commit()
                db_users.close()
                print(True)
            else:
                conn.send("False".encode())

        elif message[0] == "passcode":
            if int(message[1]) == reset_code:
                conn.send("True".encode())
            else:
                conn.send("False".encode())

        elif message[0] == "newpass":
            username = message[1]
            password1 = message[2]
            password2 = message[3]
            regex_pass = r'[A-Za-z0-9@#$%^&+=]{8,}'
            print(f"password:{password1}\nconfirm:{password2}")
            if re.fullmatch(regex_pass, password1) and re.fullmatch(regex_pass, password2):
                hash_pass = hashlib.sha256(str.encode(password1)).hexdigest()
                db_users = sqlite3.connect('users.db')
                c = db_users.cursor()
                c.execute(f"UPDATE users SET password = ? WHERE username = ?", (str(hash_pass), username))
                db_users.commit()
                db_users.close()
                conn.send("True".encode())
            else:
                if password1 != password2:
                    conn.send("False#password".encode())
                elif len(password1) >= 15 or len(password2) >= 15 or len(password1) >= 15 and len(password2) >= 15:
                    conn.send("False#passwordlen".encode())

        elif message[0] == "delete_company":
            name = message[1]
            db = sqlite3.connect('users.db')
            c = db.cursor()
            c.execute("SELECT company FROM users WHERE company = ?", [message[1]])
            exist_company = c.fetchall()
            if exist_company != [] and message[1] != "Clandery":
                c.execute("""DELETE FROM users WHERE Company = ?""", [message[1]])
                db.commit()
                db.close()
                conn.send(f"company_deleted#{name}".encode())
            elif message[1] == "Clandery":
                conn.send("company_clandery#fix".encode())
            else:
                conn.send("company_not_exist#fix".encode())

        elif message[0] == "add_company":
            input_username = message[1]
            input_name = message[2]
            input_email = message[3]
            password = message[4]
            password_hash = hashlib.sha256(str.encode(message[4])).hexdigest()
            confirm_password = message[5]
            user_company = message[6]
            c.execute("SELECT username FROM users WHERE username = ?", [input_username])
            exist_user = c.fetchall()
            c.execute("SELECT username FROM users WHERE email = ?", [input_email])
            exist_email = c.fetchall()
            c.execute("SELECT company FROM users WHERE company = ?", [user_company])
            exist_company = c.fetchall()
            print(f"existcomp:{exist_company}")
            regex_mail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if re.fullmatch(regex_mail, input_email):  # checking if email is vaild
                vaild_email = True
            else:
                vaild_email = False
            regex_pass = r'[A-Za-z0-9@#$%^&+=]{8,}'
            print(f"password:{password}\nconfirm:{confirm_password}")
            if re.fullmatch(regex_pass, password):
                vaild_pass = True
            else:
                vaild_pass = False
            if len(password) < 15 and len(confirm_password) < 15 and password == confirm_password:
                passwords = True
            else:
                passwords = False
            if exist_user == [] and exist_email == [] and exist_company == [] and vaild_email and vaild_pass and len(input_username) <= 12 and passwords:
                conn.send("True#t".encode())
                db = sqlite3.connect('users.db')
                c = db.cursor()
                c.execute(f"""INSERT INTO users (username,password,realname,email,rank,company) VALUES (?, ?, ?, ?, "Admin",?)""", (input_username, password_hash, input_name, input_email, user_company))
                db.commit()
                db.close()

                # Sending welcome email to the new user
                email_address = 'Clandery2024@outlook.com'
                email_password = 'MorikiHamood123'

                with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.ehlo()
                    smtp.login(email_address, email_password)
                    subject = 'Welcome to Clandery'
                    body = f"Hello dear {input_name}, \nWelcome to our system - Clandery\nusername: {input_username}\npassword: {password}\n Thanks for registering!"
                    msg = f'Subject: {subject}\n\n{body}'
                    smtp.sendmail(email_address, input_email, msg)
            else:
                if exist_user != [] and exist_email != []:
                    conn.send("False#username#email".encode())
                elif exist_user != [] and exist_email == []:
                    conn.send("False#username#e".encode())
                elif exist_user == [] and exist_email != []:
                    conn.send("False#email#u".encode())
                elif exist_user == [] and exist_email == [] and exist_company != []:
                    conn.send("False#company#u".encode())
                elif exist_user != [] and exist_email != [] and exist_company != []:
                    conn.send("False#username#email#company".encode())
                elif password != confirm_password:
                    conn.send("False#password#u".encode())
                elif len(password) >= 15 or len(confirm_password) >= 15 or len(password) >= 15 and len(confirm_password) >= 15:
                    conn.send("False#passwordlen#u".encode())
                elif not vaild_email:
                    conn.send("False#email_false".encode())
                elif not vaild_pass:
                    conn.send("False#pass".encode())


    def Insert_event(self, conn, eventname, date, time, company):
        db_events = sqlite3.connect('users.db')
        c_ev = db_events.cursor()
        c_ev.execute(f"""INSERT INTO events (Name,Date,Time,Company) VALUES (?, ?, ?, ?)""", (eventname, date, time, company))
        db_events.commit()
        db_events.close()
        conn.send("event_added#now".encode())


if __name__ == '__main__':
    ip = "0.0.0.0"
    port = 25565
    server1 = Server(ip, port)
    server1.start() # starting the server
