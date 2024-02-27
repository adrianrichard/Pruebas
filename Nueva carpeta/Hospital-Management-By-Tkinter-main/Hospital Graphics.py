#Importing modules
import csv
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import date
import datetime
import tkinter.messagebox
import os
name,age,weight,gender,aadhar,phone,address,doctor=0,0,0,0,0,0,0,0 #Appointment Window
name,age,weight,gender,aadhar,address,phone,refered,problem,ward=0,0,0,0,0,0,0,0,0,0 #Patient Admit Window
IDdis,f=0,0 #Discharging Window
idstaff,SID,Sname,Age,Gender,Aadhar,Phone,Desig,Address=0,0,0,0,0,0,0,0,0 #Modify Staff Window
IDpatient,name,age,weight,gender,aadhar,address,phone,refered,problem,ward=0,0,0,0,0,0,0,0,0,0,0 #Modify Patient Admitted Window
IDdpatient,name,age,weight,gender,aadhar,address,phone,refered,problem,ward=0,0,0,0,0,0,0,0,0,0,0 #Modify Patient Discharged Window
StaffName,Age,Gender,Aadhar,Phone,Desig,Address=0,0,0,0,0,0,0 #Hiring Staff Window
n=100
def First_Window():
    m1=Tk()#create a window
    m1.title("KJ Group Of Hospital")
    m1.config(bg="BLACK")#to give backgrond colour
    left_frame=Frame(m1,width=1450,height=700,bg='#7FFFD4')
    left_frame.grid(row=0,column=0,padx=50,pady=50)
    head= Label(m1, text="KJ Group Of Hospitals", font=('Verdana 70 bold '), fg='black',bg='white')
    head.place(x=220, y=0)
    head= Label(m1, text="Taramandal GKP 221715 Phone:- 9648084972", font=('Verdana 15 bold '), fg='black',bg='white')
    head.place(x=540, y=110)
    l1=Button(m1 ,bg='WHITE',text="1.Appointment",font='Verdana 20 ',command=Appointment_Window)
    l1.place(x=400,y=180)
    l1=Button(m1 ,bg='WHITE',text="2.Admitting The Patient",font='Verdana 20',command=Patient_Admit_Window)
    l1.place(x=400,y=380)
    l1=Button(m1 ,bg='WHITE',text="3.Details ",font='Verdana 20',command=Details_Window)
    l1.place(x=400,y=580)
    l1=Button(m1 ,bg='WHITE',text="4.Discharging The Patient ",font='Verdana 20',command=Patient_Discharge_Window)
    l1.place(x=800,y=180)
    l1=Button(m1 ,bg='WHITE',text="5.Modifying The Details ",font='Verdana 20',command=Modify_Window)
    l1.place(x=800,y=380)
    l1=Button(m1 ,bg='WHITE',text="6.Hiring The Staff ",font='Verdana 20',command=Hire_Staff_Window)
    l1.place(x=800,y=580)
    head= Label(m1, text=" | Difficult roads often leads to beautiful destinations | ", font=('Verdana 28 bold '), fg='black',bg='white')
    head.place(x=200, y=700)
    m1.geometry("1200x1200")
    m1.mainloop()
#For appointment of the patients
def Appointment_Window():
    global name,age,weight,gender,aadhar,phone,address,doctor
    m2=Toplevel()#create a window
    m2.geometry("600x600")
    m2.title("Appointment-KJ Group Of Hospital")
    m2.config(bg="#FFBBFF")#to give backgrond colour
    head= Label(m2, text="KJ Group Of Hospitals", font=('Verdana 60 bold '), fg='black',bg='white')
    head.place(x=300, y=0)
    head= Label(m2, text="Appointment", font=('Verdana 30 bold '), fg='white',bg='black')
    head.place(x=610, y=105)
    l2=Label(m2 ,fg='black',text="Patient Name",font='Verdana 28 ',bg='#FFBBFF')
    l2.place(x=180,y=210)
    l2=Label(m2 ,fg='black',text="Age",font='Verdana 28',bg='#FFBBFF')
    l2.place(x=180,y=280)
    l2=Label(m2 ,fg='black',text="Wieght",font='Verdana 28',bg='#FFBBFF')
    l2.place(x=180,y=350)
    l2=Label(m2 ,fg='black',text="Gender",font='Verdana 28',bg='#FFBBFF')
    l2.place(x=180,y=420)
    l2=Label(m2 ,fg='black',text="Aadhar",font='Verdana 28',bg='#FFBBFF')
    l2.place(x=710,y=210)
    l2=Label(m2 ,fg='black',text="Phone No.",font='Verdana 28',bg='#FFBBFF')
    l2.place(x=710,y=280)
    l2=Label(m2 ,fg='black',text="Address",font='Verdana 28',bg='#FFBBFF')
    l2.place(x=710,y=350)
    l2=Label(m2 ,fg='black',text="Doctor",font='Verdana 28',bg='#FFBBFF')
    l2.place(x=710,y=410)
    l2=Label(m2,fg='black',text=" We are really thankful to you that you choosed us. ",font='Calibri 25',bg='White')
    l2.place(x=200,y=520)
    head= Label(m2, text="| The Habit of persistence is the habit of victory | ", font=('Verdana 30 bold '), fg='black',bg='white')
    head.place(x=200, y=700)
    #Getting entries (Patient Name,Age,Weight,Aender,Aadhar No.,Phone No.,Doctor Name)from users
    name=Entry(m2,width=20,font='Verdana 12')
    name.place(x=470,y=228)
    age=Entry(m2,width=20,font='Verdana 12')
    age.place(x=470,y=298)
    weight=Entry(m2,width=20,font='Verdana 12')
    weight.place(x=470,y=368)
    gender= ttk.Combobox(m2,
                            values=[
                                    "Male",
                                    "Female"],width=20,font='Verdana 12')
    gender.place(x=470,y=438)
    aadhar=Entry(m2,width=20,font='Verdana 12')
    aadhar.place(x=950,y=228)
    phone=Entry(m2,width=20,font='Verdana 12')
    phone.place(x=950,y=298)
    address=Entry(m2,width=20,font='Verdana 12')
    address.place(x=950,y=368)
    doctor = ttk.Combobox(m2,
                            values=[
                                    "Amrit Lal-Physician",
                                    "Rekha jaiswal-Gynoclogist",
                                    "Farrukh-sheikh-Orthopaedic",
                                    "Ravi verma-Surgeon",
                                    "Raghav Kataria-Immunologist",
                                    "Sahnice Shreshtha-Cardiologist",
                                    "Nikhil Verma-Neurologist",
                                    "Zahir Khan-Gastroenologist"],width=20,font='Verdana 12')
    doctor.place(x=950,y=438)
    b1=Button(m2,text="Add Appointment",font='Calibri 20',command=add_appointment,bg='yellow')
    b1.place(x=930,y=520)

