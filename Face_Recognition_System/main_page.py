from tkinter import *
import tkinter as ttk
from tkinter import messagebox
import customtkinter as ctk
from Student_page import student
from train_data import dataset
from face_recognition import Face_Recognition
from Attendance import attendance
from PIL import Image, ImageTk
import os



class Face_Recognition_System:
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

        self.root.title("Face Recognition System")

        
        # =========================== Bg Image ==========================

        img = Image.open('Images/digital-human-face-artificial-intelligence-ai-dispersion-dissolve-disintegration-d-render_628331-178.png')
        img = img.resize((1500, 750), Image.LANCZOS)
        self.photo_img = ImageTk.PhotoImage(img)
        first_lb = Label(self.root, image=self.photo_img)
        first_lb.place(x=0, y=30, width=1500, height=750)

        # ====================== Heading ======================

        my_label1 = Label(self.root,text="FACE RECOGNITION SYSTEM",width=80,height=0,bg='#F5F5DC',fg='#041c3e',font=('Microsoft YaHei',30,"bold"))
        my_label1.place(x=-350,y=0)

        
        # ===================== frame ==============================

        my_frame =LabelFrame(self.root,bd=2,relief="ridge",width=850,height=600,bg='#F5F5DC',highlightbackground="#041c3e",highlightthickness=1)
        my_frame.place(x=20,y=100)

        # ======================================= Student Details =============================================

        img2=Image.open('Images/college project-pana.png')
        img2=img2.resize((150,150),Image.LANCZOS)
        self.photo_img2=ImageTk.PhotoImage(img2)  


        b1=Button(my_frame,image=self.photo_img2,command=self.Student_details,cursor="hand2")
        b1.place(x=50,y=60,width=150,height=150)

        b1_1=Button(my_frame,text="Student Details",command=self.Student_details,bg='#041c3e',fg='#F5F5DC',cursor="hand2", font=('Microsoft YaHei',10,'bold'))
        b1_1.place(x=50,y=200,width=150,height=30)



        # =========================================== Face Detection =====================================

        img3=Image.open('Images/imageedit_18_9022603448.jpg')
        img3=img3.resize((150,150),Image.LANCZOS)
        self.photo_img3=ImageTk.PhotoImage(img3)

        b2=Button(my_frame,image=self.photo_img3,cursor="hand2",command=self.Face_Scan)
        b2.place(x=250,y=60,width=150,height=150)

        b2_1=Button(my_frame,text="Face Detection",bg='#041c3e',fg='#F5F5DC',cursor="hand2", font=('Microsoft YaHei',10,'bold'),command=self.Face_Scan)
        b2_1.place(x=250,y=200,width=150,height=30)



        # =============================================== Attendance ===================================

        img4=Image.open('Images/Confirmed attendance-pana.png')
        img4=img4.resize((150,150),Image.LANCZOS)
        self.photo_img4=ImageTk.PhotoImage(img4)

        b3=Button(my_frame,image=self.photo_img4,cursor="hand2",command=self.Attendance_function)
        b3.place(x=450,y=60,width=150,height=150)

        b3_1=Button(my_frame,text="Attendance",bg='#041c3e',fg='#F5F5DC',cursor="hand2", font=('Microsoft YaHei',10,'bold'),command=self.Attendance_function)
        b3_1.place(x=450,y=200,width=150,height=30)


        # ========================================== help ===========================================

        img5=Image.open('Images/imageedit_32_3622200823.jpg')
        img5=img5.resize((150,150),Image.LANCZOS)
        self.photo_img5=ImageTk.PhotoImage(img5)

        b4=Button(my_frame,image=self.photo_img5,cursor="hand2")
        b4.place(x=650,y=60,width=150,height=150)

        b4_1=Button(my_frame,text="Help",bg='#041c3e',fg='#F5F5DC',cursor="hand2", font=('Microsoft YaHei',10,'bold'))
        b4_1.place(x=650,y=200,width=150,height=30)

         # ======================================== Train Data ======================================

        img6=Image.open('Images/Data analysis-amico.png')
        img6=img6.resize((150,150),Image.LANCZOS)
        self.photo_img6=ImageTk.PhotoImage(img6)

        b5=Button(my_frame,image=self.photo_img6,cursor="hand2",command=self.Train_dataset)
        b5.place(x=50,y=350,width=150,height=150)

        b5_1=Button(my_frame,text="Train Data",bg='#041c3e',fg='#F5F5DC',cursor="hand2", font=('Microsoft YaHei',10,'bold'),command=self.Train_dataset)
        b5_1.place(x=50,y=490,width=150,height=30)     


         # ======================================== Photos =========================================

        img7=Image.open('Images/Images-rafiki.png')
        img7=img7.resize((150,150),Image.LANCZOS)
        self.photo_img7=ImageTk.PhotoImage(img7)

        b6=Button(my_frame,image=self.photo_img7,cursor="hand2",command=self.open_img)
        b6.place(x=250,y=350,width=150,height=150)

        b6_1=Button(my_frame,text="Photos",bg='#041c3e',fg='#F5F5DC',cursor="hand2", font=('Microsoft YaHei',10,'bold'),command=self.open_img)
        b6_1.place(x=250,y=490,width=150,height=30)     

         # ====================================== Developer ========================================

        img8=Image.open('Images/Video game developer-bro.png')
        img8=img8.resize((150,150),Image.LANCZOS)
        self.photo_img8=ImageTk.PhotoImage(img8)

        b7=Button(my_frame,image=self.photo_img8,cursor="hand2")
        b7.place(x=450,y=350,width=150,height=150)

        b7_1=Button(my_frame,text="Developer",bg='#041c3e',fg='#F5F5DC',cursor="hand2", font=('Microsoft YaHei',10,'bold'))
        b7_1.place(x=450,y=490,width=150,height=30)        
   
   



         # ===================================== Log Out ====================================

        img9=Image.open('Images/imageedit_25_5473229917.jpg')
        img9=img9.resize((150,150),Image.LANCZOS)
        self.photo_img9=ImageTk.PhotoImage(img9)

        b8=Button(my_frame,image=self.photo_img9,cursor="hand2",command=self.Logout_function)
        b8.place(x=650,y=350,width=150,height=150)

        b8_1=Button(my_frame,text="Log Out",bg='#041c3e',fg='#F5F5DC',cursor="hand2", font=('Microsoft YaHei',10,'bold'),command=self.Logout_function)
        b8_1.place(x=650,y=490,width=150,height=30)  

    # ================================= Function =====================================
     
    def Student_details(self):
        self.new_window=ttk.Toplevel(self.root)
        self.app=student(self.new_window) 
    
    def open_img(self):
        os.startfile("data")
    

    def Train_dataset(self):
        self.new_window=ttk.Toplevel(self.root)
        self.app=dataset(self.new_window) 

    def Face_Scan(self):
        self.new_window=ttk.Toplevel(self.root)
        self.app=Face_Recognition(self.new_window) 

    
    def Attendance_function(self):
        self.new_window=ttk.Toplevel(self.root)
        self.app=attendance(self.new_window) 

    def Logout_function(self):
        self.logout=messagebox.askyesno("Logout","Are you sure ?",parent=self.root)
        if self.logout>0:
            self.root.destroy()
        else:
            return
    

        
        
               

    



    
      


if __name__ == "__main__":
    root = ctk.CTk()
    obj = Face_Recognition_System(root)
    root.mainloop()
