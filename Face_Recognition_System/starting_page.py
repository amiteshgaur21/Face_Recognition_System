from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image, ImageTk
from Login_page import Login


class landing_page:
    def __init__(self, root):
        self.root = root
        # ========== Window Size =========

        h = 790
        w = 1385
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 4) - (h// 4)
        self.root.geometry('{}x{}+{}+{}'.format(w, h, x, y))

        
        # =========== Title of window ==========

        self.root.title("Login")
        
        

        # ================= Background Image ======================
         
        img = Image.open(r'Face_Recognition_System\Images\ph.png')
        img = img.resize((w, h), Image.LANCZOS)
        self.photo_img = ImageTk.PhotoImage(img)
        my_label = Label(self.root, image=self.photo_img)
        my_label.place(x=0, y=0, width=w, height=h)


         # =========================== Start Button ==========================

        def Button_function():
            #start =self.root.destroy()
            Login_window=root
            app=Login(Login_window)

        
        button =ctk.CTkButton(
              master=my_label,
              text="START",
              width=10,
              bg_color='#030e32',
              text_color='#F5F5DC',
              fg_color='#030e32',
              hover_color='#030e32',
              font=('Microsoft YaHei',34),
              command=Button_function
              )
        button.place(x=460, y=640)



if __name__ == "__main__":
    root = ctk.CTk()
    obj = landing_page(root)
    root.resizable(False, False)
    #root.wm_overrideredirect(1)
    ctk.set_appearance_mode('dark')
    root.mainloop()