#Adding Data of Customer in File
def add_appointment():
        rec=[]
        global name,age,weight,gender,aadhar,phone,address,doctor
        # getting the user inputs
        m=open("Patient Appoi.csv",'r')
        c=csv.reader(m)
        f=100
        for i in c:
            if len(i) != 0:
                u=i[0]
                f=int(u)+ 1
        val0 = f
        val1 = name.get()
        val2 = age.get()
        val3 = weight.get()
        val4 = gender.get()
        val5 = aadhar.get()
        val6 = phone.get()
        val7 = address.get()
        val8 = doctor.get()
        val9 = datetime.datetime.now()
        today=date.today()
        d1 = today.strftime("%d/%m/%Y")
        val10 = d1
        rec.append(val0)
        rec.append(val1)
        rec.append(val2)
        rec.append(val3)
        rec.append(val4)
        rec.append(str(val5)) #Converting Into String So That The Full Lenght Would Be Shown In Output Table
        rec.append(str(val6))
        rec.append(val7)
        rec.append(val8)
        rec.append(str(val9))
        rec.append(str(val10))

        # checking if the user input is empty
        if val1 == '' or val2 == '' or val3 == '' or val4 == '' or val5 == '' or val6 == '' or val7 == '' or val8 == '' :
            messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        if val2.isdigit()!= True or val3.isdigit()!= True or len(val5)!= 12 or val5.isdigit()!= True or val6.isdigit()!= True or len(val6)!= 10 :
            messagebox.showinfo("Warning", "Please Fill UP Correct Details")
        else:
            # now we add to the database
            f=open("Patient Appoi.csv","a+",newline='')
            we=csv.writer(f)
            we.writerow(rec)
            rec=[]
            f.close()
            messagebox.showinfo("Success", "Appointment for " + val1 + " has been created" )
#Admitting the Patient In the Hospital
def Patient_Admit_Window():
    global name,age,weight,gender,aadhar,address,phone,refered,problem,ward
    m3=Toplevel()#create a window
    m3.title("Admitting-KJ Group Of Hospital")
    m3.config(bg="pink")#to give backgrond colour
    head= Label(m3, text="KJ Group Of Hospitals", font=('Verdana 65 bold '), bg='white',fg='black')
    head.place(x=250, y=0)
    head= Label(m3, text="Admitting the Patient", font=('Verdana 30 bold '), bg='black',fg='white')
    head.place(x=530, y=110)
    l3=Label(m3,fg='black',text="Patient Name",font='Verdana 28 ',bg='pink')
    l3.place(x=280,y=210)
    l3=Label(m3,fg='black',text="Age",font='Verdana 28',bg='pink')
    l3.place(x=280,y=270)
    l3=Label(m3,fg='black',text="Weight",font='Verdana 28',bg='pink')
    l3.place(x=280,y=330)
    l3=Label(m3,fg='black',text="Gender",font='Verdana 28',bg='pink')
    l3.place(x=280,y=390)
    l3=Label(m3,fg='black',text="Aadhar",font='Verdana 28',bg='pink')
    l3.place(x=280,y=450)
    l3=Label(m3,fg='black',text="Address",font='Verdana 28',bg='pink')
    l3.place(x=880,y=210)
    l3=Label(m3,fg='black',text="Phone No.",font='Verdana 28',bg='pink')
    l3.place(x=880,y=270)
    l3=Label(m3,fg='black',text="Refered By",font='Verdana 28',bg='pink')
    l3.place(x=880,y=330)
    l3=Label(m3,fg='black',text="Problem",font='Verdana 28',bg='pink')
    l3.place(x=880,y=390)
    l3=Label(m3,fg='black',text="Ward",font='Verdana 28',bg='pink')
    l3.place(x=880,y=450)
    name=Entry(m3,width=20,font='Verdana 12')
    name.place(x=580,y=228)
    age=Entry(m3,width=20,font='Verdana 12')
    age.place(x=580,y=288)
    weight=Entry(m3,width=20,font='Verdana 12')
    weight.place(x=580,y=348)
    gender= ttk.Combobox(m3,
                            values=[
                                    "Male",
                                    "Female"],width=20,font='Verdana 12')
    gender.place(x=580,y=408)
    aadhar=Entry(m3,width=20,font='Verdana 12')
    aadhar.place(x=580,y=468)
    address=Entry(m3,width=20,font='Verdana 12')
    address.place(x=1130,y=228)
    phone=Entry(m3,width=20,font='Verdana 12')
    phone.place(x=1130,y=288)
    refered=ttk.Combobox(m3,
                            values=[
                                    "Amrit Lal-Physician",
                                    "Rekha jaiswal-Gynoclogist",
                                    "Farrukh-sheikh-Orthopaedic",
                                    "Ravi verma-Surgeon",
                                    "Raghav Kataria-Immunologist",
                                    "Sahnice Shreshtha-Cardiologist",
                                    "Nikhil Verma-Neurologist",
                                    "Zahir Khan-Gastroenologist"],width=20,font='Verdana 12')
    refered.place(x=1130,y=348)
    problem=Entry(m3,width=20,font='Verdana 12')
    problem.place(x=1130,y=408)
    ward= ttk.Combobox(m3,
                            values=[
                                    "ICU",
                                    "G W"],width=20,font='Verdana 12')
    ward.place(x=1130,y=468)
    l1=Label(m3,fg='black',text=" We are here to take care of you.",font='Calibri 25',bg='orange')
    l1.place(x=280,y=528)
    b1=Button(m3,text="Admit",font='Verdana 15',command=admit)
    b1.place(x=800,y=530)
    head= Label(m3, text=" | The happiness of your life depends on the quality of your thoughts | ", font=('Verdana 25 bold '), fg='white',bg='black')
    head.place(x=100, y=700)
    m3.geometry("600x600")
