from tkinter import*
import tkinter
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
import os
from Student import Student
from Train import Train
from face_detector import face_recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognisation_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")
        
        img=Image.open("Images/gehu oat.jpg")
        img=img.resize((500,150),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=150)
        
        img1=Image.open("Images/face.jpg")
        img1=img1.resize((500,150),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=150)
        
        img2=Image.open("Images/gehu faculties.jpg")
        img2=img2.resize((500,150),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=150)
        
        img3=Image.open("Images/back.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_image=Label(self.root,image=self.photoimg3)
        bg_image.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_image,text="STUDENT MANAGEMENT SYSTEM ",font=("verdana",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img4=Image.open("Images/b1.jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_image,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1=Button(bg_image,text="Student Details",command=self.student_details,cursor="hand2",font=("georgia",12,"bold"),bg="blue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)
        
        img5=Image.open("Images/faceimage.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b2=Button(bg_image,image=self.photoimg5,command=self.detect,cursor="hand2")
        b2.place(x=500,y=100,width=220,height=220)
        
        b1_1=Button(bg_image,text="Face Detector",command=self.detect,cursor="hand2",font=("georgia",12,"bold"),bg="blue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)
        
        img6=Image.open("Images/attendace.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b2=Button(bg_image,image=self.photoimg6,command=self.attendance,cursor="hand2")
        b2.place(x=800,y=100,width=220,height=220)
        
        b1_1=Button(bg_image,text="Attendance",command=self.attendance,cursor="hand2",font=("georgia",12,"bold"),bg="blue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)
        
        img7=Image.open("Images/help.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b2=Button(bg_image,image=self.photoimg7,command=self.help_desk,cursor="hand2")
        b2.place(x=1100,y=100,width=220,height=220)
        
        b1_1=Button(bg_image,text="Help Desk",command=self.help_desk,cursor="hand2",font=("georgia",12,"bold"),bg="blue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        
        img8=Image.open("Images/train.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b2=Button(bg_image,image=self.photoimg8,command=self.train,cursor="hand2")
        b2.place(x=200,y=380,width=220,height=220)
        
        b1_1=Button(bg_image,text="Train Data",command=self.train,cursor="hand2",font=("georgia",12,"bold"),bg="blue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)
        
        
        img9=Image.open("Images/photo.png")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b2=Button(bg_image,image=self.photoimg9,command=self.open_img,cursor="hand2")
        b2.place(x=500,y=380,width=220,height=220)
        
        b1_1=Button(bg_image,text="Photos",command=self.open_img,cursor="hand2",font=("georgia",12,"bold"),bg="blue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)
        
        img10=Image.open("Images/developer.jpg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b2=Button(bg_image,image=self.photoimg10,command=self.developer,cursor="hand2")
        b2.place(x=800,y=380,width=220,height=220)
        
        b1_1=Button(bg_image,text="Developer",command=self.developer,cursor="hand2",font=("georgia",12,"bold"),bg="blue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)
        
        img11=Image.open("Images/exit.png")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b2=Button(bg_image,image=self.photoimg11,command=self.exit_button,cursor="hand2")
        b2.place(x=1100,y=380,width=220,height=220)
        
        b1_1=Button(bg_image,text="Exit",command=self.exit_button,cursor="hand2",font=("georgia",12,"bold"),bg="blue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)
        
    def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)

    def open_img(self):
         os.startfile("data")
            
    def train(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def detect(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognition(self.new_window)

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def exit_button(self):
        self.exit_button=tkinter.messagebox.askyesno("Exit","Are you sure you want to exit")
        if self.exit_button >0:
            self.root.destroy()
        else:
            return
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognisation_System(root)
    root.mainloop()
