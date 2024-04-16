from tkinter import *
import tkinter as ttk
from PIL import Image, ImageTk
import customtkinter as ctk

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        # ======================== Window Size ======================

        h = 790
        w = 1385
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 4) - (h// 4)
        self.root.geometry('{}x{}+{}+{}'.format(w, h, x, y))
        self.root.resizable(False,False)
        ctk.set_appearance_mode("system")

        # ======================= Title of window ======================

        self.root.title("Developer")


        # =========================== Bg Image ==========================

        img = Image.open(r'C:\Users\hp\OneDrive\Desktop\Project\Face_Recognition_System\Images\13311414_v627-aew-41-technologybackground.jpg')
        img = img.resize((1385, 750), Image.LANCZOS)
        self.photo_img = ImageTk.PhotoImage(img)
        first_lb = Label(self.root, image=self.photo_img)
        first_lb.place(x=0, y=0, width=1385, height=750)

        
        my_frame =Frame(first_lb,width=700,height=450,bg='#F5F5DC',relief=RIDGE,bd=2)
        my_frame.place(x=320,y=150)
        



if __name__ == "__main__":
    root = ctk.CTk()
    obj = Face_Recognition(root)
    root.mainloop()