#Adding Coustomer Data In File
def admit():
        rec=[]
        global name,age,weight,gender,aadhar,address,phone,refered,problem,ward
        # getting the user inputs
        m=open("PatientAD.csv",'r')
        cs=csv.reader(m)
        f=100
        for i in cs:
            if len(i) != 0:
                u=i[0]
                f=int(u)+ 1
        val0 = f
        val1 = name.get()
        val2 = age.get()
        val3 = weight.get()
        val4 = gender.get()
        val5 = aadhar.get()
        val6 = address.get()
        val7 = phone.get()
        val8 = refered.get()
        val9 = problem.get()
        val10 = ward.get()
        val11='Admitted'
        val12 = datetime.datetime.now()
        today=date.today()
        d1 = today.strftime("%d/%m/%Y")
        val13 = d1
        rec.append(val0)
        rec.append(val1)
        rec.append(val2)
        rec.append(val3)
        rec.append(val4)
        rec.append(str(val5))     #Converting Into String So That The Full Lenght Would Be Shown In Output Table
        rec.append(val6)
        rec.append(str(val7))
        rec.append(val8)
        rec.append(val9)
        rec.append(val10)
        rec.append(val11)
        rec.append(str(val12))
        rec.append(str(val13))

        # checking if the user input is empty
        if val1 == '' or val2 == '' or val3 == '' or val10 == '' or val5 == '' or val6 == '' or val7 == '' or val9 == '' :
            messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        if val2.isdigit()!= True or val3.isdigit()!= True or len(val5)!= 12 or val5.isdigit()!= True or val7.isdigit()!= True or len(val7)!= 10 :
            messagebox.showinfo("Warning", "Please Fill Up Correct Details")
        else:
            # now we add to the database
            k=open("PatientAD.csv","a+",newline='')
            we=csv.writer(k)
            we.writerow(rec)
            rec=[]
            k.close()
            messagebox.showinfo("Success", "The patient " + val1 + " has been admitted" )
        m.close()

#To Show the Details of the Stafff and patient
def Details_Window():
    global name,age,gender,address,doctor,ward
    m5=Toplevel()#create a window
    m5.title("Details-KJ Group Of Hospital")
    m5.config(bg="#BDFCC9")#to give backgrond colour
    head= Label(m5, text="KJ Group Of Hospitals", font=('Verdana 65 bold '), fg='black',bg='#CD2990')
    head.place(x=260, y=0)
    head= Label(m5, text="Details", font=('Verdana 40 bold '), fg='black',bg='#CAE1FF')
    head.place(x=670, y=115)
    l5=Button(m5,fg='black',text="Details of Staff",font='Verdana 25 ',bg='#FAFAFA',command=details_staff)
    l5.place(x=200,y=220)
    l5=Button(m5,fg='black',text="Details of Patient Admitted",font='Verdana 25',bg='#FAFAFA',command=details_patient_admitted)
    l5.place(x=200,y=320)
    l5=Button(m5,fg='black',text="Details of Patient Discharged",font='Verdana 25',bg='#FAFAFA',command=details_patient_discharged)
    l5.place(x=200,y=420)
    l5=Button(m5,fg='black',text="Appointment Details",font='Verdana 25',bg='#FAFAFA',command=details_appointment)
    l5.place(x=200,y=520)
    head= Label(m5, text=" | If everything was perfect , you would never learn and you would never grow | ", font=('Verdana 22 bold '), fg='white',bg='black')
    head.place(x=100, y=700)
    m5.geometry("1200x720+0+0")
def details_staff(): #Staff Detail
    rec='staff ID\tStaff Name\t\tAge\tGender\tAadhar No.\t\tPhone No.\t\tDesignation\t\t\tAddress\t\t\tDOJ\n'
    f=open("staff.csv",'r')
    re=csv.reader(f)
    mm=Toplevel()
    for i in re:
        rec=rec+i[0]+"\t"+i[1]+"\t""\t"+i[2]+"\t"+i[3]+"\t"+i[4]+"\t""\t"+i[5]+"\t""\t"+i[6]+"\t""\t""\t"+i[7]+"\t""\t""\t"+i[8]+"\n"
    la=Text(mm,font=70)
    la.insert(INSERT,rec)
    la.config(state=DISABLED)
    la.pack(side=TOP,fill=BOTH)
    f.close()
def details_patient_admitted(): #Patient Details
    rec='ID\tName\t\tAge\tWeight\tGender\tAadhar No.\t\tAddress\t\tPhone No.\t\tRefered By\t\t\tDate Admited\n'
    f=open("PatientAD.csv",'r')
    re=csv.reader(f)
    mm=Toplevel()
    for i in re:
        rec=rec+i[0]+"\t"+i[1]+"\t""\t"+i[2]+"\t"+i[3]+"\t"+i[4]+"\t"+i[5]+"\t""\t"+i[6]+"\t""\t"+i[7]+"\t""\t"+i[8]+"\t""\t""\t"+i[13]+"\n"
    la=Text(mm,font=70)
    la.insert(INSERT,rec)
    la.config(state=DISABLED)
    la.pack(side=TOP,fill=BOTH)
    f.close()
def details_patient_discharged(): #Patient Discharged
    rec='ID\tName\tAge\tWeight\tGender\tAadhar No.\t\tAddress\t\tPhone No.\t\tRefered By-\t\t\t\tDate Dischrged\n'
    f=open("PatientDis.csv",'r')
    re=csv.reader(f)
    mm=Toplevel()
    for i in re:
        rec=rec+i[0]+"\t"+i[1]+"\t"+i[2]+"\t"+i[3]+"\t"+i[4]+"\t"+i[5]+"\t""\t"+i[6]+"\t""\t"+i[7]+"\t""\t"+i[8]+"\t""\t""\t""\t"+i[15]+"\n"
    la=Text(mm,font=70)
    la.insert(INSERT,rec)
    la.config(state=DISABLED)
    la.pack(side=TOP,fill=BOTH)
    f.close()
def details_appointment(): #Appointment Details
    rec='ID\tName\t\tAge\tWeight\tGender\tAadhar No.\t\tPhone No.\t\tAddress\t\tRefered To\t\t\t\tDate \n'
    f=open("Patient Appoi.csv",'r')
    re=csv.reader(f)
    mm=Toplevel()
    for i in re:
        rec=rec+i[0]+"\t"+i[1]+"\t""\t"+i[2]+"\t"+i[3]+"\t"+i[4]+"\t"+i[5]+"\t""\t"+i[6]+"\t""\t"+i[7]+"\t""\t"+i[8]+"\t""\t""\t""\t"+i[10]+"\n"
    la=Text(mm,font=70)
    la.insert(INSERT,rec)
    la.config(state=DISABLED)
    la.pack(side=TOP,fill=BOTH)
    f.close()
    #To discharge the patient and create the bill of the patient
