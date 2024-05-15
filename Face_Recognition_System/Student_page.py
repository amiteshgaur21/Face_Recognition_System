from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image, ImageTk
import mysql.connector
import cv2


class student:
    def __init__(self, root):
        self.root = root
        # ======================== Window Size ======================
        
        h = 790
        w = 1385
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 4) - (h// 4)
        self.root.geometry('{}x{}+{}+{}'.format(w, h, x, y))

        self.root.resizable(False,False)
        ctk.set_appearance_mode("dark")

        # ======================= Title of window ======================

        self.root.title(" Student Management System ")


        # =========================== variables =========================

        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_studentID=StringVar()
        self.var_studentName=StringVar()
        self.var_section=StringVar()
        self.var_rollno=StringVar()
        self.var_gender=StringVar()
        self.var_DOB=StringVar()
        self.var_email=StringVar()
        self.var_mobile=StringVar()
        self.var_address=StringVar()
        self.var_faculty=StringVar()
       

        
        # =========================== Bg Image ==========================

        bg_img = Image.open(r'Face_Recognition_System\Images\GettyImages-1138740533-1.jpg')
        bg_img = bg_img.resize((1500, 750), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_img)
        my_label = Label(self.root, image=self.bg_photo)
        my_label.image=self.bg_photo
        my_label.place(x=0, y=30, width=1500, height=750)


        # ====================== Heading ==========================

        heading_label = Label(self.root,
                          text="STUDENT MANAGEMENT SYSTEM",
                          width=80,
                          height=0,
                          bg='white',
                          fg='#041c3e',
                          font=('Microsoft YaHei',30,"bold")
                          )
        
        heading_label.place(x=-350,y=0)

        # ======================= Main Frame ======================

        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=15,y=70,width=1340,height=660)

        # ====================== Left Frame ========================
         
        Left_frame=LabelFrame(main_frame,
                              bd=2,
                              relief="ridge",
                              text="Student Details",
                              fg='#041c3e',
                              bg='white',
                              font=('Microsoft YaHei',10,"bold")
                              )
        
        Left_frame.place(x=10,y=10,width=640,height=630)

        # ====================== Left Frame Image ===================

        img_left = Image.open(r'Face_Recognition_System\Images\group-of-students-holding-books-and-laptop-university-or-college-students-reading-books-talking-flat-illustration-vector.jpg')
        img_left = img_left.resize((635,150), Image.LANCZOS)
        self.photo_img_left = ImageTk.PhotoImage(img_left)
        left_lb = Label(Left_frame, image=self.photo_img_left,bd=2)
        left_lb.image=self.photo_img_left
        left_lb.place(x=0, y=0, width=635, height=150)

        # ====================== Course Information ==================

        course_frame=LabelFrame(Left_frame,
                                bd=2,
                                relief="ridge",
                                text="Course Information",
                                fg='#041c3e',
                                bg='white',
                                font=('Microsoft YaHei',10,"bold")
                                )
        
        course_frame.place(x=5,y=130,width=625,height=130)

        # ====================== Department ============================

        dept_label=Label(course_frame,
                         text="Department",
                         fg='#041c3e',
                         bg='white',
                         font=('Microsoft YaHei',10,"bold")
                         )
        
        dept_label.grid(row=0,column=0,padx=20,sticky=W)

        dept_combo=ttk.Combobox(course_frame,
                                textvariable=self.var_dept,
                                font=('Microsoft YaHei',10,"bold"),
                                state="readonly",
                                width=20
                                )
        
        dept_combo.config(foreground='#041c3e') 
        dept_combo["values"]=("-- Select --","CS","CS/AI-ML","IT","ME","EC","EN")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # ========================= Course ===============================

        course_label=Label(course_frame,
                           text="Course",
                           fg='#041c3e',
                           bg='white',
                           font=('Microsoft YaHei',10,"bold")
                           )
        course_label.grid(row=0,column=3,padx=20,sticky=W)

        course_combo=ttk.Combobox(course_frame,
                                  textvariable=self.var_course,
                                  font=('Microsoft YaHei',10,"bold"),
                                  state="readonly",
                                  width=20
                                  )
        
        course_combo.config(foreground='#041c3e') 
        course_combo["values"]=("-- Select --","B.Tech","BCA","BBA","M.Tech","MCA","MBA")
        course_combo.current(0)
        course_combo.grid(row=0,column=4,padx=2,pady=10,sticky=W)

         # ========================= Year ===============================

        Year_label=Label(course_frame,
                         text="Year",
                         fg='#041c3e',
                         bg='white',
                         font=('Microsoft YaHei',10,"bold")
                         )
        
        Year_label.grid(row=1,column=0,padx=20,sticky=W)

        Year_combo=ttk.Combobox(course_frame,
                                textvariable=self.var_year,
                                font=('Microsoft YaHei',10,"bold"),
                                state="readonly",
                                width=20
                                )
        
        Year_combo.config(foreground='#041c3e') 
        Year_combo["values"]=("-- Select --","1st","2nd","3rd","4th")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=20,sticky=W)

         # ========================= Semester ===============================

        Semester_label=Label(course_frame,
                             text="Semester",
                             fg='#041c3e',
                             bg='white',
                             font=('Microsoft YaHei',10,"bold")
                             )
        
        Semester_label.grid(row=1,column=3,padx=20,sticky=W)

        Semester_combo=ttk.Combobox(course_frame,
                                    textvariable=self.var_semester,
                                    font=('Microsoft YaHei',10,"bold"),
                                    state="readonly",
                                    width=20
                                    )
        
        Semester_combo.config(foreground='#041c3e') 
        Semester_combo["values"]=("-- Select --","1st","2nd","3rd","4th","5th","6th","7th","8th")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=4,padx=2,pady=10,sticky=W)

        # ====================== Student Information ==================

        Student_frame=LabelFrame(Left_frame,
                                 bd=2,
                                 relief="ridge",
                                 text="Student Information",
                                 fg='#041c3e',
                                 bg='white',
                                 font=('Microsoft YaHei',10,"bold")
                                 )
        
        Student_frame.place(x=5,y=260,width=625,height=340)

         # ====================== StudentID ========================

        StudentID_label=Label(Student_frame,
                             text="StudentID :",
                             fg='#041c3e',
                             bg='white',
                             font=('Microsoft YaHei',10,"bold")
                             )
        
        StudentID_label.grid(row=0,column=0,padx=20,sticky=W)

        StudentID_entry=ttk.Entry(Student_frame,
                                  textvariable=self.var_studentID,
                                  width=20, 
                                  font=('Microsoft YaHei',10,"bold")
                                  )
        
        StudentID_entry.config(foreground='#041c3e') 
        StudentID_entry.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        # ====================== StudentName ========================

        StudentName_label=Label(Student_frame,
                             text="Student Name :",
                             fg='#041c3e',
                             bg='white',
                             font=('Microsoft YaHei',10,"bold")
                             )
        
        StudentName_label.grid(row=0,column=3,padx=10,sticky=W)

        StudentName_entry=ttk.Entry(Student_frame,
                                    textvariable=self.var_studentName,
                                  width=20, 
                                  font=('Microsoft YaHei',10,"bold")
                                  )
        
        StudentName_entry.config(foreground='#041c3e') 
        StudentName_entry.grid(row=0,column=4,padx=2,pady=5,sticky=W)


         # ====================== Section ========================

        Section_label=Label(Student_frame,
                             text="Section :",
                             fg='#041c3e',
                             bg='white',
                             font=('Microsoft YaHei',10,"bold")
                             )
        
        Section_label.grid(row=1,column=0,padx=20,sticky=W)

        Section_combo=ttk.Combobox(Student_frame,
                                textvariable=self.var_section,
                                font=('Microsoft YaHei',10,"bold"),
                                state="readonly",
                                width=18
                                )
        
        Section_combo.config(foreground='#041c3e') 
        Section_combo["values"]=("-- Select --","A","B")
        Section_combo.current(0)
        Section_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        # ====================== RollNo ========================

        RollNo_label=Label(Student_frame,
                             text="Roll No :",
                             fg='#041c3e',
                             bg='white',
                             font=('Microsoft YaHei',10,"bold")
                             )
        
        RollNo_label.grid(row=1,column=3,padx=10,sticky=W)

        RollNo_entry=ttk.Entry(Student_frame,
                               textvariable=self.var_rollno,
                                  width=20, 
                                  font=('Microsoft YaHei',10,"bold")
                                  )
        
        RollNo_entry.config(foreground='#041c3e') 
        RollNo_entry.grid(row=1,column=4,padx=2,pady=5,sticky=W)

         # ====================== Gender ========================

        Gender_label=Label(Student_frame,
                             text="Gender :",
                             fg='#041c3e',
                             bg='white',
                             font=('Microsoft YaHei',10,"bold")
                             )
        
        Gender_label.grid(row=2,column=0,padx=20,sticky=W)

        
        Gender_combo=ttk.Combobox(Student_frame,
                                textvariable=self.var_gender,
                                font=('Microsoft YaHei',10,"bold"),
                                state="readonly",
                                width=18
                                )
        
        Gender_combo.config(foreground='#041c3e') 
        Gender_combo["values"]=("-- Select --","Male","Female")
        Gender_combo.current(0)
        Gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)

        # ====================== DOB ========================

        DOB_label=Label(Student_frame,
                             text="DOB :",
                             fg='#041c3e',
                             bg='white',
                             font=('Microsoft YaHei',10,"bold")
                             )
        
        DOB_label.grid(row=2,column=3,padx=10,sticky=W)

        DOB_entry=ttk.Entry(Student_frame,
                            textvariable=self.var_DOB,
                                  width=20, 
                                  font=('Microsoft YaHei',10,"bold")
                                  )
        
        DOB_entry.config(foreground='#041c3e') 
        DOB_entry.grid(row=2,column=4,padx=2,pady=5,sticky=W)

         # ====================== Email========================

        Email_label=Label(Student_frame,
                             text="Email :",
                             fg='#041c3e',
                             bg='white',
                             font=('Microsoft YaHei',10,"bold")
                             )
        
        Email_label.grid(row=3,column=0,padx=20,pady=5,sticky=W)

        Email_entry=ttk.Entry(Student_frame,
                              textvariable=self.var_email,
                                  width=20, 
                                  font=('Microsoft YaHei',10,"bold")
                                  )
        
        Email_entry.config(foreground='#041c3e') 
        Email_entry.grid(row=3,column=1,padx=2,pady=5,sticky=W)

        # ====================== Mobile ========================

        Mobile_label=Label(Student_frame,
                             text="Mobile :",
                             fg='#041c3e',
                             bg='white',
                             font=('Microsoft YaHei',10,"bold")
                             )
        
        Mobile_label.grid(row=3,column=3,padx=10,sticky=W)

        Mobile_entry=ttk.Entry(Student_frame,
                               textvariable=self.var_mobile,
                                  width=20, 
                                  font=('Microsoft YaHei',10,"bold")
                                  )
        
        Mobile_entry.config(foreground='#041c3e') 
        Mobile_entry.grid(row=3,column=4,padx=2,pady=5,sticky=W) 

         # ====================== Address ========================

        Address_label=Label(Student_frame,
                             text="Address :",
                             fg='#041c3e',
                             bg='white',
                             font=('Microsoft YaHei',10,"bold")
                             )
        
        Address_label.grid(row=4,column=0,padx=20,sticky=W)

        Address_entry=ttk.Entry(Student_frame,
                                textvariable=self.var_address,
                                  width=20, 
                                  font=('Microsoft YaHei',10,"bold")
                                  )
        
        Address_entry.config(foreground='#041c3e') 
        Address_entry.grid(row=4,column=1,padx=2,pady=5,sticky=W)

        # ====================== Faculty Name ========================

        FacultyName_label=Label(Student_frame,
                             text="Faculty Name :",
                             fg='#041c3e',
                             bg='white',
                             font=('Microsoft YaHei',10,"bold")
                             )
        
        FacultyName_label.grid(row=4,column=3,padx=10,sticky=W)

        FacultyName_entry=ttk.Entry(Student_frame,
                                    textvariable=self.var_faculty,
                                  width=20, 
                                  font=('Microsoft YaHei',10,"bold")
                                  )
        
        FacultyName_entry.config(foreground='#041c3e') 
        FacultyName_entry.grid(row=4,column=4,padx=2,pady=5,sticky=W)


        # ========================== Radio Button =====================

        s = ttk.Style()

        s.configure('Wild.TRadiobutton',  
        background="white",         
        foreground='#041c3e',
        font=('Microsoft YaHei',10,"bold")
        )

        self.var_radio=StringVar()
        radiobtn1=ttk.Radiobutton(Student_frame,
                                  variable=self.var_radio,
                                  text="Take Photo Sample",
                                  value="Yes",
                                  style='Wild.TRadiobutton',
                                  cursor="hand2"
                                  )
        
        radiobtn1.place(x=20,y=185)
        
        
        radiobtn2=ttk.Radiobutton(Student_frame,
                                  variable=self.var_radio,
                                  text="No Photo Sample",
                                  value="No",
                                  style='Wild.TRadiobutton',
                                  cursor="hand2"
                                  )
        
        radiobtn2.place(x=300,y=185)

        # =====================  Button Frame ================

        btn_frame=Frame(Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=215,width=617,height=100)

        # =====================  Save Button ====================

        Save_btn=Button(btn_frame,
                        command=self.add_data,
                        text="Save",
                        bg='#041c3e',
                        fg='#F5F5DC',
                        cursor="hand2",
                        font=('Microsoft YaHei',10,'bold'),
                        width=37
                        )
        
        Save_btn.grid(row=0,column=0)

        # =====================  Update Button =================

        Update_btn=Button(btn_frame,
                        text="Update",
                        bg='#041c3e',
                        fg='#F5F5DC',
                        cursor="hand2",
                        font=('Microsoft YaHei',10,'bold'),
                        width=37,
                        command=self.Update_data
                        )
        
        Update_btn.grid(row=0,column=1)

        # =====================  Delete Button ==================

        Delete_btn=Button(btn_frame,
                        text="Delete",
                        bg='#041c3e',
                        fg='#F5F5DC',
                        cursor="hand2",
                        font=('Microsoft YaHei',10,'bold'),
                        width=37,
                        command=self.Delete_data
                        )
        
        Delete_btn.grid(row=1,column=0)

        # =====================  Reset Button ===================

        Reset_btn=Button(btn_frame,
                        text="Reset",
                        bg='#041c3e',
                        fg='#F5F5DC',
                        cursor="hand2",
                        font=('Microsoft YaHei',10,'bold'),
                        width=37,
                        command=self.Reset_data
                        )
        
        Reset_btn.grid(row=1,column=1)

        # =====================  Take photo Button ================

        take_photo_btn=Button(btn_frame,
                        text="Take Photo Sample",
                        bg='#041c3e',
                        fg='#F5F5DC',
                        cursor="hand2",
                        font=('Microsoft YaHei',10,'bold'),
                        width=37,
                        command=self.generate_dataset
                        )
        
        take_photo_btn.grid(row=2,column=0)

        # =====================  Update Photo Button ====================

        No_photo_btn=Button(btn_frame,
                        text="Update Photo Sample",
                        bg='#041c3e',
                        fg='#F5F5DC',
                        cursor="hand2",
                        font=('Microsoft YaHei',10,'bold'),
                        width=37
                        )
        
        No_photo_btn.grid(row=2,column=1)


        # ====================== Right Frame ========================
         
        Right_frame=LabelFrame(main_frame,
                               bd=2,
                               relief="ridge",
                               text="Student Data",
                               fg='#041c3e',
                               bg='white',
                               font=('Microsoft YaHei',10,"bold")
                               )
        
        Right_frame.place(x=660,y=10,width=665,height=630)

        # ========================= Right Image ======================

        img_right = Image.open(r'Face_Recognition_System\Images\imageedit_4_9080682063.jpg')
        img_right = img_right.resize((660,150), Image.LANCZOS)
        self.photo_img_right = ImageTk.PhotoImage(img_right)
        right_lb = Label(Right_frame, image=self.photo_img_right,bd=2)
        right_lb.image=self.photo_img_right
        right_lb.place(x=0, y=0, width=660, height=150)

        # ====================== Search Frame ==================

        Search_frame=LabelFrame(Right_frame,
                                 bd=2,
                                 relief="ridge",
                                 text="Search System",
                                 fg='#041c3e',
                                 bg='white',
                                 font=('Microsoft YaHei',10,"bold")
                                 )
        
        Search_frame.place(x=5,y=130,width=652,height=60)

        Search_label=Label(Search_frame,
                             text="Search By :",
                             fg='#041c3e',
                             bg='white',
                             font=('Microsoft YaHei',10,"bold")
                             )
        
        Search_label.grid(row=0,column=0,padx=10,sticky=W)

        Search_combo=ttk.Combobox(Search_frame,
                                font=('Microsoft YaHei',10,"bold"),
                                state="readonly",
                                width=20
                                )
        
        Search_combo.config(foreground='#041c3e') 
        Search_combo["values"]=("-- Select --","CS","CS/AI-ML","IT","ME","EC","EN")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,sticky=W)


        Search_entry=ttk.Entry(Search_frame,
                                  width=20, 
                                  font=('Microsoft YaHei',10,"bold")
                                  )
        
        Search_entry.config(foreground='#041c3e') 
        Search_entry.grid(row=0,column=2,padx=2,pady=5,sticky=W)

        # ======================= Search Button =====================
        
        Search_btn=Button(Search_frame,
                        text="Search",
                        bg='#041c3e',
                        fg='#F5F5DC',
                        cursor="hand2",
                        font=('Microsoft YaHei',10,'bold'),
                        width=10
                        )
        
        Search_btn.grid(row=0,column=3,padx=5)

        # ======================== Show Button ========================

        Show_btn=Button(Search_frame,
                        text="Show All",
                        bg='#041c3e',
                        fg='#F5F5DC',
                        cursor="hand2",
                        font=('Microsoft YaHei',10,'bold'),
                        width=10
                        )
        
        Show_btn.grid(row=0,column=4)

        # =========================== Table Frame =====================

        Table_frame=LabelFrame(Right_frame,
                                 bd=2,
                                 relief="ridge",
                                 fg='#041c3e',
                                 bg='white',
                                 font=('Microsoft YaHei',10,"bold")
                                 )
        
        Table_frame.place(x=5,y=195,width=652,height=410)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.Student_table=ttk.Treeview(Table_frame,
                                  column=("dept",
                                           "course",
                                           "year",
                                           "sem",
                                           "ID",
                                           "Name",
                                           "sec",
                                           "rollno",
                                           "Gender",
                                           "DOB",
                                           "Email",
                                           "Mobile",
                                           "Address",
                                           "Facutly",
                                           "photo"
                                           ))
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("dept",text="Department")
        self.Student_table.heading("course",text="Course")
        self.Student_table.heading("year",text="Year")
        self.Student_table.heading("sem",text="Semester")
        self.Student_table.heading("ID",text="StudentID")
        self.Student_table.heading("Name",text="Student Name")
        self.Student_table.heading("sec",text="Section")
        self.Student_table.heading("rollno",text="Roll No")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("DOB",text="DOB")
        self.Student_table.heading("Email",text="Email")
        self.Student_table.heading("Mobile",text="Mobile")
        self.Student_table.heading("Address",text="Address")
        self.Student_table.heading("Facutly",text="Facutly Name")
        self.Student_table.heading("photo",text="Photo Status")
        self.Student_table["show"]="headings"


        self.Student_table.column("dept",width=80)
        self.Student_table.column("course",width=80)
        self.Student_table.column("year",width=80)
        self.Student_table.column("sem",width=80)
        self.Student_table.column("ID",width=80)
        self.Student_table.column("Name",width=180)
        self.Student_table.column("sec",width=80)
        self.Student_table.column("rollno",width=100)
        self.Student_table.column("Gender",width=80)
        self.Student_table.column("DOB",width=80)
        self.Student_table.column("Email",width=120)
        self.Student_table.column("Mobile",width=80)
        self.Student_table.column("Address",width=80)
        self.Student_table.column("Facutly",width=100)
        self.Student_table.column("photo",width=80)

        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        # ================================ Function =============================

    def add_data(self) :
        if self.var_dept.get() == "-- Select --" :
            messagebox.showerror("Error","Select the Department")
        elif self.var_course.get() == "-- Select --" :
            messagebox.showerror("Error","Select the Course")
        elif self.var_year.get() == "-- Select --" :
            messagebox.showerror("Error","Select the Year")
        elif self.var_semester.get() == "-- Select --" :
            messagebox.showerror("Error","Select the semester")
        elif (self.var_studentID.get() == "" 
              or self.var_studentName.get() == "" 
              or self.var_section.get() == ""  
              or self.var_rollno.get() == ""
              or self.var_gender.get() == ""
              or self.var_DOB.get() == ""
              or self.var_email.get() == ""
              or self.var_mobile.get() == ""
              or self.var_address.get() == ""
              or self.var_faculty.get() == ""):
            messagebox.showerror("Error"," All Fields are Required")
        else :
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sHj@6378#jw",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dept.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_studentID.get(),
                                                                                                            self.var_studentName.get(),
                                                                                                            self.var_section.get(),
                                                                                                            self.var_rollno.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_DOB.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_mobile.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_faculty.get(),
                                                                                                            self.var_radio.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success"," Student Details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)
    

    # ======================= fetch data =======================================
    def fetch_data(self) :
        conn=mysql.connector.connect(host="localhost",username="root",password="sHj@6378#jw",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0 :
            self.Student_table.delete(*self.Student_table.get_children())
            for i in data :
                self.Student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # =============================== Get cursor ====================================

    def get_cursor(self,event=""):
        cursor_focus=self.Student_table.focus()
        content=self.Student_table.item(cursor_focus)
        data =content["values"]

        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_studentID.set(data[4]),
        self.var_studentName.set(data[5]),
        self.var_section.set(data[6]),
        self.var_rollno.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_DOB.set(data[9]),
        self.var_email.set(data[10]),
        self.var_mobile.set(data[11]),
        self.var_address.set(data[12]),
        self.var_faculty.set(data[13]),
        self.var_radio.set(data[14])
    
    # ==================================== Update data =====================================

    def Update_data(self) :
        if self.var_dept.get() == "-- Select --" :
            messagebox.showerror("Error","Select the Department")
        elif self.var_course.get() == "-- Select --" :
            messagebox.showerror("Error","Select the Course")
        elif self.var_year.get() == "-- Select --" :
            messagebox.showerror("Error","Select the Year")
        elif self.var_semester.get() == "-- Select --" :
            messagebox.showerror("Error","Select the semester")
        elif (self.var_studentID.get() == "" 
              or self.var_studentName.get() == "" 
              or self.var_section.get() == ""  
              or self.var_rollno.get() == ""
              or self.var_gender.get() == ""
              or self.var_DOB.get() == ""
              or self.var_email.get() == ""
              or self.var_mobile.get() == ""
              or self.var_address.get() == ""
              or self.var_faculty.get() == ""):
            messagebox.showerror("Error"," All Fields are Required")
        else :
            try:
                Update=messagebox.askyesno("Update","Do you want to update this Student Details",parent=self.root)
                if Update>0:
                 conn=mysql.connector.connect(host="localhost",username="root",password="sHj@6378#jw",database="face_recognition")
                 my_cursor=conn.cursor()
                 my_cursor.execute("update student set dept=%s,course=%s,year=%s,semester=%s,studentName=%s,section=%s,rollno=%s,gender=%s,DOB=%s,email=%s,mobile=%s,address=%s,facultyName=%s,PhotoSample=%s where studentID=%s",(

                                                                                                                                                                                                                   self.var_dept.get(),
                                                                                                                                                                                                                   self.var_course.get(),
                                                                                                                                                                                                                   self.var_year.get(),
                                                                                                                                                                                                                   self.var_semester.get(),
                                                                                                                                                                                                                   self.var_studentName.get(),
                                                                                                                                                                                                                   self.var_section.get(),
                                                                                                                                                                                                                   self.var_rollno.get(),
                                                                                                                                                                                                                   self.var_gender.get(),
                                                                                                                                                                                                                   self.var_DOB.get(),
                                                                                                                                                                                                                   self.var_email.get(),
                                                                                                                                                                                                                   self.var_mobile.get(),
                                                                                                                                                                                                                   self.var_address.get(),
                                                                                                                                                                                                                   self.var_faculty.get(),
                                                                                                                                                                                                                   self.var_radio.get(),
                                                                                                                                                                                                                   self.var_studentID.get()
                                                                                                                                                                                                                   ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details Successfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)
    
    # ================================ Delete Data ==============================================

    def Delete_data(self):
        if self.var_studentID.get() =="" :
            messagebox.showerror("Error","studentID must be required",parent =self.root)
        else :
            try:
                Delete=messagebox.askyesno("Delete","Do you want to delete Student Details",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="sHj@6378#jw",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where studentID=%s"
                    val=(self.var_studentID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not Delete:
                        return
                messagebox.showinfo("Success","Student Details Successfully Deleted",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)
    

    # ================================== RESET DATA =====================================

    def Reset_data(self):
        self.var_dept.set("-- Select --"),
        self.var_course.set("-- Select --"),
        self.var_year.set("-- Select --"),
        self.var_semester.set("-- Select --"),
        self.var_studentID.set(""),
        self.var_studentName.set(""),
        self.var_section.set("-- Select --"),
        self.var_rollno.set(""),
        self.var_gender.set("-- Select --"),
        self.var_DOB.set(""),
        self.var_email.set(""),
        self.var_mobile.set(""),
        self.var_address.set(""),
        self.var_faculty.set(""),
        self.var_radio.set("")

    # =================================== GENERATE DATASET OR TAKE PHOTO SAMPLE ==============================
    def generate_dataset(self):
        if self.var_dept.get() == "-- Select --" :
            messagebox.showerror("Error","Select the Department")
        elif self.var_course.get() == "-- Select --" :
            messagebox.showerror("Error","Select the Course")
        elif self.var_year.get() == "-- Select --" :
            messagebox.showerror("Error","Select the Year")
        elif self.var_semester.get() == "-- Select --" :
            messagebox.showerror("Error","Select the semester")
        elif (self.var_studentID.get() == "" 
              or self.var_studentName.get() == "" 
              or self.var_section.get() == ""  
              or self.var_rollno.get() == ""
              or self.var_gender.get() == ""
              or self.var_DOB.get() == ""
              or self.var_email.get() == ""
              or self.var_mobile.get() == ""
              or self.var_address.get() == ""
              or self.var_faculty.get() == ""):
            messagebox.showerror("Error"," All Fields are Required")
        else :
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sHj@6378#jw",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                my_result=my_cursor.fetchall()
                id=0
                for x in my_result:
                    id+=1
                my_cursor.execute("update student set dept=%s,course=%s,year=%s,semester=%s,studentName=%s,section=%s,rollno=%s,gender=%s,DOB=%s,email=%s,mobile=%s,address=%s,facultyName=%s,PhotoSample=%s where studentID=%s",(

                                                                                                                                                                                                                   self.var_dept.get(),
                                                                                                                                                                                                                   self.var_course.get(),
                                                                                                                                                                                                                   self.var_year.get(),
                                                                                                                                                                                                                   self.var_semester.get(),
                                                                                                                                                                                                                   self.var_studentName.get(),
                                                                                                                                                                                                                   self.var_section.get(),
                                                                                                                                                                                                                   self.var_rollno.get(),
                                                                                                                                                                                                                   self.var_gender.get(),
                                                                                                                                                                                                                   self.var_DOB.get(),
                                                                                                                                                                                                                   self.var_email.get(),
                                                                                                                                                                                                                   self.var_mobile.get(),
                                                                                                                                                                                                                   self.var_address.get(),
                                                                                                                                                                                                                   self.var_faculty.get(),
                                                                                                                                                                                                                   self.var_radio.get(),
                                                                                                                                                                                                                   self.var_studentID.get()==id+1
                                                                                                                                                                                                                   ))
                 
                conn.commit()
                self.fetch_data()
                self.Reset_data()
                conn.close()

                face_classifier=cv2.CascadeClassifier(r"Face_Recognition_System\haarcascade_frontalface_default.xml")
        
                def face_scanning(img):     
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scale factor = 1.3
                    #minimum neighbour=5

                    for (x,y,w,h) in faces:
                        face_scanning=img[y:y+h,x:x+w]
                        return face_scanning
            

                cap=cv2.VideoCapture(0)
                img_id=0

                while True:
                     ret,face_frame=cap.read()
                     if face_scanning(face_frame) is not None:
                       img_id+=1
                       my_face=cv2.resize(face_scanning(face_frame),(450,450))
                       my_face=cv2.cvtColor(my_face,cv2.COLOR_BGR2GRAY)
                       file_path="Face_Recognition_System/data/user."+str(id)+"."+str(img_id)+".jpg"

                       cv2.imwrite(file_path,my_face)
                       cv2.putText(my_face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                       cv2.imshow("face scanning",my_face)

                     if cv2.waitKey(1)==13 or int(img_id)==200:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Face Scanning Compeleted Successfully")

            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)
    






if __name__ == "__main__":
    root = ctk.CTk()
    obj = student(root)
    root.mainloop()
