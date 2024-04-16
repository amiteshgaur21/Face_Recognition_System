from tkinter import *
import tkinter as ttk
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image,ImageTk
import mysql.connector
import os
import numpy as np
import cv2
from time import strftime
from datetime import datetime



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
        ctk.set_appearance_mode("dark")

        # ======================= Title of window ======================

        self.root.title("Face Recognition")


        # ============================= Heading =============================

        my_label1 = Label(self.root,text="FACE RECOGNITION",width=80,height=0,bg='white',fg='#041c3e',font=('TIMES NEW ROMAN',30,"bold"))
        my_label1.place(x=-250,y=0)



        # =========================== Bg Image ==========================

        img = Image.open(r'C:\Users\hp\OneDrive\Desktop\Project\Face_Recognition_System\Images\44703347.jpg')
        img = img.resize((1385, 750), Image.LANCZOS)
        self.photo_img = ImageTk.PhotoImage(img)
        first_lb = Label(self.root, image=self.photo_img)
        first_lb.place(x=0, y=50, width=1385, height=750)


         # ===================== frame ==============================

        my_frame =LabelFrame(first_lb,bd=2,relief="ridge",width=400,height=500,bg='#F5F5DC',highlightbackground="#041c3e",highlightthickness=1)
        my_frame.place(x=850,y=100)


         # =========================== Second Image ==========================

        img1 = Image.open(r'C:\Users\hp\OneDrive\Desktop\Project\Face_Recognition_System\Images\18423154.jpg')
        img1= img1.resize((395, 495), Image.LANCZOS)
        self.photo_img1 = ImageTk.PhotoImage(img1)
        first_lb1 = Label(my_frame, image=self.photo_img1)
        first_lb1.place(x=0, y=0, width=395, height=495)


        # ================================== BUTTON =======================================



        b1_1=Button(my_frame,text="Scan Face",bg='#041c3e',fg='white',cursor="hand2", font=('Times New Roman',18,'bold'),command=self.face_recog)
        b1_1.place(x=100,y=430,width=200,height=40)

     # ============================================== Attendance =============================================

    def mark_attendance(self,i,n,s,r,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)and (s not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{s},{r},{d},{dtString},{d1},Present")





    # ====================================== face recognition =======================================

    def face_recog(self):
        def draw_boundary(img,classifier,scalefactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scalefactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="T#9758@qlph",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select studentName from student where studentID="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select rollno from student where studentID="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select dept from student where studentID="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select studentID from student where studentID="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select section from student where studentID="+str(id))
                s=my_cursor.fetchone()
                s="+".join(s)



                if confidence>78:
                    cv2.putText(img,f"StudentID:{i}",(x,y-85),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
                    cv2.putText(img,f"Rollno:{r}",(x,y-65),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
                    cv2.putText(img,f"Name:{n}",(x,y-45),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
                    cv2.putText(img,f"Department:{d}",(x,y-25),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
                    cv2.putText(img,f"Section:{s}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
                    self.mark_attendance(i,n,s,r,d)

                else:
                     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                     cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(1)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

















if __name__ == "__main__":
    root = ctk.CTk()
    obj = Face_Recognition(root)
    root.mainloop()