def Patient_Discharge_Window():
    global IDdis
    m4=Toplevel() #create a window
    m4.title("Discharging-KJ Group Of Hospital")
    m4.config(bg="#FFA07A") #to give backgrond colour
    head= Label(m4, text="KJ Group Of Hospitals", font=('Verdana 70 bold '), fg='white',bg='black')
    head.place(x=210, y=0)
    head= Label(m4, text="Discharging the Patient", font=('Verdana 30 bold '), fg='black',bg='#48D1CC')
    head.place(x=500, y=120)
    l3=Label(m4,fg='black',text="Patient ID",font='Verdana 25 ',bg='#FFFACD')
    l3.place(x=200,y=240)
    IDdis=Entry(m4,width=20,font='Verdana 12')
    IDdis.place(x=450,y=253)
    l1=Label(m4,fg='black',text=" Bye Bye Take Care ",font='Calibri 25',bg='#E6E6FA')
    l1.place(x=300,y=300)
    b1=Button(m4,text="Discharge",font='Verdana 15',command=Discharge,bg='#E0FFFF')
    b1.place(x=600,y=300)
    head= Label(m4, text=" | Life isn't about waiting for the storm to pass. ", font=('Verdana 25 bold '), fg='BLACK',bg='#E6E6FA')
    head.place(x=300, y=500)
    head= Label(m4, text="   It's about learning how to dance in  the rain | ", font=('Verdana 25 bold '), fg='BLACK',bg='#E6E6FA')
    head.place(x=300, y=550)
    head= Label(m4, text=" HAVE A HEALTHY LIFE AHEAD ", font=('Verdana 25 bold '), fg='BLACK',bg='#48D1CC')
    head.place(x=800, y=650)
    m4.geometry("600x600")
    #Adding Details To Discharge File

def Discharge():
    global IDdis,f
    # Getting the User Inputs
    val = IDdis.get()
    k=open("PatientAD.csv",'r')
    ff=open("temp.csv",'a+',newline='')
    m=open("PatientDis.csv",'a+',newline='')
    n=open("PatientDis.csv",'r')
    cr=csv.reader(k)
    cw=csv.writer(ff)
    kw=csv.writer(m)
    kr=csv.reader(n)
    f=100
    for s in kr:
        if len(s) != 0:
            u=s[0]
            f=int(u)+ 1
    for i in cr:
        rec=[]
        print(f)
        val0 = f
        val1 = i[1]
        val2 = i[2]
        val3 = i[3]
        val4 = i[4]
        val5 = i[5]
        val6 = i[6]
        val7 = i[7]
        val8 = i[8]
        val9 = i[9]
        val10 = i[10]
        val11 = 'Discharged'
        val12 = i[12]
        val13 = i[13]
        val14=datetime.datetime.now()
        today=date.today()
        d1 = today.strftime("%d/%m/%Y")
        val15 = d1
        rec.append(val0)
        rec.append(val1)
        rec.append(val2)
        rec.append(val3)
        rec.append(val4)
        rec.append(val5)
        rec.append(val6)
        rec.append(val7)
        rec.append(val8)
        rec.append(val9)
        rec.append(val10)
        rec.append(val11)
        rec.append(val12)
        rec.append(val13)
        rec.append(str(val14))
        rec.append(str(val15))
        if i[0]!=val:
            cw.writerow(i)
        else:
            kw.writerow(rec)
            messagebox.showinfo("Success", "Congratulations You Can Go Home" )
            rec=[]

    k.close()
    ff.close()
    m.close()
    n.close()
    os.remove("PatientAD.csv")
    os.rename("temp.csv","PatientAD.csv")
    discharge_certificate_window()

#To Give Patient a Discharge Certificate
def discharge_certificate_window():
    global IDdis,f
    val=IDdis.get()
    g=f
    f=open("PatientDis.csv",'r')
    cr=csv.reader(f)
    today=date.today()
    d1 = today.strftime("%d/%m/%Y")
    for i in cr:
        val0=d1
        val00=i[0]
        val1=i[1]
        val2=i[2]
        val3=i[3]
        val4=i[4]
        val5=i[5]
        val6=i[7]
        val7=i[8]
        val8=i[9]
        val9=i[13]
        val10=i[15]


    d1=Tk()#Creating a Window
    d1.title("Modify Staff-KJ Group Of Hospital")
    d1.config(bg="#EEE5DE")#To Give Backgrond Colour
    head= Label(d1, text="KJ Group Of Hospitals", font=('Calibri 65 bold '), bg='white',fg='black')
    head.place(x=385, y=0)
    head= Label(d1, text="Discharge Certificate", font=('Calibri 30 bold '), fg='black',bg='white')
    head.place(x=580, y=120)
    l1=Label(d1,fg='black',text="Date of Issue = "+str(val0),font='Calibri 20 ',bg='#EEE5DE')
    l1.place(x=200,y=200)
    l1=Label(d1,fg='black',text="Patient ID = "+val00,font='Calibri 20 ',bg='#EEE5DE')
    l1.place(x=700,y=200)
    l1=Label(d1,fg='black',text="Name Of Patients = "+val1,font='Calibri 20 ',bg='#EEE5DE')
    l1.place(x=200,y=250)
    l1=Label(d1,fg='black',text="Age = "+val2,font='Calibri 20',bg='#EEE5DE')
    l1.place(x=200,y=300)
    l1=Label(d1,fg='black',text="Weight = "+val3,font='Calibri 20',bg='#EEE5DE')
    l1.place(x=200,y=350)
    l1=Label(d1,fg='black',text="Gender = "+val4,font='Calibri 20',bg='#EEE5DE')
    l1.place(x=200,y=400)
    l1=Label(d1,fg='black',text="Aadhar No. = "+val5,font='Calibri 20',bg='#EEE5DE')
    l1.place(x=200,y=450)
    l1=Label(d1,fg='black',text="Phone No. =  "+val6,font='Calibri 20 ',bg='#EEE5DE')
    l1.place(x=700,y=250)
    l1=Label(d1,fg='black',text="Problem = "+val8,font='Calibri 20',bg='#EEE5DE')
    l1.place(x=700,y=300)
    l1=Label(d1,fg='black',text="Treated By "+val7,font='Calibri 20',bg='#EEE5DE')
    l1.place(x=700,y=350)
    l1=Label(d1,fg='black',text="Admitted:- "+val9,font='Calibri 20',bg='#EEE5DE')
    l1.place(x=700,y=400)
    l1=Label(d1,fg='black',text="Discharged:- "+val10,font='Calibri 20',bg='#EEE5DE')
    l1.place(x=700,y=450)
    l1=Label(d1,fg='black',text="Complication :- No Complications ",font='Calibri 20',bg='#EEE5DE')
    l1.place(x=200,y=500)
    l1=Label(d1,fg='black',text="Instruction :- To Have More Rest ",font='Calibri 20',bg='#EEE5DE')
    l1.place(x=200,y=550)
    l1=Label(d1,fg='black',text="This is to certify that "+val1+" is being treated from KJ Group Of Hospitals.",font='Calibri 20',bg='#EEE5DE')
    l1.place(x=200,y=600)
    head= Label(d1, text=" | The purpose of our lives is to be happy | ", font=('Verdana 25 bold '), fg='BLACK',bg='white')
    head.place(x=380, y=700)
    d1.geometry("600x600")
