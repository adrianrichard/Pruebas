'''Program that asks users what day and time they want
their doctors appointment set'''
import stringsVar as main        #imports functions module
import classesModule as classes #imports classes module
from tkinter import *           #lets us use a GUI
from tkinter import messagebox  #imports the message box
from tkcalendar import *        #imports the tk calendar
from datetime import *          #imports datetime module

#tkinter
root = Tk()
root.title('Doctor\'s Appointment Schedular') #name of title shown
root.eval('tk::PlaceWindow . center') #centers gui screen
root.geometry('600x800') #size of gui screen

#function from Pet button
def show_pet():
    #needed to globalized all variables...would get erros otherwise
    global name_pet
    global human_lname
    global pet_age
    global pet_type
    global name_human
    global human_lname2
    global human_age

    #initialized human variables because we would get errors of undefined
    name_human = ''
    human_lname2 = ''
    human_age = ''

    #asks for pet age
    name_pet = Entry(petentryframe, width=20)
    name_pet.insert(0,'Enter Pet\'s name:')
    name_pet.pack()

    #asks for owners last name
    human_lname = Entry(petentryframe, width=20)
    human_lname.insert(0, 'Enter your last name:')
    human_lname.pack()

    #asks for pets age
    pet_age = Entry(petentryframe, width=20)
    pet_age.insert(0, 'Enter Pet\'s age:')
    pet_age.pack()

    #asks for what type of pet
    pet_type = Entry(petentryframe, width=20)
    pet_type.insert(0,'Enter Pet\'s type:')
    pet_type.pack()



def show_human():
    #needed to globalized all variables...would get erros otherwise...feels redundant but it only works like this
    global name_human
    global human_lname2
    global human_age
    global name_pet
    global human_lname
    global pet_age
    global pet_type


    #asks for patients first name
    name_human = Entry(humanentryframe, width=30)
    name_human.insert(0, 'Enter patient\'s first name:')
    name_human.pack()

    #asks for patients last name
    human_lname2 = Entry(humanentryframe, width=30)
    human_lname2.insert(0, 'Enter patient\'s last name:')
    human_lname2.pack()

    #asks for patients age
    human_age = Entry(humanentryframe, width=30)
    human_age.insert(0,'Enter patient\'s age:')
    human_age.pack()


#Welcome Message from functions module
welcomeframe = LabelFrame(root, padx=20, pady=20)   #Frame for input fields
welcomeframe.grid(row=0, column=0)
welcome_label = Label(welcomeframe, text=main.welcome_msg, font=('bold', 14))
welcome_label.grid(row=0, column=0)


#button to choose pet or human input boxes
buttonframe = LabelFrame(root, padx=20, pady=20)   #Frame for input fields
buttonframe.grid(row=1, column=0)
choose_pet = Button(buttonframe, text='Pet', command=show_pet).grid(row=1, column=1)
choose_human = Button(buttonframe, text='Human', command=show_human).grid(row=1, column=0)

#Frame for entry fields
humanentryframe = LabelFrame(root, text="Enter patient's first name, last name, and age", padx=10, pady=10)
humanentryframe.grid(row=2, column=0)

#Pet frame for entry fields
petentryframe = LabelFrame(root, text="Enter pet's name, owner's last name, and pet's age", padx=10, pady=10)
petentryframe.grid(row=3, column=0)

#Calendar frame for entry fields
calendarframe = LabelFrame(root, text="Select a date and time", padx=100, pady=10)
calendarframe.grid(row=4, column=0)

#This shows the calendar in TKINTER
cal = Calendar(calendarframe, selectmode="day")
cal.pack()  #pads calendar


#function of grabbing the date
def grab_date():
    #function inside a function that works with the class module
    def show_booking():
        #from show_pet function to see if user chose pet or human
        if (name_human == '' and human_lname2 == '' and human_age == ''):
            #saving to pets classes using get()
            typePet = pet_type.get()
            petAge = pet_age.get()
            lastName = human_lname.get()
            petName = name_pet.get()
            #Creates new Object for Pets
            newPet = classes.Pets(petName, lastName, petAge, typePet)

            #opens file then writes and appends appointments for vet
            f = open('PetAppointment.txt', 'a+')
            f.write('Name: ' + newPet.full_name()+ '\nPet type: ' + newPet.pet_type + '\nPet age: ' + newPet.age + '\nAppointment date: ' + check_date + '\nTime: ' + hours.get() + '\n\n\n')
            f.close()
            root.update()


        else:
            #saves to human classes using get()
            humanName = name_human.get()
            lastName2 = human_lname2.get()
            humanAge = human_age.get()
            newHuman = classes.Human(humanName, lastName2, humanAge) #Creates object for Humans

            #opens file then writes and appends appointments for doctor or nurse
            f = open('HumanAppointment.txt', 'a+')
            f.write('Name: ' + newHuman.full_name()+ '\nAge: ' + newHuman.age + '\nAppointment date: ' + check_date + '\nTime: ' + hours.get() + '\n\n\n')
            f.close()
        #label that visually shows you booked an appointment
        times_label = Label(calendarframe, text='Thank you! Your appointment has been booked for '+ check_date + ' at ' + hours.get()).pack()

    #grabs the date you selected in calendar
    check_date = cal.get_date()
    #this converts check date to datetime format
    convert_datetime = datetime.strptime(check_date, '%m/%d/%y')

    #while loop to make sure time and date is available
    while True:
    #  If statement that pops up if you choose a weekend
        if ((convert_datetime.weekday() == 5) or (convert_datetime.weekday() == 6)): #Checks if weekend
            #gives an error message and wont let you continue until correct date is chosen
            messagebox.showwarning(title='Error', message='Please select a day between Monday and Friday')
            break
        else:
            my_label.config(text=main.show_times_msg)
            #this creates a drop down menu
            hours = StringVar()
            hours.set(main.times_tup[0]) #sets as the default value
            drop = OptionMenu(calendarframe, hours, *main.times_tup).pack()#menu
            book_button = Button(calendarframe, text='Book Appt', command=show_booking).pack()
            break

#button that select date you want to book
my_button = Button(calendarframe, text='Get Date', command=grab_date)
my_button.pack()
my_label = Label(calendarframe, text='')
my_label.pack()

root.mainloop()
