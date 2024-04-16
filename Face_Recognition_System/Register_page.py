from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        # ========== Window Size =========

        h = 790
        w = 1385
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 4) - (h// 4)
        self.root.geometry('{}x{}+{}+{}'.format(w, h, x, y))

        
        # =========== Title of window ==========

        self.root.title("Register")


        # ==================================== variables ====================================

        self.var_firstName=StringVar()
        self.var_lastName=StringVar()
        self.var_Email=StringVar()
        self.var_Password=StringVar()
        self.var_ConfirmPassword=StringVar()
        


        
        # ================= Background Image ======================
         
        img = Image.open(r'C:\Users\hp\OneDrive\Desktop\Project\Face_Recognition_System\Images\ph4.png')
        img = img.resize((w, h), Image.LANCZOS)
        self.photo_img = ImageTk.PhotoImage(img)
        my_label = Label(self.root, image=self.photo_img)
        my_label.place(x=0, y=0, width=w, height=h)


          # =================== Register  ====================

        my_frame =Frame(self.root,width=700,height=450,bg='#F5F5DC',highlightbackground="black",highlightthickness=1)
        my_frame.place(x=150,y=150)

        my_label1 = Label(self.root,text="Register",width=15,height=0,bg='#F5F5DC',fg='#041c3e',font=('Microsoft YaHei',24,"bold"))
        my_label1.place(x=340,y=165)

        # ===================== First Name  =======================

        my_label2 = Label(self.root,text="First Name",width=10,height=1,bg='#F5F5DC',fg='#041c3e',font=('Microsoft YaHei',12,"bold"))
        my_label2.place(x=210,y=250)

        
        img1 = Image.open(r'C:\Users\hp\OneDrive\Desktop\Project\Face_Recognition_System\Images\icons8-name-50.png')
        img1 = img1.resize((20, 20), Image.LANCZOS)
        self.photo_img1 = ImageTk.PhotoImage(img1)
        my_label3 = Label(self.root, image=self.photo_img1)
        my_label3.place(x=460, y=280, width=20, height=20)
        
        
        email= Entry(self.root,width=25,fg='#041c3e',border=0,bg='#F5F5DC',font=('Microsoft YaHei',12),textvariable=self.var_firstName)
        email.place(x=220, y=280)

        
        f=Frame(self.root,width=280,height=2,bg='#041c3e')
        f.place(x=210, y=310)


        # ===================== Last Name =======================

        my_label3 = Label(self.root,text="Last Name",width=10,height=1,bg='#F5F5DC',fg='#041c3e',font=('Microsoft YaHei',12,"bold"))
        my_label3.place(x=510,y=250)
        
        img2 = Image.open(r'C:\Users\hp\OneDrive\Desktop\Project\Face_Recognition_System\Images\icons8-name-50.png')
        img2 = img2.resize((20, 20), Image.LANCZOS)
        self.photo_img2 = ImageTk.PhotoImage(img2)
        my_label3 = Label(self.root, image=self.photo_img2)
        my_label3.place(x=770, y=280, width=20, height=20)

        email= Entry(self.root,width=25,fg='#041c3e',border=0,bg='#F5F5DC',font=('Microsoft YaHei',12),textvariable=self.var_lastName)
        email.place(x=525, y=280)
        

        f1=Frame(self.root,width=280,height=2,bg='#041c3e')
        f1.place(x=520, y=310)


        # ===================== Email =======================

        my_label4 = Label(self.root,text="Email",width=5,height=1,bg='#F5F5DC',fg='#041c3e',font=('Microsoft YaHei',12,"bold"))
        my_label4.place(x=210,y=340)
        
        img3 = Image.open(r'C:\Users\hp\OneDrive\Desktop\Project\Face_Recognition_System\Images\icons8-email-24.png')
        img3 = img3.resize((20, 20), Image.LANCZOS)
        self.photo_img3 = ImageTk.PhotoImage(img3)
        my_label4 = Label(self.root, image=self.photo_img3)
        my_label4.place(x=460, y=370, width=20, height=20)

        email= Entry(self.root,width=25,fg='#041c3e',border=0,bg='#F5F5DC',font=('Microsoft YaHei',12),textvariable=self.var_Email)
        email.place(x=220, y=370)
        

        f3=Frame(self.root,width=280,height=2,bg='#041c3e')
        f3.place(x=210, y=400)


          # ===================== Password =======================

        my_label5 = Label(self.root,text="Password",width=10,height=1,bg='#F5F5DC',fg='#041c3e',font=('Microsoft YaHei',12,"bold"))
        my_label5.place(x=510,y=340)
        
        img4 = Image.open(r'C:\Users\hp\OneDrive\Desktop\Project\Face_Recognition_System\Images\icons8-password-48.png')
        img4 = img4.resize((25, 25), Image.LANCZOS)
        self.photo_img4 = ImageTk.PhotoImage(img4)
        my_label5 = Label(self.root, image=self.photo_img4)
        my_label5.place(x=770, y=370, width=25, height=25)

        email= Entry(self.root,width=25,fg='#041c3e',border=0,bg='#F5F5DC',font=('Microsoft YaHei',12),textvariable=self.var_Password)
        email.place(x=525, y=370)
        

        f4=Frame(self.root,width=280,height=2,bg='#041c3e')
        f4.place(x=520, y=400)

         # ===================== Confirm Password =======================

        my_label6 = Label(self.root,text="Confirm Password",width=20,height=1,bg='#F5F5DC',fg='#041c3e',font=('Microsoft YaHei',12,"bold"))
        my_label6.place(x=190,y=430)
        
        img5 = Image.open(r'C:\Users\hp\OneDrive\Desktop\Project\Face_Recognition_System\Images\icons8-password-48.png')
        img5 = img5.resize((25, 25), Image.LANCZOS)
        self.photo_img5 = ImageTk.PhotoImage(img5)
        my_label6 = Label(self.root, image=self.photo_img5)
        my_label6.place(x=460, y=465, width=25, height=25)

        email= Entry(self.root,width=25,fg='#041c3e',border=0,bg='#F5F5DC',font=('Microsoft YaHei',12),textvariable=self.var_ConfirmPassword)
        email.place(x=220, y=465)
        

        f3=Frame(self.root,width=280,height=2,bg='#041c3e')
        f3.place(x=210, y=495)


         # =========================== Register Button ==========================

       
        
        button =ctk.CTkButton(
              master=self.root,
              text="Register",
              width=280,
              bg_color='#041c3e',
              text_color='#F5F5DC',
              fg_color='#041c3e',
              font=('Microsoft YaHei',24),
              command=self.Add_Data
              )
        button.place(x=520, y=460)


          # =========================== Login Button ==========================

        my_label6= Label(self.root,text="Already have an account?",width=20,bg='#F5F5DC',fg='#041c3e',font=('Microsoft YaHei',12))
        my_label6.place(x=350,y=530)

       
        
        button =ctk.CTkButton(
              master=self.root,
              text="Login here",
              width=15,
              bg_color='#F5F5DC',
              text_color='#041c3e',
              fg_color='#F5F5DC',
              hover_color='#F5F5DC',
              font=('Microsoft YaHei',15,"bold"),
              command=self.login_function
              )
        button.place(x=550, y=530)

    # ======================================= Functions ======================================

    def Add_Data(self):
        if self.var_firstName.get() == "":
            messagebox.showerror("Error","Please Enter your First Name",parent=self.root)
        elif self.var_lastName.get() == "":
            messagebox.showerror("Error","Please Enter your Last Name",parent=self.root)
        elif self.var_Email.get() == "":
            messagebox.showerror("Error","Please Enter your Email",parent=self.root)
        elif self.var_Password.get() == "":
            messagebox.showerror("Error","Please Enter the Password",parent=self.root)
        elif self.var_ConfirmPassword.get() == "":
            messagebox.showerror("Error","Please Enter the Confirm Password",parent=self.root)
        elif self.var_Password.get()!=self.var_ConfirmPassword.get():
            messagebox.showerror("Error","Confirm Password not matched",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="T#9758@qlph",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s)",(
                                                                               
                                                                              self.var_firstName.get(),
                                                                              self.var_lastName.get(),
                                                                              self.var_Email.get(),
                                                                              self.var_Password.get(),
                                                                              self.var_ConfirmPassword.get()

                                                                               ))
                conn.commit()
                conn.close()
                self.var_firstName.set("")
                self.var_lastName.set("")
                self.var_Email.set("")
                self.var_Password.set("")
                self.var_ConfirmPassword.set("")
                messagebox.showinfo("Success"," You Are successfully Registered",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)
    
    # ============================= Login Function ===========================================
    
    def login_function(self):
        self.root.destroy()
          
            






        



        


if __name__ == "__main__":
    root = ctk.CTk()
    obj = Register(root)
    root.resizable(False, False)
    ctk.set_appearance_mode('dark')
    root.mainloop()