#To Modify the Details of the Stafff and Patient
def Modify_Window():
    m6=Toplevel()#Tk()#create a window
    m6.title("Modify-KJ Group Of Hospital")
    m6.config(bg="#FFF68F")#To Give Backgrond Colour
    head= Label(m6, text="KJ Group Of Hospitals", font=('Verdana 60 bold '), fg='white',bg='black')
    head.place(x=300, y=0)
    head= Label(m6, text="Modify the Reords" ,font=('Verdana 30 bold '), fg='black',bg='orange')
    head.place(x=580, y=110)
    l6=Button(m6,fg='white',text="1.Records of Staff",font='Verdana 25 ',bg='brown',command=modify_staff)
    l6.place(x=200,y=190)
    l6=Button(m6,fg='white',text="2.Records of Patient Admitted",font='Verdana 25',bg='brown',command=modify_patientadmitted)
    l6.place(x=200,y=270)
    l6=Button(m6,fg='white',text="2.Records of Patient Discharged",font='Verdana 25',bg='brown',command=modify_patientdischarged)
    l6.place(x=200,y=350)
    head= Label(m6, text=" | The past is a place of reference, not a place of recidence | ", font=('Verdana 25 bold '), fg='black',bg='white')
    head.place(x=200, y=600)
    m6.geometry("600x600")

def modify_staff():
    global idstaff
    m7=Toplevel()#Tk()#create a window
    m7.title("Modify Staff-KJ Group Of Hospital")
    m7.config(bg="#FFD700")#To Give Backgrond Colour
    head= Label(m7, text="KJ Group Of Hospitals", font=('Verdana 60 bold '), fg='white',bg='black')
    head.place(x=300, y=0)
    head= Label(m7, text="Modify the Reords of Staff" ,font=('Verdana 30 bold '), fg='black',bg='blue')
    head.place(x=500, y=110)
    l7=Label(m7,fg='black',text=" Enter ID of Staff ",font='Verdana 28 ',bg='lightgreen')
    l7.place(x=200,y=200)
    l7=Button(m7,bg='red',text="Search",font='Verdana 20 ',command=edit_staff)
    l7.place(x=560,y=250)
    idstaff=Entry(m7,width=20,font='Verdana 12')
    idstaff.place(x=550,y=220)
    head= Label(m7, text=" | Never let the fear of striking out keep you from playing the game | ", font=('Verdana 25 bold '), fg='white',bg='black')
    head.place(x=130, y=600)
    m7.geometry("600x600")

def edit_staff():
    global SID,Sname,Age,Gender,Aadhar,Phone,Desig,Address,idstaff
    m8=Toplevel()#Tk()#Create a Window
    m8.title("Modify Staff-KJ Group Of Hospital")
    m8.config(bg="#CD5555")#to Give Backgrond Colour
    head= Label(m8, text="KJ Group Of Hospitals", font=('Verdana 65 bold '), fg='white',bg='black')
    head.place(x=315, y=0)
    head= Label(m8, text="Modify The Staff Records", font=('Verdana 30 bold '), fg='black',bg='orange')
    head.place(x=550, y=110)
    l8=Label(m8,fg='black',text="Staff ID",font='Verdana 28 ',bg='#CD5555')
    l8.place(x=200,y=180)
    l8=Label(m8,fg='black',text="Staff Name",font='Verdana 28',bg='#CD5555')
    l8.place(x=200,y=240)
    l8=Label(m8,fg='black',text="Age",font='Verdana 28',bg='#CD5555')
    l8.place(x=200,y=300)
    l8=Label(m8,fg='black',text="Gender",font='Verdana 28',bg='#CD5555')
    l8.place(x=200,y=360)
    l8=Label(m8,fg='black',text="Aadhar No.",font='Verdana 28',bg='#CD5555')
    l8.place(x=200,y=420)
    l8=Label(m8,fg='black',text="Phone No.",font='Verdana 28',bg='#CD5555')
    l8.place(x=200,y=480)
    l8=Label(m8,fg='black',text="Designation",font='Verdana 28',bg='#CD5555')
    l8.place(x=200,y=540)
    l8=Label(m8,fg='black',text="Address",font='Verdana 28',bg='#CD5555')
    l8.place(x=200,y=600)
    SID=Entry(m8,width=20,font='Verdana 12')
    SID.place(x=460,y=200)
    Sname=Entry(m8,width=20,font='Verdana 12')
    Sname.place(x=460,y=260)
    Age=Entry(m8,width=20,font='Verdana 12')
    Age.place(x=460,y=320)
    Gender= ttk.Combobox(m8,
                            values=[
                                    "Male",
                                    "Female"])
    Gender.place(x=460,y=380)
    Aadhar=Entry(m8,width=20,font='Verdana 12')
    Aadhar.place(x=460,y=440)
    Phone=Entry(m8,width=20,font='Verdana 12')
    Phone.place(x=460,y=500)
    Desig=Entry(m8,width=20,font='Verdana 12')
    Desig.place(x=460,y=560)
    Address=Entry(m8,width=20,font='Verdana 12')
    Address.place(x=460,y=620)
    b1=Button(m8,text="Done",font='Verdana 15',command=Edited_Staff) #Programme Not Running from here
    b1.place(x=440,y=660)
    head= Label(m8, text=" | You only live once, but if you do it right, once is enough | ", font=('Verdana 25 bold '), fg='black',bg='white')
    head.place(x=220, y=730)
    m8.geometry("600x600")
