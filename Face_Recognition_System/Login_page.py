from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from forgot_password_page import Forgot
from Register_page import Register
from main_page import Face_Recognition_System
import mysql.connector

ctk.set_appearance_mode('dark')

class Login:
    def __init__(self, root):
        self.root = root
        root.resizable(False, False)
        
        # ========== Window Size =========

        h = 790
        w = 1385
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 4) - (h// 4)
        self.root.geometry('{}x{}+{}+{}'.format(w, h, x, y))

        
        # =========== Title of window ==========

        self.root.title("Login")


        # ======================== Variables ===================================

        self.var_email=StringVar()
        self.var_password=StringVar()
       
        
        

        # ================= Background Image ======================
         
        Login_img = Image.open(r'C:\Users\hp\OneDrive\Desktop\Project\Face_Recognition_System\Images\ph4.png')
        Login_img = Login_img.resize((w, h), Image.LANCZOS)
        self.Login_photo_img = ImageTk.PhotoImage(Login_img)
        my_label = Label(self.root, image=self.Login_photo_img)
        my_label.image = self.Login_photo_img
        my_label.place(x=0, y=0, width=w, height=h)


          
        # ===================  Login  ====================

        my_frame =Frame(self.root,width=420,height=450,bg='#F5F5DC',highlightbackground="black",highlightthickness=1)
        my_frame.place(x=300,y=150)

        my_label1 = Label(self.root,text="Login",width=5,height=0,bg='#F5F5DC',fg='#041c3e',font=('Microsoft YaHei',24,"bold"))
        my_label1.place(x=450,y=170)


        # ===================== Email =======================

        my_label2 = Label(self.root,text="Email",width=5,height=1,bg='#F5F5DC',fg='#041c3e',font=('Microsoft YaHei',12,"bold"))
        my_label2.place(x=350,y=250)

        Login_img1 = Image.open(r'C:\Users\hp\OneDrive\Desktop\Project\Face_Recognition_System\Images\icons8-email-24.png')
        Login_img1 = Login_img1.resize((20, 20), Image.LANCZOS)
        self.Login_photo_img1 = ImageTk.PhotoImage(Login_img1)
        my_label3 = Label(self.root, image=self.Login_photo_img1)
        my_label3.image=self.Login_photo_img1
        my_label3.place(x=640, y=280, width=20, height=20)

        email= Entry(self.root,width=30,fg='#041c3e',border=0,bg='#F5F5DC',font=('Microsoft YaHei',12),textvariable=self.var_email)
        email.place(x=360, y=280)

        f=Frame(self.root,width=310,height=2,bg='#041c3e')
        f.place(x=355, y=310)

         # ===================== Password  =======================

        my_label2 = Label(self.root,text="Password",width=10,height=1,bg='#F5F5DC',fg='#041c3e',font=('Microsoft YaHei',12,"bold"))
        my_label2.place(x=345,y=340)

          
        Login_img2 = Image.open(r'C:\Users\hp\OneDrive\Desktop\Project\Face_Recognition_System\Images\icons8-password-48.png')
        Login_img2 = Login_img2.resize((25, 25), Image.LANCZOS)
        self.Login_photo_img2 = ImageTk.PhotoImage(Login_img2)
        my_label3 = Label(self.root, image=self.Login_photo_img2)
        my_label3.image=self.Login_photo_img2
        my_label3.place(x=640, y=370, width=25, height=25)

        email= Entry(self.root,width=30,fg='#041c3e',border=0,bg='#F5F5DC',font=('Microsoft YaHei',12),textvariable=self.var_password)
        email.place(x=360, y=370)

        f1=Frame(self.root,width=311,height=2,bg='#041c3e')
        f1.place(x=355, y=400)


         # =========================== forgot Button ==========================

        def forgot_function():
             
             new_window=Toplevel(root)
             app=Forgot(new_window) 

            
           
        
        button =ctk.CTkButton(
              master=self.root,
              text="Forgot Password?",
              width=20,
              bg_color='#F5F5DC',
              text_color='#041c3e',
              fg_color='#F5F5DC',
              hover_color='#F5F5DC',
              font=('Microsoft YaHei',15,"bold"),
              command=forgot_function
              )
        button.place(x=525, y=420)

          # =========================== Login Button ==========================

       
        
        button =ctk.CTkButton(
              master=self.root,
              text="Login",
              width=310,
              bg_color='#041c3e',
              text_color='#F5F5DC',
              fg_color='#041c3e',
              font=('Microsoft YaHei',24),
              command=self.login_btn
              )
        button.place(x=355, y=470)

        # =========================== Register Button ==========================

        my_label3= Label(self.root,text="Don't have an account?",width=20,bg='#F5F5DC',fg='#041c3e',font=('Microsoft YaHei',12))
        my_label3.place(x=370,y=530)

        
        
        button =ctk.CTkButton(
              master=self.root,
              text="Register",
              width=15,
              bg_color='#F5F5DC',
              text_color='#041c3e',
              fg_color='#F5F5DC',
              hover_color='#F5F5DC',
              font=('Microsoft YaHei',15,"bold"),
              command=self.register_function
              )
        button.place(x=565, y=530)
    # ============================================= REGISTER FUNCTION ======================================

    def register_function(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    
    # ============================================= Login function ===========================================

    def login_btn(self):
        if self.var_email.get()=="":
            messagebox.showerror("Error","Please enter the email")
        elif self.var_password.get()=="":
            messagebox.showerror("Error","Please Enter the Password")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="T#9758@qlph",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from register where Email=%s and Password=%s",(self.var_email.get(),self.var_password.get()))
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid username or password")
                else:
                    self.var_email.set("")
                    self.var_password.set("")
                    
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)


                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)


        


if __name__ == "__main__":
    root = ctk.CTk()
    obj = Login(root)
    root.mainloop()
