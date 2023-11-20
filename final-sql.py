import tkinter as tk
import tkinter.ttk as ttk
# import pymongo
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="hospital"
)

myCursor = db.cursor()

root = tk.Tk()
root.title("Hospital Management Software")
root.geometry('600x400')


def AdminWindow():
    AdminWindow = tk.Toplevel(root)
    AdminWindow.geometry('600x400')
    AdminWindow.title("Administrator")
    adLabel = tk.Label(AdminWindow, text="Enter your login details:", font=("Arial", 16), fg="Black")
    adLabel.place(x=200, y=50)
    idLabel = tk.Label(AdminWindow, text="Id:", font=("Lucida Console", 12), fg="Black")
    idLabel.place(x=60, y=150)
    idtext = tk.Entry(AdminWindow, width=30)
    idtext.place(x=100, y=150)
    pwrdL = tk.Label(AdminWindow, text="Password:", font=("Lucida Console", 12), fg="Black")
    pwrdL.place(x=60, y=180)
    pwrd = tk.Entry(AdminWindow, width=30, show='*')
    pwrd.place(x=155, y=180)

    def login():
        if idtext.get() == 'admin' and pwrd.get() == 'admin':

            l1 = tk.Label(AdminWindow, text="Login Successful!!", fg="Red")
            l1.place(x=200, y=90)
            adminopr = tk.Toplevel(AdminWindow)
            adminopr.geometry('600x400')
            adminopr.title("Administrator")
            helloL = tk.Label(adminopr, text="Hello!! Administrator", font=("Comic Sans MS", 10), fg="Red")
            helloL.place(x=20, y=50)
            oprL = tk.Label(adminopr, text="Select your task", font=("Arial", 12), fg="Black")
            oprL.place(x=225, y=100)

            def adoct():
                doc = tk.Toplevel(adminopr)
                doc.geometry('600x400')
                doc.title("Add Doctor")
                headL = tk.Label(doc, text="Enter the following details:", font=("Arial", 10), fg="Blue")
                headL.place(x=50, y=30)
                iLabel = tk.Label(doc, text="Id:", font=("Arial", 9), fg="Black")  # DocID
                iLabel.place(x=30, y=75)
                itext = tk.Entry(doc, width=25)
                itext.place(x=50, y=75)
                nLabel = tk.Label(doc, text="Name:", font=("Arial", 9), fg="Black")  # Name
                nLabel.place(x=30, y=115)
                ntext = tk.Entry(doc, width=25)
                ntext.place(x=80, y=115)
                gLabel = tk.Label(doc, text="Gender:", font=("Arial", 9), fg="Black")  # Gender
                gLabel.place(x=30, y=155)
                gtext = tk.Entry(doc, width=25)
                gtext.place(x=80, y=155)
                dobLabel = tk.Label(doc, text="DOB:", font=("Arial", 9), fg="Black")  # DateOfBirth
                dobLabel.place(x=30, y=195)
                dobtext = tk.Entry(doc, width=25)
                dobtext.place(x=70, y=195)
                qLabel = tk.Label(doc, text="Qualification:", font=("Arial", 9), fg="Black")  # Qualification
                qLabel.place(x=30, y=235)
                qtext = tk.Entry(doc, width=25)
                qtext.place(x=110, y=235)
                dLabel = tk.Label(doc, text="Dept:", font=("Arial", 9), fg="Black")  # Department
                dLabel.place(x=30, y=275)
                dtext = tk.Entry(doc, width=25)
                dtext.place(x=70, y=275)
                aLabel = tk.Label(doc, text="Address:", font=("Arial", 9), fg="Black")  # Address
                aLabel.place(x=30, y=315)
                atext = tk.Entry(doc, width=25)
                atext.place(x=90, y=315)
                pLabel = tk.Label(doc, text="PhoneNo:", font=("Arial", 9), fg="Black")  # PhoneNo
                pLabel.place(x=30, y=355)
                pno = tk.Entry(doc, width=25)
                pno.place(x=95, y=355)
                salLabel = tk.Label(doc, text="Salary:", font=("Arial", 9), fg="Black")  # Salary
                salLabel.place(x=320, y=30)
                saltext = tk.Entry(doc, width=15)
                saltext.place(x=370, y=30)
                password = tk.Label(doc, text="Set Password:", font=("Arial", 9), fg="Black")  # Login_Password
                password.place(x=320, y=70)
                password_text = tk.Entry(doc, width=20, show='*')
                password_text.place(x=410, y=70)

                def reset():
                    itext.delete(0, tk.END)
                    ntext.delete(0, tk.END)
                    gtext.delete(0, tk.END)
                    dobtext.delete(0, tk.END)
                    qtext.delete(0, tk.END)
                    dtext.delete(0, tk.END)
                    atext.delete(0, tk.END)
                    pno.delete(0, tk.END)
                    saltext.delete(0, tk.END)
                    password_text.delete(0, tk.END)

                def submit():
                    myCursor.execute("insert into Login_Det(id , password) values (%s,%s)", (itext.get(),
                                                                                             password_text.get()))

                    myCursor.execute("insert into doctor(DocId,name,gender,dob,Qualification,department,address,"
                                     "salary,phone) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (itext.get(), ntext.get(),
                        gtext.get(), dobtext.get(),qtext.get(), dtext.get(),atext.get(), saltext.get(),pno.get()))

                    db.commit()

                    done_label = tk.Label(doc, text="Doctor added successfully!!", font=("Arial", 8), fg="Black")
                    done_label.place(x=410, y=280)

                reset_button = tk.Button(doc, text="Reset", width=9, height=1, command=reset)
                reset_button.place(x=450, y=200)
                submit_button = tk.Button(doc, text="Submit", width=9, height=1, command=submit)
                submit_button.place(x=450, y=245)

            def get_det(doc_id):
                myCursor.execute("select * from doctor where docId = %s", (doc_id,))
                doctor = myCursor.fetchone()
                print(doctor)
                return doctor

            def edoct():
                edit = tk.Toplevel(adminopr)
                edit.geometry('600x400')
                edit.title("Edit Doctor Details")
                iLabel = tk.Label(edit, text="Id:", font=("Arial", 9), fg="Black")  # DocID
                iLabel.place(x=30, y=75)
                itext = tk.Entry(edit, width=25)
                itext.place(x=50, y=75)
                nLabel = tk.Label(edit, text="Name:", font=("Arial", 9), fg="Black")  # Name
                nLabel.place(x=30, y=115)
                ntext = tk.Entry(edit, width=25)
                ntext.place(x=80, y=115)
                gLabel = tk.Label(edit, text="Gender:", font=("Arial", 9), fg="Black")  # Gender
                gLabel.place(x=30, y=155)
                gtext = tk.Entry(edit, width=25)
                gtext.place(x=80, y=155)
                dobLabel = tk.Label(edit, text="DOB:", font=("Arial", 9), fg="Black")  # DateOfBirth
                dobLabel.place(x=30, y=195)
                dobtext = tk.Entry(edit, width=25)
                dobtext.place(x=70, y=195)
                qLabel = tk.Label(edit, text="Qualification:", font=("Arial", 9), fg="Black")  # Qualification
                qLabel.place(x=30, y=235)
                qtext = tk.Entry(edit, width=25)
                qtext.place(x=110, y=235)
                dLabel = tk.Label(edit, text="Dept:", font=("Arial", 9), fg="Black")  # Department
                dLabel.place(x=30, y=275)
                dtext = tk.Entry(edit, width=25)
                dtext.place(x=70, y=275)
                aLabel = tk.Label(edit, text="Address:", font=("Arial", 9), fg="Black")  # Address
                aLabel.place(x=30, y=315)
                atext = tk.Entry(edit, width=25)
                atext.place(x=90, y=315)
                pLabel = tk.Label(edit, text="PhoneNo:", font=("Arial", 9), fg="Black")  # PhoneNo
                pLabel.place(x=30, y=355)
                pno = tk.Entry(edit, width=25)
                pno.place(x=95, y=355)
                salLabel = tk.Label(edit, text="Salary:", font=("Arial", 9), fg="Black")  # Salary
                salLabel.place(x=320, y=30)
                saltext = tk.Entry(edit, width=15)
                saltext.place(x=370, y=30)

                def get_details():
                    doc_id = itext.get()
                    doctor = get_det(doc_id)
                    if doctor is not None:
                        ntext.delete(0, tk.END)
                        ntext.insert(0, doctor[1])
                        ntext.config(state='disabled')
                        gtext.insert(0, doctor[2])
                        gtext.config(state='disabled')
                        dobtext.insert(0, doctor[3])
                        dobtext.config(state='disabled')
                        qtext.delete(0, tk.END)
                        qtext.insert(0, doctor[4])
                        qtext.config(state='disabled')
                        dtext.delete(0, tk.END)
                        dtext.insert(0, doctor[5])
                        atext.delete(0, tk.END)
                        atext.insert(0, doctor[6])
                        pno.delete(0, tk.END)
                        pno.insert(0, doctor[7])
                        saltext.delete(0, tk.END)
                        saltext.insert(0, doctor[8])

                def update_details():
                    doc_id = itext.get()
                    myCursor.execute("update doctor set Department = %s, address = %s, phone = %s ,salary = %s where "
                                     "docId = %s", (dtext.get(), atext.get(), pno.get(), saltext.get(), doc_id))

                    db.commit()

                    done_label = tk.Label(edit, text="Doctor edited successfully!!", font=("Arial", 8), fg="Black")
                    done_label.place(x=400, y=280)

                updt_btn = tk.Button(edit, text="Update", width=9, height=1, command=update_details)
                updt_btn.place(x=450, y=250)
                get_btn = tk.Button(edit, text="Get Details", width=10, height=1, command=get_details)
                get_btn.place(x=450, y=200)

            def addstaff():
                staff = tk.Toplevel(adminopr)
                staff.geometry('600x400')
                staff.title("Add Staff")
                headL = tk.Label(staff, text="Enter the following details:", font=("Arial", 10), fg="Blue")
                headL.place(x=50, y=30)
                iLabel = tk.Label(staff, text="Id:", font=("Arial", 9), fg="Black")  # StaffID
                iLabel.place(x=30, y=75)
                itext = tk.Entry(staff, width=25)
                itext.place(x=50, y=75)
                nLabel = tk.Label(staff, text="Name:", font=("Arial", 9), fg="Black")  # Name
                nLabel.place(x=30, y=115)
                ntext = tk.Entry(staff, width=25)
                ntext.place(x=80, y=115)
                gLabel = tk.Label(staff, text="Gender:", font=("Arial", 9), fg="Black")  # Gender
                gLabel.place(x=30, y=155)
                gtext = tk.Entry(staff, width=25)
                gtext.place(x=80, y=155)
                dobLabel = tk.Label(staff, text="DOB:", font=("Arial", 9), fg="Black")  # DateOfBirth
                dobLabel.place(x=30, y=195)
                dobtext = tk.Entry(staff, width=25)
                dobtext.place(x=70, y=195)
                desLabel = tk.Label(staff, text="Designation:", font=("Arial", 9), fg="Black")  # Designations
                desLabel.place(x=30, y=235)
                destext = tk.Entry(staff, width=25)
                destext.place(x=110, y=235)
                salLabel = tk.Label(staff, text="Salary:", font=("Arial", 9), fg="Black")  # Salary
                salLabel.place(x=30, y=275)
                saltext = tk.Entry(staff, width=25)
                saltext.place(x=70, y=275)
                aLabel = tk.Label(staff, text="Address:", font=("Arial", 9), fg="Black")  # Address
                aLabel.place(x=30, y=315)
                atext = tk.Entry(staff, width=25)
                atext.place(x=90, y=315)
                pLabel = tk.Label(staff, text="PhoneNo:", font=("Arial", 9), fg="Black")  # PhoneNo
                pLabel.place(x=30, y=355)
                pno = tk.Entry(staff, width=25)
                pno.place(x=95, y=355)
                password = tk.Label(staff, text="Set Password", font=("Arial", 9), fg="Black")
                password.place(x=320, y=30)
                pass_text = tk.Entry(staff, width=20, show='*')
                pass_text.place(x=410, y=30)
                instrcn = tk.Label(staff, text="*only for receptionist//", font=("Arial", 8), fg="Red")
                instrcn.place(x=410, y=60)

                def reset():
                    itext.delete(0, tk.END)
                    ntext.delete(0, tk.END)
                    gtext.delete(0, tk.END)
                    dobtext.delete(0, tk.END)
                    destext.delete(0, tk.END)
                    saltext.delete(0, tk.END)
                    atext.delete(0, tk.END)
                    pno.delete(0, tk.END)
                    pass_text.delete(0, tk.END)

                def submit():
                    myCursor.execute("insert into Login_Det (id,password) values (%s, %s)",
                                     (itext.get(), pass_text.get()))


                    myCursor.execute("insert into staff (id,name,gender,dob,designation,salary,address,phone) values("
                                     "%s,%s,%s,%s,%s,%s,%s,%s)", (itext.get(), ntext.get(), gtext.get(), dobtext.get(),
                                                                  destext.get(), saltext.get(), atext.get(), pno.get()))

                    db.commit()

                    done_label = tk.Label(staff, text="Staff added successfully!!", font=("Arial", 8), fg="Black")
                    done_label.place(x=410, y=280)

                reset_button = tk.Button(staff, text="Reset", width=9, height=1, command=reset)
                reset_button.place(x=450, y=200)
                submit_button = tk.Button(staff, text="Submit", width=9, height=1, command=submit)
                submit_button.place(x=450, y=245)

            def get_staffdet(st_id):
                myCursor.execute("select * from staff where id = %s", (st_id,))
                staff = myCursor.fetchone()
                return staff

            def editstaff():
                edits = tk.Toplevel(adminopr)
                edits.geometry('600x400')
                edits.title("Edit Staff Details")
                iLabel = tk.Label(edits, text="Id:", font=("Arial", 9), fg="Black")  # StaffID
                iLabel.place(x=30, y=75)
                itext = tk.Entry(edits, width=25)
                itext.place(x=50, y=75)
                nLabel = tk.Label(edits, text="Name:", font=("Arial", 9), fg="Black")  # Name
                nLabel.place(x=30, y=115)
                ntext = tk.Entry(edits, width=25)
                ntext.place(x=80, y=115)
                gLabel = tk.Label(edits, text="Gender:", font=("Arial", 9), fg="Black")  # Gender
                gLabel.place(x=30, y=155)
                gtext = tk.Entry(edits, width=25)
                gtext.place(x=80, y=155)
                dobLabel = tk.Label(edits, text="DOB:", font=("Arial", 9), fg="Black")  # DateOfBirth
                dobLabel.place(x=30, y=195)
                dobtext = tk.Entry(edits, width=25)
                dobtext.place(x=70, y=195)
                desLabel = tk.Label(edits, text="Designation:", font=("Arial", 9), fg="Black")  # Designation
                desLabel.place(x=30, y=235)
                destext = tk.Entry(edits, width=25)
                destext.place(x=110, y=235)
                salLabel = tk.Label(edits, text="Salary:", font=("Arial", 9), fg="Black")  # Salary
                salLabel.place(x=30, y=275)
                saltext = tk.Entry(edits, width=25)
                saltext.place(x=70, y=275)
                aLabel = tk.Label(edits, text="Address:", font=("Arial", 9), fg="Black")  # Address
                aLabel.place(x=30, y=315)
                atext = tk.Entry(edits, width=25)
                atext.place(x=90, y=315)
                pLabel = tk.Label(edits, text="PhoneNo:", font=("Arial", 9), fg="Black")  # PhoneNo
                pLabel.place(x=30, y=355)
                pno = tk.Entry(edits, width=25)
                pno.place(x=95, y=355)

                def get_detail():
                    st_id = itext.get()
                    staff = get_staffdet(st_id)
                    if staff is not None:
                        ntext.delete(0, tk.END)
                        ntext.insert(0, staff[1])
                        ntext.config(state='disabled')

                        gtext.delete(0, tk.END)
                        gtext.insert(0, staff[2])
                        gtext.config(state='disabled')

                        dobtext.delete(0, tk.END)
                        dobtext.insert(0, staff[3])
                        dobtext.config(state='disabled')

                        destext.delete(0, tk.END)
                        destext.insert(0, staff[4])

                        saltext.delete(0, tk.END)
                        saltext.insert(0, staff[5])

                        atext.delete(0, tk.END)
                        atext.insert(0, staff[6])

                        pno.delete(0, tk.END)
                        pno.insert(0, staff[7])

                def update_details():
                    st_id = itext.get()

                    myCursor.execute("update staff set designation = %s, salary = %s, address = %s, phone = %s where "
                                     "id = %s", (destext.get(), saltext.get(), atext.get(), pno.get(), st_id))

                    db.commit()

                    done_label = tk.Label(edits, text="Staff edited successfully!!", font=("Arial", 8), fg="Black")
                    done_label.place(x=410, y=280)

                updt_btn = tk.Button(edits, text="Update", width=9, height=1, command=update_details)
                updt_btn.place(x=450, y=250)
                get_btn1 = tk.Button(edits, text="Get Details", width=10, height=1, command=get_detail)
                get_btn1.place(x=450, y=200)

            adoc = tk.Button(adminopr, text="Add Doctor", width=12, height=2, command=adoct)
            adoc.place(x=225, y=135)
            edoc = tk.Button(adminopr, text="Edit Doctor", width=12, height=2, command=edoct)
            edoc.place(x=225, y=180)
            astaff = tk.Button(adminopr, text="Add staff", width=12, height=2, command=addstaff)
            astaff.place(x=225, y=225)
            estaff = tk.Button(adminopr, text="Edit Staff", width=12, height=2, command=editstaff)
            estaff.place(x=225, y=270)
        else:
            l1 = tk.Label(AdminWindow, text="Wrong Id or Password entered!!", fg="Red")
            l1.place(x=200, y=90)

    btn2 = tk.Button(AdminWindow, text="Login", width=12, height=2, bg='#FFFFFF', command=login)
    btn2.place(x=200, y=300)