def Edited_Staff():
    global SID,Sname,Age,Gender,Aadhar,Phone,Desig,Address,idstaff
    # getting the user inputs
    ids=idstaff.get()
    k=open("Staff.csv",'r')
    ff=open("temp.csv",'a+',newline='')
    cr=csv.reader(k)
    cw=csv.writer(ff)
    rec=[]
    for i in cr:
        val1 = SID.get()
        val2 = Sname.get()
        val3 = Age.get()
        val4 = Gender.get()
        val5 = Aadhar.get()
        val6 = Phone.get()
        val7 = Address.get()
        val8 = Desig.get()
        val9 = i[8]
        rec.append(val1)
        rec.append(val2)
        rec.append(val3)
        rec.append(val4)
        rec.append(str(val5))
        rec.append(str(val6))
        rec.append(val8)
        rec.append(val7)
        rec.append(val9)
        if i[0]!=ids:
            cw.writerow(i)
        else:
            cw.writerow(rec)
            rec.clear()
            messagebox.showinfo("Success", "The record has been edited" )


    k.close()
    ff.close()
    os.remove("Staff.csv")
    os.rename("temp.csv","Staff.csv")

def modify_patientadmitted():
    global IDpatient
    m9=Toplevel()#Tk()#create a window
    m9.title("Modify Staff-KJ Group Of Hospital")
    m9.config(bg="#FFA07A")#to give backgrond colour
    head= Label(m9, text="KJ Group Of Hospitals", font=('Verdana 60 bold '), fg='white',bg='black')
    head.place(x=300, y=0)
    head= Label(m9, text="Modify the Reords of Patient Admitted" ,font=('Verdana 30 bold '), fg='black',bg='#20B2AA')
    head.place(x=360, y=110)
    l9=Label(m9,fg='black',text="Enter Patient ID",font='Verdana 28 ',bg='#FFFFE0')
    l9.place(x=220,y=200)
    l9=Button(m9,bg='#F08080',text="Search",font='Verdana 20 ',command=edit_patientadmitted_check)
    l9.place(x=620,y=260)
    IDpatient=Entry(m9,width=20,font='Verdana 12')
    IDpatient.place(x=600,y=220)
    head= Label(m9, text=" | Money and success don’t change people; they merely amplify what is already there | ", font=('Verdana 20 bold '), fg='white',bg='black')
    head.place(x=90, y=600)
    m9.geometry("600x600")
def edit_patientadmitted_check():
    global IDpatient
    k=IDpatient.get()
    m=open("PatientAD.csv",'r')
    c=csv.reader(m)
    e = 0
    for i in c:
        if i[0] == k :
            edit_patientadmitted()
            e = 1
    if e == 0:
        messagebox.showinfo("No Record"," No Record Found Please Check The ID" )
def edit_patientadmitted():
    global name,age,weight,gender,aadhar,address,phone,refered,problem,ward,IDpatient
    m3=Toplevel()#Tk()#create a window
    m3.title("Modify Patient-KJ Group Of Hospital")
    m3.config(bg="#FFF68F")#to give backgrond colour
    head= Label(m3, text="KJ Group Of Hospitals", font=('Verdana 65 bold '), fg='white',bg='black')
    head.place(x=230, y=0)
    head= Label(m3, text="Modify The Addmitted Patient Records", font=('Verdana 30 bold '), fg='black',bg='orange')
    head.place(x=340, y=130)
    l3=Label(m3,fg='black',text="Patient Name",font='Verdana 28 ',bg='#FFF68F')
    l3.place(x=220,y=200)
    l3=Label(m3,fg='black',text="Age",font='Verdana 28',bg='#FFF68F')
    l3.place(x=220,y=260)
    l3=Label(m3,fg='black',text="Weight",font='Verdana 28',bg='#FFF68F')
    l3.place(x=220,y=320)
    l3=Label(m3,fg='black',text="Gender",font='Verdana 28',bg='#FFF68F')
    l3.place(x=220,y=380)
    l3=Label(m3,fg='black',text="Aadhar",font='Verdana 28',bg='#FFF68F')
    l3.place(x=220,y=440)
    l3=Label(m3,fg='black',text="Address",font='Verdana 28',bg='#FFF68F')
    l3.place(x=860,y=200)
    l3=Label(m3,fg='black',text="Phone No.",font='Verdana 28',bg='#FFF68F')
    l3.place(x=860,y=260)
    l3=Label(m3,fg='black',text="Refered By",font='Verdana 28',bg='#FFF68F')
    l3.place(x=860,y=320)
    l3=Label(m3,fg='black',text="Problem",font='Verdana 28',bg='#FFF68F')
    l3.place(x=860,y=380)
    l3=Label(m3,fg='black',text="Ward",font='Verdana 28',bg='#FFF68F')
    l3.place(x=860,y=440)
    name=Entry(m3,width=20,font='Verdana 12')
    name.place(x=500,y=220)
    age=Entry(m3,width=20,font='Verdana 12')
    age.place(x=500,y=280)
    weight=Entry(m3,width=20,font='Verdana 12')
    weight.place(x=500,y=340)
    gender= ttk.Combobox(m3,
                            values=[
                                    "Male",
                                    "Female"])
    gender.place(x=500,y=400)
    aadhar=Entry(m3,width=20,font='Verdana 12')
    aadhar.place(x=500,y=460)
    address=Entry(m3,width=20,font='Verdana 12')
    address.place(x=1100,y=220)
    phone=Entry(m3,width=20,font='Verdana 12')
    phone.place(x=1100,y=280)
    refered=ttk.Combobox(m3,
                            values=[
                                    "Amrit Lal-Physician",
                                    "Rekha jaiswal-Gynoclogist",
                                    "Farrukh-sheikh-Orthopaedic",
                                    "Ravi verma-Surgeon",
                                    "Raghav Kataria-Immunologist",
                                    "Sahnice Shreshtha-Cardiologist",
                                    "Nikhil Verma-Neurologist",
                                    "Zahir Khan-Gastroenologist"])
    refered.place(x=1100,y=340)
    problem=Entry(m3,width=20,font='Verdana 12')
    problem.place(x=1100,y=400)
    ward= ttk.Combobox(m3,
                            values=[
                                    "ICU",
                                    "General Ward"])
    ward.place(x=1100,y=460)
    b1=Button(m3,text="Done",font='Verdana 20',command=Edited_PatientAdmitted)
    b1.place(x=720,y=500)
    head= Label(m3, text=" | The whole secret of a successful life is to find out what is one’s destiny to do, and then do it | ", font=('Verdana 20 bold '), fg='black',bg='white')
    head.place(x=30, y=730)
    m3.geometry("600x600")
