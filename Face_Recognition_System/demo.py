 # =========================== First Image ==========================

           

       

 img = Image.open(r'C:\Users\hp\OneDrive\Desktop\Project\Images\college students-rafiki.png')
        img = img.resize((500, 200), Image.LANCZOS)
        self.photo_img = ImageTk.PhotoImage(img)
        first_lb = Label(self.root, image=self.photo_img)
        first_lb.place(x= -100, y=0, width=500, height=200)

      
       
    


         

          
       
        


        

       

        

       
        

       


        
      

        
        
        

       

        
         


         