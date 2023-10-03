from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
from PIL import Image, ImageDraw 

class Face_Recognition_System:
    # Call constructor (UI)
    def __init__(self, root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        # image 1
        img = Image.open("images\\download.jpeg")
        img = img.resize((500, 250))
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=0, width=500, height=250)

        # image2
        img2 = Image.open("images\\download.jpeg")
        img2 = img2.resize((500, 250))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_label = Label(self.root, image=self.photoimg2)
        first_label.place(x=500, y=0, width=500, height=250)

        # image3
        img3 = Image.open("images\\download.jpeg")
        img3 = img3.resize((500, 250))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        first_label = Label(self.root, image=self.photoimg3)
        first_label.place(x=1000, y=0, width=550, height=250)


        #background image
        img4 = Image.open("images\\naturepic.jpg")
        img4 = img4.resize((1920, 1080))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_image_label = Label(self.root, image=self.photoimg4)
        bg_image_label.place(x=0, y=130, width=1530, height=650)

        #label title on background
        title_label=Label(bg_image_label, text="FACE RECOGNITION SOFTWARE WITH ATTTENDANCE",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_label.place(x=0,y=0,width=1530,height=45)
#-----------------------------------------------------------------------------------------------------------------------------------------------------#
        #student button
        img5 = Image.open("images\\student1.png")
        img5 = img5.resize((220, 220))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_image_label, image=self.photoimg5, cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1 = Button(bg_image_label, text="Student Details", cursor="hand2", font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=290,width=220,height=40)

        #Face Detection button
        img6 = Image.open("images\\shutterstock_1651644223-1.webp")
        img6 = img6.resize((220, 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b2 = Button(bg_image_label, image=self.photoimg6, cursor="hand2")
        b2.place(x=600,y=100,width=220,height=220)
        
        b2_2 = Button(bg_image_label, text="Face Tracking", cursor="hand2", font=("times new roman",15,"bold"),bg="black",fg="white")
        b2_2.place(x=600,y=290,width=220,height=40)

        #Attendance button
        img7 = Image.open("images\\shutterstock_1651644223-1.webp")
        img7 = img7.resize((220, 220))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b3 = Button(bg_image_label, image=self.photoimg7, cursor="hand2")
        b3.place(x=1000,y=100,width=220,height=220)
        
        b3_3 = Button(bg_image_label, text="Attendance", cursor="hand2", font=("times new roman",15,"bold"),bg="black",fg="white")
        b3_3.place(x=1000,y=290,width=220,height=40)
#------------------------------------------------------------------------------------------------------------------------------------------------------------#
        #Student Login button
        img8 = Image.open("images\\shutterstock_1651644223-1.webp")      #change the image
        img8 = img8.resize((220, 220))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b4 = Button(bg_image_label, image=self.photoimg8, cursor="hand2")
        b4.place(x=200,y=400,width=220,height=220)
        
        b4_4 = Button(bg_image_label, text="Student Details", cursor="hand2", font=("times new roman",15,"bold"),bg="black",fg="white")
        b4_4.place(x=200,y=590,width=220,height=40)

        #Attendance record button
        img9 = Image.open("images\\shutterstock_1651644223-1.webp")     #change the image
        img9 = img9.resize((220, 220))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b5 = Button(bg_image_label, image=self.photoimg9, cursor="hand2")
        b5.place(x=600,y=400,width=220,height=220)
        
        b5_5 = Button(bg_image_label, text="Attendance Record", cursor="hand2", font=("times new roman",15,"bold"),bg="black",fg="white")
        b5_5.place(x=600,y=490,width=220,height=40)

        #Help Desk button
        img8 = Image.open("images\\shutterstock_1651644223-1.webp")     #change the image
        img8 = img6.resize((220, 220))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b4 = Button(bg_image_label, image=self.photoimg8, cursor="hand2")
        b4.place(x=800,y=600,width=220,height=220)
        
        b4_4 = Button(bg_image_label, text="Help-Desk", cursor="hand2", font=("times new roman",15,"bold"),bg="black",fg="white")
        b4_4.place(x=800,y=690,width=220,height=40)
#-------------------------------------------------------------------------------------------------------------------------------------------------#



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