def Edited_PatientAdmitted():
    global name,age,weight,gender,aadhar,address,phone,refered,problem,ward,IDpatient
    # getting the user inputs
    IDp=IDpatient.get()
    k=open("PatientAD.csv",'r')
    ff=open("temp.csv",'a+',newline='')
    cr=csv.reader(k)
    cw=csv.writer(ff)
    for i in cr :
        rec=[]
        # getting the user inputs
        val0 = IDp
        val1 = name.get()
        val2 = age.get()
        val3 = weight.get()
        val4 = gender.get()
        val5 = aadhar.get()
        val6 = address.get()
        val7 = phone.get()
        val8 = refered.get()
        val9 = problem.get()
        val10 = ward.get()
        val11 = i[11]
        val12 = i[12]
        val13 = i[13]
        rec.append(val0)
        rec.append(val1)
        rec.append(val2)
        rec.append(val3)
        rec.append(val4)
        rec.append(str(val5))
        rec.append(val6)
        rec.append(str(val7))
        rec.append(val8)
        rec.append(val9)
        rec.append(val10)
        rec.append(val11)
        rec.append(val12)
        rec.append(val13)
        if i[0]!=IDp:
            cw.writerow(i)
        else:
            cw.writerow(rec)
            rec.clear()
            messagebox.showinfo("Success", "The record has been edited" )

    k.close()
    ff.close()
    os.remove("PatientAD.csv")
    os.rename("temp.csv","PatientAD.csv")
def modify_patientdischarged():
    global IDdpatient
    m9=Toplevel()#Tk()#create a window
    m9.title("Modify Staff-KJ Group Of Hospital")
    m9.config(bg="#FFA54F")#to give backgrond colour
    head= Label(m9, text="KJ Group Of Hospitals", font=('Verdana 60 bold '), fg='white',bg='black')
    head.place(x=280, y=0)
    head= Label(m9, text="Modify the Reords of Patient Discharged" ,font=('Verdana 30 bold '), fg='black',bg='#008080')
    head.place(x=310, y=110)
    l9=Label(m9,fg='black',text="Enter Patient ID",font='Verdana 28 ',bg='#FFFFE0')
    l9.place(x=200,y=200)
    l9=Button(m9,bg='#EEAEEE',text="Search",font='Verdana 20 ',command=edit_patientdischarged_check)
    l9.place(x=600,y=260)
    IDdpatient=Entry(m9,width=20,font='Verdana 12')
    IDdpatient.place(x=580,y=218)
    head= Label(m9, text=" | In order to write about life first you must live it | ", font=('Verdana 25 bold '), fg='white',bg='black')
    head.place(x=270, y=600)
    m9.geometry("600x600")
def edit_patientdischarged_check():
    global IDdpatient
    r=IDdpatient.get()
    m=open("PatientDis.csv",'r')
    c=csv.reader(m)
    e=0
    for i in c:
        if i[0] == r :
            edit_patientdischarged()
            e=1
    if e == 0:
        messagebox.showinfo("No Record"," No Record Found Please Check The ID" )
def edit_patientdischarged():
    global name,age,weight,gender,aadhar,address,phone,refered,problem,ward,IDdpatient
    m3=Toplevel()#Tk()#create a window
    m3.title("Modify Patient-KJ Group Of Hospital")
    m3.config(bg="#FF8247")#to give backgrond colour
    head= Label(m3, text="KJ Group Of Hospitals", font=('Verdana 65 bold '), fg='white',bg='black')
    head.place(x=230, y=0)
    head= Label(m3, text="Modify The Discharged Patient Records", font=('Verdana 30 bold '), fg='black',bg='White')
    head.place(x=330, y=120)
    l3=Label(m3,fg='black',text="Patient Name",font='Verdana 28 ',bg='#FF8247')
    l3.place(x=240,y=200)
    l3=Label(m3,fg='black',text="Age",font='Verdana 28',bg='#FF8247')
    l3.place(x=240,y=260)
    l3=Label(m3,fg='black',text="Weight",font='Verdana 28',bg='#FF8247')
    l3.place(x=240,y=320)
    l3=Label(m3,fg='black',text="Gender",font='Verdana 28',bg='#FF8247')
    l3.place(x=240,y=380)
    l3=Label(m3,fg='black',text="Aadhar",font='Verdana 28',bg='#FF8247')
    l3.place(x=240,y=440)
    l3=Label(m3,fg='black',text="Address",font='Verdana 28',bg='#FF8247')
    l3.place(x=880,y=200)
    l3=Label(m3,fg='black',text="Phone No.",font='Verdana 28',bg='#FF8247')
    l3.place(x=880,y=260)
    l3=Label(m3,fg='black',text="Refered By",font='Verdana 28',bg='#FF8247')
    l3.place(x=860,y=320)
    l3=Label(m3,fg='black',text="Problem",font='Verdana 28',bg='#FF8247')
    l3.place(x=880,y=380)
    l3=Label(m3,fg='black',text="Ward",font='Verdana 28',bg='#FF8247')
    l3.place(x=880,y=440)
    name=Entry(m3,width=20,font='Verdana 12')
    name.place(x=520,y=220)
    age=Entry(m3,width=20,font='Verdana 12')
    age.place(x=520,y=280)
    weight=Entry(m3,width=20,font='Verdana 12')
    weight.place(x=520,y=340)
    gender= ttk.Combobox(m3,
                            values=[
                                    "Male",
                                    "Female"])
    gender.place(x=520,y=400)
    aadhar=Entry(m3,width=20,font='Verdana 12')
    aadhar.place(x=520,y=460)
    address=Entry(m3,width=20,font='Verdana 12')
    address.place(x=1100,y=220)
    phone=Entry(m3,width=20,font='Verdana 12')
    phone.place(x=1100,y=280)
    refered=ttk.Combobox(m3,
                            values=[
                                    "Amrit Lal-Physician",
                                    "Rekha jaiswal-Gynoclogist",
                                    "Farrukh-sheikh-Orthopaedic",
                                    "Ravi verma-Surgeon",
                                    "Raghav Kataria-Immunologist",
                                    "Sahnice Shreshtha-Cardiologist",
                                    "Nikhil Verma-Neurologist",
                                    "Zahir Khan-Gastroenologist"])
    refered.place(x=1100,y=340)
    problem=Entry(m3,width=20,font='Verdana 12')
    problem.place(x=1100,y=400)
    ward= ttk.Combobox(m3,
                            values=[
                                    "ICU",
                                    "General Ward"])
    ward.place(x=1100,y=460)
    b1=Button(m3,text="Done",font='Verdana 20',command=Edited_PatientDischarged)
    b1.place(x=740,y=520)
    head= Label(m3, text=" | Life is not a problem to be solved, but a reality to be experienced | ", font=('Verdana 25 bold '), fg='black',bg='white')
    head.place(x=130, y=730)
    m3.geometry("600x600")