def EmpWindow():
    EmpWindow = tk.Toplevel(root)
    EmpWindow.geometry('600x400')
    EmpWindow.title("Employee")

    # login_details = db['Login_Det']

    headLabel = tk.Label(EmpWindow, text="Enter your login details:", font=("Arial", 16), fg="Black")
    headLabel.place(x=200, y=50)
    id1 = tk.Label(EmpWindow, text="Id:", font=("Lucida Console", 12), fg="Black")
    id1.place(x=60, y=150)
    idinp = tk.Entry(EmpWindow, width=30)
    idinp.place(x=100, y=150)
    pwrdL = tk.Label(EmpWindow, text="Password:", font=("Lucida Console", 12), fg="Black")
    pwrdL.place(x=60, y=180)
    pwrd = tk.Entry(EmpWindow, width=30, show='*')
    pwrd.place(x=155, y=180)

    def login():
        global emp_id
        emp_id = idinp.get()
        # doc = login_details.find_one({'ID': emp_id})

        myCursor.execute("select * from login_Det where id = %s", (emp_id,))
        doc = myCursor.fetchone()
        first_char = emp_id[0]
        if doc is not None:


            passwrd = doc[1]
            if pwrd.get() == passwrd:
                l1 = tk.Label(EmpWindow, text="Login Successful!!", fg="Red")
                l1.place(x=200, y=90)
                if first_char == 'r' or first_char == 'R':
                    recep = tk.Toplevel(EmpWindow)
                    recep.geometry('600x400')
                    recep.title("Reception")

                    def add_patient():
                        add_pat = tk.Toplevel(recep)
                        add_pat.geometry('600x400')
                        add_pat.title("Add Patient")
                        headL = tk.Label(add_pat, text="Enter the following details:", font=("Arial", 10), fg="Blue")
                        headL.place(x=50, y=30)
                        iLabel = tk.Label(add_pat, text="Id:", font=("Arial", 9), fg="Black")  # PatientID
                        iLabel.place(x=30, y=75)
                        itext = tk.Entry(add_pat, width=25)
                        itext.place(x=50, y=75)
                        nLabel = tk.Label(add_pat, text="Name:", font=("Arial", 9), fg="Black")  # Name
                        nLabel.place(x=30, y=115)
                        ntext = tk.Entry(add_pat, width=25)
                        ntext.place(x=80, y=115)
                        gLabel = tk.Label(add_pat, text="Gender:", font=("Arial", 9), fg="Black")  # Gender
                        gLabel.place(x=30, y=155)
                        gtext = tk.Entry(add_pat, width=25)
                        gtext.place(x=80, y=155)
                        dobLabel = tk.Label(add_pat, text="DOB:", font=("Arial", 9), fg="Black")  # DateOfBirth
                        dobLabel.place(x=30, y=195)
                        dobtext = tk.Entry(add_pat, width=25)
                        dobtext.place(x=70, y=195)
                        insLabel = tk.Label(add_pat, text="Insurance:", font=("Arial", 9), fg="Black")  # Insurance
                        insLabel.place(x=30, y=235)
                        instext = tk.Entry(add_pat, width=25)
                        instext.place(x=95, y=235)
                        aLabel = tk.Label(add_pat, text="Address:", font=("Arial", 9), fg="Black")  # Address
                        aLabel.place(x=30, y=275)
                        atext = tk.Entry(add_pat, width=25)
                        atext.place(x=85, y=275)
                        pLabel = tk.Label(add_pat, text="PhoneNo:", font=("Arial", 9), fg="Black")  # PhoneNo
                        pLabel.place(x=30, y=315)
                        pno = tk.Entry(add_pat, width=25)
                        pno.place(x=90, y=315)

                        def reset():
                            itext.delete(0, tk.END)
                            ntext.delete(0, tk.END)
                            gtext.delete(0, tk.END)
                            dobtext.delete(0, tk.END)
                            instext.delete(0, tk.END)
                            atext.delete(0, tk.END)
                            pno.delete(0, tk.END)

                        def submit():

                            myCursor.execute("insert into patient(patientId,name,gender,dob,Insurance,address,phone) "
                                             "values(%s,%s,%s,%s,%s,%s,%s)", (itext.get(), ntext.get(), gtext.get(),
                                                                              dobtext.get(), instext.get(), atext.get(),
                                                                              pno.get()))

                            db.commit()
                            done_label = tk.Label(add_pat, text="Patient added successfully!!", font=("Arial", 8),
                                                  fg="Black")
                            done_label.place(x=410, y=280)

                        reset_button = tk.Button(add_pat, text="Reset", width=9, height=1, command=reset)
                        reset_button.place(x=450, y=200)
                        submit_button = tk.Button(add_pat, text="Submit", width=9, height=1, command=submit)
                        submit_button.place(x=450, y=245)

                    def get_det(pat_id):
                        myCursor.execute("select * from patient where patientID = %s", (pat_id,))
                        patient = myCursor.fetchone()
                        return patient

                    def edit_patient():
                        edit_pat = tk.Toplevel(recep)
                        edit_pat.geometry('600x400')
                        edit_pat.title("Update Patient Details")
                        iLabel = tk.Label(edit_pat, text="Id:", font=("Arial", 9), fg="Black")  # PatientID
                        iLabel.place(x=30, y=75)
                        itext = tk.Entry(edit_pat, width=25)
                        itext.place(x=50, y=75)
                        nLabel = tk.Label(edit_pat, text="Name:", font=("Arial", 9), fg="Black")  # Name
                        nLabel.place(x=30, y=115)
                        ntext = tk.Entry(edit_pat, width=25)
                        ntext.place(x=80, y=115)
                        gLabel = tk.Label(edit_pat, text="Gender:", font=("Arial", 9), fg="Black")  # Gender
                        gLabel.place(x=30, y=155)
                        gtext = tk.Entry(edit_pat, width=25)
                        gtext.place(x=80, y=155)
                        dobLabel = tk.Label(edit_pat, text="DOB:", font=("Arial", 9), fg="Black")  # DateOfBirth
                        dobLabel.place(x=30, y=195)
                        dobtext = tk.Entry(edit_pat, width=25)
                        dobtext.place(x=70, y=195)
                        insLabel = tk.Label(edit_pat, text="Insurance:", font=("Arial", 9), fg="Black")  # Insurance
                        insLabel.place(x=30, y=235)
                        instext = tk.Entry(edit_pat, width=25)
                        instext.place(x=95, y=235)
                        aLabel = tk.Label(edit_pat, text="Address:", font=("Arial", 9), fg="Black")  # Address
                        aLabel.place(x=30, y=275)
                        atext = tk.Entry(edit_pat, width=25)
                        atext.place(x=85, y=275)
                        pLabel = tk.Label(edit_pat, text="PhoneNo:", font=("Arial", 9), fg="Black")  # PhoneNo
                        pLabel.place(x=30, y=315)
                        pno = tk.Entry(edit_pat, width=25)
                        pno.place(x=90, y=315)

                        def get_details():
                            pat_id = itext.get()
                            patient = get_det(pat_id)
                            if patient is not None:
                                ntext.delete(0, tk.END)
                                ntext.insert(0, patient[1])
                                ntext.config(state='disabled')

                                gtext.delete(0, tk.END)
                                gtext.insert(0, patient[2])
                                gtext.config(state='disabled')

                                dobtext.delete(0, tk.END)
                                dobtext.insert(0, patient[3])
                                dobtext.config(state='disabled')

                                instext.delete(0, tk.END)
                                instext.insert(0, patient[4])

                                atext.delete(0, tk.END)
                                atext.insert(0, patient[5])

                                pno.delete(0, tk.END)
                                pno.insert(0, patient[6])

                        def update_details():
                            pat_id = itext.get()
                            myCursor.execute("update patient set Insurance=%s, address=%s, phone=%s where patientID=%s",
                                             (instext.get(), atext.get(), pno.get(), pat_id))
                            db.commit()

                            done_label = tk.Label(edit_pat, text="Patient edited successfully!!", font=("Arial", 8),
                                                  fg="Black")
                            done_label.place(x=410, y=280)

                        updt_btn = tk.Button(edit_pat, text="Update", width=9, height=1, command=update_details)
                        updt_btn.place(x=450, y=250)
                        get_btn = tk.Button(edit_pat, text="Get Details", width=10, height=1, command=get_details)
                        get_btn.place(x=450, y=200)

                    def add_appointment():
                        new_appt = tk.Toplevel(recep)
                        new_appt.geometry('200x350')
                        new_appt.title("New Appointment")
                        hlabel = tk.Label(new_appt, text="Enter the following details:", font=("Arial", 10), fg="Blue")
                        hlabel.place(x=25, y=30)
                        ilabel = tk.Label(new_appt, text="Patient's Id:", font=("Arial", 9), fg="Red")
                        ilabel.place(x=30, y=75)
                        itext = tk.Entry(new_appt, width=10)
                        itext.place(x=100, y=75)
                        dilabel = tk.Label(new_appt, text="Doctor's Id:", font=("Arial", 9), fg="Red")
                        dilabel.place(x=30, y=105)
                        ditext = tk.Entry(new_appt, width=10)
                        ditext.place(x=100, y=105)
                        datel = tk.Label(new_appt, text="Date:", font=("Arial", 9), fg="Red")
                        datel.place(x=30, y=140)
                        date = tk.Entry(new_appt, width=13)
                        date.place(x=70, y=140)
                        timel = tk.Label(new_appt, text="Time", font=("Arial", 9), fg="Red")
                        timel.place(x=30, y=170)
                        timet = tk.Entry(new_appt, width=12)
                        timet.place(x=70, y=170)
                        apptl = tk.Label(new_appt, text="Appt. No.", font=("Arial", 9), fg="Red")
                        apptl.place(x=30, y=200)
                        apptn = tk.Entry(new_appt, width=5)
                        apptn.place(x=90, y=200)
                        statl = tk.Label(new_appt, text="Status", font=("Arial", 9), fg="Red")
                        statl.place(x=30, y=230)
                        stat = tk.Entry(new_appt, width=6)
                        stat.place(x=80, y=230)

                        def add():
                            myCursor.execute("insert into appointment(appointmentNo,patientid,docid,a_date,a_time,"
                                             "status) values(%s,%s,%s,%s,%s,%s)",
                                             (apptn.get(), itext.get(), ditext.get(),
                                              date.get(), timet.get(), stat.get()))

                            db.commit()

                            done_label = tk.Label(new_appt, text="Appointment added successfully!!", font=("Arial", 8),
                                                  fg="Black")
                            done_label.place(x=20, y=250)

                        add_btn = tk.Button(new_appt, text="Add", width=9, height=1, command=add)
                        add_btn.place(x=50, y=270)

                    def genBill():
                        bill = tk.Toplevel(recep)
                        bill.geometry('200x350')
                        bill.title("Billing")
                        blabel = tk.Label(bill, text="Bill No:", font=("Arial", 9), fg="Red")
                        blabel.place(x=30, y=75)
                        btext = tk.Entry(bill, width=10)
                        btext.place(x=100, y=75)
                        pilabel = tk.Label(bill, text="Patient's Id:", font=("Arial", 9), fg="Red")
                        pilabel.place(x=30, y=105)
                        pitext = tk.Entry(bill, width=10)
                        pitext.place(x=100, y=105)
                        datel = tk.Label(bill, text="Date:", font=("Arial", 9), fg="Red")
                        datel.place(x=30, y=140)
                        date = tk.Entry(bill, width=13)
                        date.place(x=70, y=140)
                        amtl = tk.Label(bill, text="Amount", font=("Arial", 9), fg="Red")
                        amtl.place(x=30, y=170)
                        amtn = tk.Entry(bill, width=10)
                        amtn.place(x=110, y=170)

                        def printt():
                            myCursor.execute(
                                "INSERT INTO transactions (BillNo, PatientID, B_date, amount) VALUES (%s, %s, %s, %s)",
                                (btext.get(), pitext.get(), date.get(), amtn.get()))

                            db.commit()

                            done_label = tk.Label(bill, text="Bill generated successfully!!", font=("Arial", 8),
                                                  fg="Black")
                            done_label.place(x=410, y=290)

                        add_btn = tk.Button(bill, text="Print", width=9, height=1, command=printt)
                        add_btn.place(x=50, y=270)

                    def view_tests():
                        test_window = tk.Toplevel(recep)
                        test_window.geometry('600x400')
                        test_window.title("View Scheduled Tests")

                        def load_tests():
                            tree.delete(*tree.get_children())  # Clear the treeview widget

                            myCursor.execute("SELECT * FROM TestSchedule")
                            appointments = myCursor.fetchall()

                            for appointment in appointments:
                                tree.insert("", tk.END, values=(
                                    appointment[0], appointment[1], appointment[2], appointment[3], appointment[4]))

                        # Create Treeview widget to display the list of appointments
                        tree = ttk.Treeview(test_window, columns=("PID", "DID", "Date", "Time", "Test"),
                                            show="headings")
                        tree.column("PID", width=30)
                        tree.column("DID", width=30)
                        tree.column("Date", width=30)
                        tree.column("Time", width=30)
                        tree.column("Test", width=30)
                        tree.heading("PID", text="PID")
                        tree.heading("DID", text="DID")
                        tree.heading("Date", text="Date")
                        tree.heading("Time", text="Time")
                        tree.heading("Test", text="Test")
                        tree.pack(fill=tk.BOTH, expand=True)
                        # Load appointments initially
                        load_tests()

                    apat = tk.Button(recep, text="Add Patient", width=12, height=2, command=add_patient)
                    apat.place(x=225, y=135)
                    epat = tk.Button(recep, text="Update Patient Details ", width=18, height=2, command=edit_patient)
                    epat.place(x=220, y=180)
                    aappt = tk.Button(recep, text="Set New appointment", width=18, height=2, command=add_appointment)
                    aappt.place(x=220, y=225)
                    bill = tk.Button(recep, text="Generate Bill", width=12, height=2, command=genBill)
                    bill.place(x=225, y=270)
                    vtest = tk.Button(recep, text="View Scheduled Tests", width=18, height=2, command=view_tests)
                    vtest.place(x=212, y=320)

                if first_char == 'D' or first_char == 'd':
                    doctor = tk.Toplevel(EmpWindow)
                    doctor.geometry('600x400')
                    doctor.title("Doctor")

                    def view_appointments(emp_id):
                        appts = tk.Toplevel(doctor)
                        appts.geometry('600x400')
                        appts.title("View Appointments")

                        def update_appointment_status():
                            selected_item = tree.selection()
                            if selected_item:
                                appointment_id = tree.item(selected_item)['values'][0]
                                print(appointment_id)
                                status = "D"  # Set the desired status (e.g., "Done")
                                # appointments_collection.update_one({'DocID': emp_id, 'PatientID': appointment_id},
                                #                                    {'$set': {'Status': status}})

                                myCursor.execute("update appointment set status = 'D' where docID=%s and patientID=%s",
                                                 (emp_id, appointment_id))

                                db.commit()

                                load_appointments()  # Refresh the appointment list

                        def load_appointments():
                            tree.delete(*tree.get_children())  # Clear the treeview widget
                            # appointments = appointments_collection.find({'DocID': emp_id})

                            myCursor.execute("select * from appointment where DocID=%s", (emp_id,))
                            # print(emp_id)
                            appointments = myCursor.fetchall()
                            # print(appointments)

                            for appointment in appointments:
                                tree.insert("", tk.END,
                                            values=(appointment[1], appointment[3], appointment[4], appointment[5]))

                        # Create Treeview widget to display the list of appointments
                        tree = ttk.Treeview(appts, columns=("ID", "Date", "Time", "Status"), show="headings")
                        tree.column("ID", width=50)
                        tree.column("Date", width=50)
                        tree.column("Time", width=50)
                        tree.column("Status", width=50)
                        tree.heading("ID", text="ID")
                        tree.heading("Date", text="Date")
                        tree.heading("Time", text="Time")
                        tree.heading("Status", text="Status")
                        tree.pack(fill=tk.BOTH, expand=True)

                        # Load appointments initially
                        load_appointments()

                        # Create a button to update the status of attended appointments
                        update_button = tk.Button(appts, text="Mark as Done", command=update_appointment_status)
                        update_button.pack(pady=10)

                    def schedule_tests(emp_id):
                        new_test = tk.Toplevel(doctor)
                        new_test.geometry('400x350')
                        new_test.title("Schedule Test")
                        hlabel = tk.Label(new_test, text="Enter the following details:", font=("Arial", 10), fg="Blue")
                        hlabel.place(x=25, y=30)
                        ilabel = tk.Label(new_test, text="Patient's Id:", font=("Arial", 9), fg="Red")
                        ilabel.place(x=30, y=75)
                        itext = tk.Entry(new_test, width=10)
                        itext.place(x=100, y=75)
                        dilabel = tk.Label(new_test, text="Doctor's Id:", font=("Arial", 9), fg="Red")
                        dilabel.place(x=30, y=105)
                        ditext = tk.Entry(new_test, width=10)
                        ditext.place(x=100, y=105)
                        ditext.insert(0, emp_id)
                        datel = tk.Label(new_test, text="Date:", font=("Arial", 9), fg="Red")
                        datel.place(x=30, y=140)
                        date = tk.Entry(new_test, width=13)
                        date.place(x=70, y=140)
                        timel = tk.Label(new_test, text="Time", font=("Arial", 9), fg="Red")
                        timel.place(x=30, y=170)
                        timet = tk.Entry(new_test, width=12)
                        timet.place(x=70, y=170)
                        t_typel = tk.Label(new_test, text="Test type:", font=("Arial", 9), fg="Red")
                        t_typel.place(x=30, y=200)
                        t_type = tk.Entry(new_test, width=16)
                        t_type.place(x=86, y=200)

                        def add():
                            myCursor.execute("insert into TestSchedule(PatientID,DocId,T_date,T_time,test) values(%s,"
                                             "%s,%s,%s,%s)",
                                             (itext.get(), emp_id, date.get(), timet.get(), t_type.get()))
                            print(itext.get(), emp_id, date.get(), timet.get(), t_type.get())
                            db.commit()

                            done_label = tk.Label(new_test, text="Test scheduled successfully!!", font=("Arial", 8),
                                                  fg="Black")
                            done_label.place(x=40, y=250)

                        add_btn = tk.Button(new_test, text="Schedule", width=12, height=1, command=add)
                        add_btn.place(x=50, y=270)

                    vappt = tk.Button(doctor, text="View Appointments", width=15, height=2,
                                      command=lambda: view_appointments(emp_id))
                    vappt.place(x=225, y=135)
                    vpatl = tk.Button(doctor, text="Schedule Test", width=15, height=2,
                                      command=lambda: schedule_tests(emp_id))
                    vpatl.place(x=220, y=180)

            else:
                l1 = tk.Label(EmpWindow, text="Wrong Password entered!!", fg="Red")
                l1.place(x=200, y=90)
        else:
            l1 = tk.Label(EmpWindow, text="Wrong Id entered!!", fg="Red")
            l1.place(x=200, y=90)

    btn2 = tk.Button(EmpWindow, text="Login", width=12, height=2, bg='#FFFFFF', command=login)
    btn2.place(x=200, y=300)


headlabel = tk.Label(root, text="Login as", font=("Arial", 16), fg="Black")
headlabel.place(x=250, y=50)
btn = tk.Button(root, text="Administrator", width=12, height=3, bg="#F5EFE7", command=AdminWindow)
btn.place(x=250, y=150)
btn1 = tk.Button(root, text="Employee", width=12, height=3, bg="#F5EFE7", command=EmpWindow)
btn1.place(x=250, y=250)
root.mainloop()
