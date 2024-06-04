from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class attendance:
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

        
        self.var_studentID=StringVar()
        self.var_studentName=StringVar()
        self.var_section=StringVar()
        self.var_rollno=StringVar()
        self.var_dept=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendance=StringVar()
       



         # =========================== Bg Image ==========================

        bg_img = Image.open(r'Images\GettyImages-1138740533-1.jpg')
        bg_img = bg_img.resize((1500, 750), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_img)
        my_label = Label(self.root, image=self.bg_photo)
        my_label.image=self.bg_photo
        my_label.place(x=0, y=30, width=1500, height=750)


        # ====================== Heading ==========================

        heading_label = Label(self.root,
                          text="ATTENDANCE MANAGEMENT SYSTEM",
                          width=80,
                          height=0,
                          bg='white',
                          fg='#041c3e',
                          font=('TIMES NEW ROMAN',30,"bold")
                          )
        
        heading_label.place(x=-270,y=0)

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

        img_left = Image.open(r'Images\group-of-students-holding-books-and-laptop-university-or-college-students-reading-books-talking-flat-illustration-vector.jpg')
        img_left = img_left.resize((635,150), Image.LANCZOS)
        self.photo_img_left = ImageTk.PhotoImage(img_left)
        left_lb = Label(Left_frame, image=self.photo_img_left,bd=2)
        left_lb.image=self.photo_img_left
        left_lb.place(x=0, y=0, width=635, height=150)
       
       # ====================== Student Information ==================

        Student_frame=LabelFrame(Left_frame,
                                 bd=2,
                                 relief="ridge",
                                 text="Student Information",
                                 fg='#041c3e',
                                 bg='white',
                                 font=('Microsoft YaHei',10,"bold")
                                 )
        
        Student_frame.place(x=5,y=130,width=625,height=470)

         # ====================== StudentID ========================

        StudentID_label=Label(Student_frame,
                             text="StudentID :",
                             fg='#041c3e',
                             bg='white',
                             font=('Microsoft YaHei',10,"bold")
                             )
        
        StudentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        StudentID_entry=ttk.Entry(Student_frame,
                                  textvariable=self.var_studentID,
                                  width=20, 
                                  font=('Microsoft YaHei',10,"bold")
                                  )
        
        StudentID_entry.config(foreground='#041c3e') 
        StudentID_entry.grid(row=0,column=1,padx=1,pady=10,sticky=W)

        # ====================== StudentName ========================

        StudentName_label=Label(Student_frame,
                             text="Student Name :",
                             fg='#041c3e',
                             bg='white',
                             font=('Microsoft YaHei',10,"bold")
                             )
        
        StudentName_label.grid(row=0,column=3,padx=20,pady=5,sticky=W)

        StudentName_entry=ttk.Entry(Student_frame,
                                    textvariable=self.var_studentName,
                                  width=20, 
                                  font=('Microsoft YaHei',10,"bold")
                                  )
        
        StudentName_entry.config(foreground='#041c3e') 
        StudentName_entry.grid(row=0,column=4,padx=2,pady=10,sticky=W)


         # ====================== Section ========================

        Section_label=Label(Student_frame,
                             text="Section :",
                             fg='#041c3e',
                             bg='white',
                             font=('Microsoft YaHei',10,"bold")
                             )
        
        Section_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Section_combo=ttk.Combobox(Student_frame,
                                textvariable=self.var_section,
                                font=('Microsoft YaHei',10,"bold"),
                                state="readonly",
                                width=18
                                )
        
        Section_combo.config(foreground='#041c3e') 
        Section_combo["values"]=("-- Select --","A","B")
        Section_combo.current(0)
        Section_combo.grid(row=1,column=1,padx=1,pady=10,sticky=W)

        # ====================== RollNo ========================

        RollNo_label=Label(Student_frame,
                             text="Roll No :",
                             fg='#041c3e',
                             bg='white',
                             font=('Microsoft YaHei',10,"bold")
                             )
        
        RollNo_label.grid(row=1,column=3,padx=20,pady=5,sticky=W)

        RollNo_entry=ttk.Entry(Student_frame,
                               textvariable=self.var_rollno,
                                  width=20, 
                                  font=('Microsoft YaHei',10,"bold")
                                  )
        
        RollNo_entry.config(foreground='#041c3e') 
        RollNo_entry.grid(row=1,column=4,padx=2,pady=10,sticky=W)


        # ====================== Department ============================

        dept_label=Label(Student_frame,
                         text="Department :",
                         fg='#041c3e',
                         bg='white',
                         font=('Microsoft YaHei',10,"bold")
                         )
        
        dept_label.grid(row=2,column=0,padx=10,sticky=W)

        dept_combo=ttk.Combobox(Student_frame,
                                textvariable=self.var_dept,
                                font=('Microsoft YaHei',10,"bold"),
                                state="readonly",
                                width=18
                                )
        
        dept_combo.config(foreground='#041c3e') 
        dept_combo["values"]=("-- Select --","CS","CS/AI-ML","IT","ME","EC","EN")
        dept_combo.current(0)
        dept_combo.grid(row=2,column=1,padx=1,pady=10,sticky=W)

         
        

        # ====================== TIME ========================

        time_label=Label(Student_frame,
                             text="Time :",
                             fg='#041c3e',
                             bg='white',
                             font=('Microsoft YaHei',10,"bold")
                             )
        
        time_label.grid(row=2,column=3,padx=20,pady=5,sticky=W)

        time_entry=ttk.Entry(Student_frame,
                                  textvariable=self.var_time,
                                  width=20, 
                                  font=('Microsoft YaHei',10,"bold")
                                  )
        
        time_entry.config(foreground='#041c3e') 
        time_entry.grid(row=2,column=4,padx=2,pady=10,sticky=W)

        # ====================== Date ========================

        date_label=Label(Student_frame,
                             text="Date :",
                             fg='#041c3e',
                             bg='white',
                             font=('Microsoft YaHei',10,"bold")
                             )
        
        date_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(Student_frame,
                                    textvariable=self.var_date,
                                  width=20, 
                                  font=('Microsoft YaHei',10,"bold")
                                  )
        
        date_entry.config(foreground='#041c3e') 
        date_entry.grid(row=3,column=1,padx=1,pady=10,sticky=W)


        # ========================= Attendance Status ===============================

        attendance_label=Label(Student_frame,
                           text="Attendance Status : ",
                           fg='#041c3e',
                           bg='white',
                           font=('Microsoft YaHei',10,"bold")
                           )
        attendance_label.grid(row=3,column=3,padx=12,pady=5,sticky=W)

        attendance_combo=ttk.Combobox(Student_frame,
                                  textvariable=self.var_attendance,
                                  font=('Microsoft YaHei',10,"bold"),
                                  state="readonly",
                                  width=18
                                  )
        
        attendance_combo.config(foreground='#041c3e') 
        attendance_combo["values"]=("-- Select --","Present","Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=3,column=4,padx=2,pady=20,sticky=W)


          # =====================  Button Frame ================

        btn_frame=Frame(Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=370,width=617,height=70)

        # =====================  Update Button =================

        Update_btn=Button(btn_frame,
                        text="Update",
                        bg='#041c3e',
                        fg='#F5F5DC',
                        cursor="hand2",
                        font=('Microsoft YaHei',10,'bold'),
                        width=37,
                        command=self.update_csv
                        )
        
        Update_btn.grid(row=0,column=0)

        # =====================  Reset Button ===================

        Reset_btn=Button(btn_frame,
                        text="Reset",
                        bg='#041c3e',
                        fg='#F5F5DC',
                        cursor="hand2",
                        font=('Microsoft YaHei',10,'bold'),
                        width=37,
                        command=self.reset_data
                        )
        
        Reset_btn.grid(row=0,column=1)

         # =====================  Import csv Button =================

        Import_btn=Button(btn_frame,
                        text="Import csv",
                        bg='#041c3e',
                        fg='#F5F5DC',
                        cursor="hand2",
                        font=('Microsoft YaHei',10,'bold'),
                        width=37,
                        command=self.importCsv
                        )
        
        Import_btn.grid(row=1,column=0)

        # =====================  Export csv Button ===================

        Export_btn=Button(btn_frame,
                        text="Export csv",
                        bg='#041c3e',
                        fg='#F5F5DC',
                        cursor="hand2",
                        font=('Microsoft YaHei',10,'bold'),
                        width=37,
                        command=self.ExportCsv
                        )
        
        Export_btn.grid(row=1,column=1)






         # ====================== Right Frame ========================
         
        Right_frame=LabelFrame(main_frame,
                               bd=2,
                               relief="ridge",
                               text="Attendance Details",
                               fg='#041c3e',
                               bg='white',
                               font=('Microsoft YaHei',10,"bold")
                               )
        
        Right_frame.place(x=660,y=10,width=665,height=630)


        # ================================================ Right Image =========================================

        img_right = Image.open(r'Images\imageedit_4_9080682063.jpg')
        img_right = img_right.resize((660,150), Image.LANCZOS)
        self.photo_img_right = ImageTk.PhotoImage(img_right)
        right_lb = Label(Right_frame, image=self.photo_img_right,bd=2)
        right_lb.image=self.photo_img_right
        right_lb.place(x=0, y=0, width=660, height=150)

        # =========================== Table Frame =====================

        Table_frame=LabelFrame(Right_frame,
                                 bd=2,
                                 relief="ridge",
                                 fg='#041c3e',
                                 bg='white',
                                 font=('Microsoft YaHei',10,"bold")
                                 )
        
        Table_frame.place(x=5,y=140,width=652,height=460)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)


        self.Student_table=ttk.Treeview(Table_frame,
                                  column=( "ID",
                                           "Name",
                                           "sec",
                                           "rollno",
                                           "dept",
                                           "Time",
                                           "Date",
                                           "Attendance Status"

                                           
                                           ))
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        
        self.Student_table.heading("ID",text="StudentID")
        self.Student_table.heading("Name",text="Student Name")
        self.Student_table.heading("sec",text="Section")
        self.Student_table.heading("rollno",text="Roll No")
        self.Student_table.heading("dept",text="Department")
        self.Student_table.heading("Time",text="Time")
        self.Student_table.heading("Date",text="Date")
        self.Student_table.heading("Attendance Status",text="Attendance Status")
        self.Student_table["show"]="headings"


       
        self.Student_table.column("ID",width=80)
        self.Student_table.column("Name",width=180)
        self.Student_table.column("sec",width=80)
        self.Student_table.column("rollno",width=100)
        self.Student_table.column("dept",width=100)
        self.Student_table.column("Time",width=100)
        self.Student_table.column("Date",width=80)
        self.Student_table.column("Attendance Status",width=120)

        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease>",self.get_cursor)

      # =============================== fetch data =====================================

    def fetchdata(self,rows):
        self.Student_table.delete(*self.Student_table.get_children())
        for i in rows:
            self.Student_table.insert("",END,values=i)

    # ========================================== Import csv =========================================

    def importCsv(self): 
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),(" All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")   
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)    

    # ========================================== Export csv =================================================

    def ExportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found",parent=self.root)
                return False
            
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),(" All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Success","Your Data Exported to "+os.path.basename(fln)+" Successfully !!",parent=self.root)
        except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)

    # ========================================= fuction ===================================================

    def get_cursor(self,event=""):
        cursor_row=self.Student_table.focus()
        content=self.Student_table.item(cursor_row)
        rows=content['values']
        self.var_studentID.set(rows[0])
        self.var_studentName.set(rows[1])
        self.var_section.set(rows[2])
        self.var_rollno.set(rows[3])
        self.var_dept.set(rows[4])
        self.var_time.set(rows[5])
        self.var_date.set(rows[6])
        self.var_attendance.set(rows[7])
    
    # ================================ Reset data ===================================================
    
    def reset_data(self):
        self.var_studentID.set("")
        self.var_studentName.set("")
        self.var_section.set("-- Select --")
        self.var_rollno.set("")
        self.var_dept.set("-- Select --")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("-- Select --")

    # ================================= Update data ==================================================

    def update_data(self):
        self.var_studentID.get()
        self.var_studentName.get()
        self.var_section.get()
        self.var_rollno.get()
        self.var_dept.get()
        self.var_time.get()
        self.var_date.get()
        self.var_attendance.get()

    # ============================== update csv file ====================================================
    def update_csv(self):
         try:
            # Read CSV data into a list of lists
            with open('attendance.csv', 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                csv_data = list(reader)

            print(len(csv_data))
            print(csv_data)

            # Validate row and column numbers
            # if 2 >= len(csv_data) or 7 >= len(csv_data[0]):
            #     raise IndexError("Invalid row or column number!")

            # Update the specified value
            csv_data[0][7] = self.var_attendance.get()

            # Write updated data back to the CSV file
            with open('attendance.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(csv_data)
                self.fetchdata(csv_data)
            
            # Display success message
            messagebox.showinfo("Success","Your Data is Updated Successfully !!",parent=self.root)
         except Exception as e:
              
              # Display error message
              messagebox.showerror("Error",f"Due To : {str(e)}",parent=self.root)







if __name__ == "__main__":
    root = ctk.CTk()
    obj = attendance(root)
    root.mainloop()

