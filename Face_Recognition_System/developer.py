from tkinter import *
import tkinter as ttk
from PIL import Image, ImageTk
import customtkinter as ctk

class Developer:
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

        self.root.title("Developer")



        # =========================== Bg Image ==========================

        img = Image.open(r'Images\developer.png')
        img = img.resize((1385, 750), Image.LANCZOS)
        self.photo_img = ImageTk.PhotoImage(img)
        first_lb = Label(self.root, image=self.photo_img)
        first_lb.place(x=0, y=0, width=1385, height=750)

        
        # my_frame =Frame(first_lb,width=700,height=450,bg='#F5F5DC',relief=RIDGE,bd=2)
        # my_frame.place(x=320,y=150)
        
        # my_label1 = Label(my_frame,text="DEVELOPER",width=50,height=0,bg='#F5F5DC',fg='#041c3e',font=('Microsoft YaHei',17,"bold"))
        # my_label1.place(x=-20,y=0)
        

        

if __name__ == "__main__":
    root = ctk.CTk()
    obj = Developer(root)
    root.mainloop()