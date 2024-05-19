from tkinter import *
import tkinter as ttk
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image,ImageTk
import os
import numpy as np
import cv2 



class dataset:
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

        self.root.title("Train Data")

        
        # =========================== Bg Image ==========================

        img = Image.open(r'Face_Recognition_System\Images\18b7acd6-6cdf-4f25-ab0f-845a6e59bd2c.jpg')
        img = img.resize((1400, 750), Image.LANCZOS)
        self.photo_img = ImageTk.PhotoImage(img)
        first_lb = Label(self.root, image=self.photo_img)
        first_lb.place(x=0, y=0, width=1400, height=750)

        # ============================= Heading =============================

        my_label1 = Label(self.root,text="PHOTO SAMPLE TRAINING",width=80,height=0,bg='white',fg='#041c3e',font=('TIMES NEW ROMAN',30,"bold"))
        my_label1.place(x=-250,y=0)

        # ===================== frame ==============================

        my_frame =LabelFrame(self.root,bd=2,relief="ridge",width=500,height=450,bg='white',highlightbackground="#041c3e",highlightthickness=1)
        my_frame.place(x=50,y=170)

        # =========================== First Image ==========================

        img1 = Image.open(r'Face_Recognition_System\Images\face-600x900.png')
        img1 = img1.resize((250, 200), Image.LANCZOS)
        self.photo_img1 = ImageTk.PhotoImage(img1)
        first_lb1 = Label(my_frame, image=self.photo_img1)
        first_lb1.place(x=0, y=0, width=250, height=200)

        # =========================== Second Image ==========================

        img2 = Image.open(r'Face_Recognition_System\Images\istockphoto-1139859542-612x612.jpg')
        img2= img2.resize((250, 200), Image.LANCZOS)
        self.photo_img2 = ImageTk.PhotoImage(img2)
        first_lb2 = Label(my_frame, image=self.photo_img2)
        first_lb2.place(x=250,y=0, width=245, height=200)

        # =========================== Third Image ==========================
       
        img3 = Image.open(r'Face_Recognition_System\Images\Learn-Facial-Recognition-scaled.jpg')
        img3 = img3.resize((250, 200), Image.LANCZOS)
        self.photo_img3 = ImageTk.PhotoImage(img3)
        first_lb3 = Label(my_frame, image=self.photo_img3)
        first_lb3.place(x=0, y=200, width=250, height=200)

         # =========================== Fourth Image ==========================
       
        img4 = Image.open(r'Face_Recognition_System\Images\istockphoto-1248505534-612x612.jpg')
        img4 = img4.resize((250, 200), Image.LANCZOS)
        self.photo_img4 = ImageTk.PhotoImage(img4)
        first_lb4 = Label(my_frame, image=self.photo_img4)
        first_lb4.place(x=250, y=200, width=245, height=200)

        
        # ================================== BUTTON =======================================

        
        b1_1=Button(my_frame,text="Train Data",bg='#041c3e',fg='white',cursor="hand2", font=('Times New Roman',20,'bold'),command=self.train_classifier)
        b1_1.place(x=-1,y=400,width=497,height=50)
    



# =============================== fuction ===============================

    def train_classifier(self):
        data_dir=("Face_Recognition_System/data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # gray scale image 
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Taining",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # ================================ Train the classifier And save =============================

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("Face_Recognition_System/classifier.xml")
        cv2.destroyAllWindows()
        self.root.destroy()
        messagebox.showinfo("Result","Training dataset completed !!")

        

        
         




        




if __name__ == "__main__":
    root = ctk.CTk()
    obj = dataset(root)
    root.mainloop()