def Edited_PatientDischarged():
    global name,age,weight,gender,aadhar,address,phone,refered,problem,ward,IDdpatient
    # getting the user inputs
    IDdp=IDdpatient.get()
    k=open("PatientDis.csv",'r')
    ff=open("temp.csv",'a+',newline='')
    cr=csv.reader(k)
    cw=csv.writer(ff)
    for i in cr :
        rec=[]
        # getting the user inputs
        val0 = IDdp
        val1 = name.get()
        val2 = age.get()
        val3 = weight.get()
        val4 = gender.get()
        val5 = aadhar.get()
        val6 = address.get()
        val7 = phone.get()
        val8 = i[8]
        val9 = problem.get()
        val10 = ward.get()
        val11 = i[11]
        val12 = i[12]
        val13 = i[13]
        val14 = i[14]
        val15 = i[15]
        rec.append(val0)
        rec.append(val1)
        rec.append(val2)
        rec.append(val3)
        rec.append(val4)
        rec.append(val5)
        rec.append(str(val6))
        rec.append(str(val7))
        rec.append(val8)
        rec.append(val9)
        rec.append(val10)
        rec.append(val11)
        rec.append(val12)
        rec.append(val13)
        rec.append(val14)
        rec.append(val15)
        if i[0]!=IDdp:
            cw.writerow(i)
        else:
            cw.writerow(rec)
            rec.clear()
            messagebox.showinfo("Success", "The record has been edited" )

    k.close()
    ff.close()
    os.remove("PatientDis.csv")
    os.rename("temp.csv","PatientDis.csv")

def Hire_Staff_Window():
    global StaffName,Age,Gender,Aadhar,Phone,Desig,Address
    m2=Toplevel()#Tk()#create a window
    m2.title("HIRING-KJ Group Of Hospital")
    m2.config(bg="#EE3A8C")#to give backgrond colour
    head= Label(m2, text="KJ Group Of Hospitals", font=('Verdana 65 bold '), fg='white',bg='black')
    head.place(x=250, y=0)
    head= Label(m2, text=" Details Of Staff ", font=('Verdana 32 bold '), fg='black',bg='orange')
    head.place(x=580, y=115)
    l2=Label(m2,fg='black',text="Staff Name",font='Verdana 28',bg='#EE3A8C')
    l2.place(x=200,y=240)
    l3=Label(m2,fg='black',text="Age",font='Verdana 28',bg='#EE3A8C')
    l3.place(x=200,y=300)
    l3=Label(m2,fg='black',text="Gender",font='Verdana 28',bg='#EE3A8C')
    l3.place(x=200,y=360)
    l2=Label(m2,fg='black',text="Aadhar No.",font='Verdana 28',bg='#EE3A8C')
    l2.place(x=200,y=420)
    l2=Label(m2,fg='black',text="Phone No.",font='Verdana 28',bg='#EE3A8C')
    l2.place(x=200,y=480)
    l2=Label(m2,fg='black',text="Designation",font='Verdana 28',bg='#EE3A8C')
    l2.place(x=200,y=540)
    l2=Label(m2,fg='black',text="Address",font='Verdana 28',bg='#EE3A8C')
    l2.place(x=200,y=600)
    StaffName=Entry(m2,width=20,font='Verdana 12')
    StaffName.place(x=430,y=258)
    Age=Entry(m2,width=20,font='Verdana 12')
    Age.place(x=430,y=318)
    Gender= ttk.Combobox(m2,
                            values=[
                                    "Male",
                                    "Female"])
    Gender.place(x=430,y=378)
    Aadhar=Entry(m2,width=20,font='Verdana 12')
    Aadhar.place(x=430,y=438)
    Phone=Entry(m2,width=20,font='Verdana 12')
    Phone.place(x=430,y=498)
    Desig=Entry(m2,width=20,font='Verdana 12')
    Desig.place(x=430,y=558)
    Address=Entry(m2,width=20,font='Verdana 12')
    Address.place(x=430,y=618)
    b2=Button(m2,text="Done",font='Verdana 20',command=hire)
    b2.place(x=440,y=670)
    head= Label(m2, text=" | Life is really simple, but we insist on making it complicated | ", font=('Verdana 25 bold '), fg='black',bg='white')
    head.place(x=180, y=740)
    m2.geometry("600x600")

def hire():
        rec=[]
        global StaffName,Age,Gender,Aadhar,Phone,Desig,Address,n
        # getting the user inputs
        val1 = n+1
        n=val1
        val2 = StaffName.get()
        val3 = Age.get()
        val4 = Gender.get()
        val5 = Aadhar.get()
        val6 = Phone.get()
        val7 = Desig.get()
        val8 = Address.get()
        today=date.today()
        d1 = today.strftime("%d/%m/%Y")
        val9=d1
        rec.append(val1)
        rec.append(val2)
        rec.append(val3)
        rec.append(val4)
        rec.append(str(val5))
        rec.append(str(val6))
        rec.append(val7)
        rec.append(val8)
        rec.append(str(val9))

        # checking if the user input is empty
        if val1 == '' or val2 == '' or val3 == '' or val4 == '' or val5 == '' or val6=='':
            messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        if len(val5)!= 12 or len(val6)!= 10 :
            messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            # now we add to the database
            k=open("Staff.csv","a+",newline='')
            we=csv.writer(k)
            we.writerow(rec)
            rec=[]
            k.close()
            messagebox.showinfo("Success", "Congrats " + val2 + ", Welcome in KJ Group Of Hospitals")

First_Window()
