from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image, ImageTk
import mysql.connector

ctk.set_appearance_mode('dark')

class Forgot:
    def __init__(self, root):
        self.root = root
        root.resizable(False, False)
        # ========== Window Size =========

        h = 650
        w = 1240
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 4) - (h// 4)
        self.root.geometry('{}x{}+{}+{}'.format(w, h, x, y))

        
        # =========== Title of window ==========

        self.root.title("Forgot Password")


        
        # ==================================== variables ====================================

        self.var_Email=StringVar()
        self.var_Password=StringVar()
        self.var_ConfirmPassword=StringVar()
        

        # ================= Background Image ======================
         
        Forgot_img = Image.open(r'C:\Users\hp\OneDrive\Desktop\Project\Face_Recognition_System\Images\ph4.png')
        Forgot_img = Forgot_img.resize((w, h), Image.LANCZOS)
        self.Forgot_photo_img = ImageTk.PhotoImage(Forgot_img)
        my_label = Label(self.root, image=self.Forgot_photo_img)
        my_label.image=self.Forgot_photo_img
        my_label.place(x=0, y=0, width=w, height=h)


          
        # ===================  Login  ====================

        my_frame =Frame(self.root,width=420,height=450,bg='#F5F5DC',highlightbackground="black",highlightthickness=1)
        my_frame.place(x=100,y=100)

        my_label1 = Label(self.root,text="Forgot Password",width=15,height=0,bg='#F5F5DC',fg='#041c3e',font=('Microsoft YaHei',20,"bold"))
        my_label1.place(x=180,y=120)


        # ===================== Email =======================

        my_label2 = Label(self.root,text="Email",width=5,height=1,bg='#F5F5DC',fg='#041c3e',font=('Microsoft YaHei',12,"bold"))
        my_label2.place(x=150,y=200)
        
        Forgot_img1 = Image.open(r'C:\Users\hp\OneDrive\Desktop\Project\Face_Recognition_System\Images\icons8-email-24.png')
        Forgot_img1 = Forgot_img1.resize((20, 20), Image.LANCZOS)
        self.Forgot_photo_img1 = ImageTk.PhotoImage(Forgot_img1)
        my_label2 = Label(self.root, image=self.Forgot_photo_img1)
        my_label2.image=self.Forgot_photo_img1
        my_label2.place(x=440, y=230, width=20, height=20)

        email= Entry(self.root,width=30,fg='#041c3e',border=0,bg='#F5F5DC',font=('Microsoft YaHei',12),textvariable=self.var_Email)
        email.place(x=160, y=230)
        

        f=Frame(self.root,width=310,height=2,bg='#041c3e')
        f.place(x=155, y=255)


         # =====================  New Password  =======================

        my_label3 = Label(self.root,text=" New Password",width=15,height=1,bg='#F5F5DC',fg='#041c3e',font=('Microsoft YaHei',12,"bold"))
        my_label3.place(x=140,y=280)
        
        Forgot_img2 = Image.open(r'C:\Users\hp\OneDrive\Desktop\Project\Face_Recognition_System\Images\icons8-password-48.png')
        Forgot_img2 = Forgot_img2.resize((30, 30), Image.LANCZOS)
        self.Forgot_photo_img2 = ImageTk.PhotoImage(Forgot_img2)
        my_label3 = Label(self.root, image=self.Forgot_photo_img2)
        my_label3.image=self.Forgot_photo_img2
        my_label3.place(x=433, y=305, width=30, height=30)

        Password= Entry(self.root,width=30,fg='#041c3e',border=0,bg='#F5F5DC',font=('Microsoft YaHei',12),textvariable=self.var_Password)
        Password.place(x=155, y=310)
        
        f1=Frame(self.root,width=311,height=2,bg='#041c3e')
        f1.place(x=155, y=340)


         # =====================  Confirm Password  =======================

        my_label4 = Label(self.root,text="Confirm New Password",width=25,height=1,bg='#F5F5DC',fg='#041c3e',font=('Microsoft YaHei',12,"bold"))
        my_label4.place(x=130,y=370)
        
        Forgot_img3 = Image.open(r'C:\Users\hp\OneDrive\Desktop\Project\Face_Recognition_System\Images\icons8-password-48.png')
        Forgot_img3 = Forgot_img3.resize((30, 30), Image.LANCZOS)
        self.Forgot_photo_img3 = ImageTk.PhotoImage(Forgot_img3)
        my_label4 = Label(self.root, image=self.Forgot_photo_img3)
        my_label4.image=self.Forgot_photo_img3
        my_label4.place(x=433, y=390, width=30, height=30)

        comfirm_password = Entry(self.root,width=30,fg='#041c3e',border=0,bg='#F5F5DC',font=('Microsoft YaHei',12),textvariable=self.var_ConfirmPassword)
        comfirm_password.place(x=155, y=400)
        
        f2=Frame(self.root,width=311,height=2,bg='#041c3e')
        f2.place(x=155, y=430)

         # =========================== Submit Button ==========================
        
        button =ctk.CTkButton(
              master=self.root,
              text="Submit",
              width=310,
              bg_color='#041c3e',
              text_color='#F5F5DC',
              fg_color='#041c3e',
              font=('Microsoft YaHei',24),
              command=self.Update_password
              )
        button.place(x=150, y=470)

    # ================================================== Update Password ======================================

    def Update_password(self):
        if self.var_Email.get() == "":
            messagebox.showerror("Error","Please Enter your Email")
        elif self.var_Password.get() == "":
            messagebox.showerror("Error","Please Enter your Password")
        elif self.var_ConfirmPassword.get() == "":
            messagebox.showerror("Error","Please Enter your Confirm Password")
        elif self.var_Password.get()!=self.var_ConfirmPassword.get():
            messagebox.showerror("Error","Confirm Password not matched")
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update the Password",parent=self.root)
                if Update>0:
                 conn=mysql.connector.connect(host="localhost",username="root",password="T#9758@qlph",database="face_recognition")
                 my_cursor=conn.cursor()
                 my_cursor.execute("update register set Password=%s,ConfirmPassword=%s where Email=%s",(
                                                                                                       self.var_Password.get(),
                                                                                                       self.var_ConfirmPassword.get(),
                                                                                                       self.var_Email.get()

                                                                                                        ))
                else:
                    if not Update:
                        return
                conn.commit()
                conn.close()
                self.var_Email.set("")
                self.var_Password.set("")
                self.var_ConfirmPassword.set("")
                messagebox.showinfo("Success"," Your Password has been Updated",parent=self.root)
                self.root.destroy()
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)


if __name__ == "__main__":
    root = ctk.CTk()
    obj = Forgot(root)
    root.mainloop()
