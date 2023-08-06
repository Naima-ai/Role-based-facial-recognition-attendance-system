import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognizer import Face_recognizer
from attendance import Attendance
from help import Help

class Student_management_system:
    # function buttons

    def exit_sys(self):
        self.exit_sys=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit?",parent=self.root)
        if self.exit_sys>0:
            self.root.destroy()
        else:
            return



    def student_details(self):
            self.new_window = Toplevel(self.root)
            self.app = Student(self.new_window)




    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    def face_detect(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognizer(self.new_window)
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
    def help_desk(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)



    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")
        #bg image
        img=Image.open(r"E:\Nova Work\project-ml using python\facialrecognitionsystem\img1.jpg")
        img=img.resize((1500,790),Image.Resampling.LANCZOS) #high level img to lowlevel img
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1500,height=790)

        #label
        title_lbl=Label(bg_img,text="Facial Recognition Based Attendance System",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=130,width=1530,height=50)

        #student button
        img1 = Image.open(r"E:\Nova Work\project-ml using python\facialrecognitionsystem\stu.jpg")
        img1 = img1.resize((220,200), Image.Resampling.LANCZOS)  # high level img to lowlevel img
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1=Button(bg_img,image=self.photoimg1,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=220,width=220,height=200)

        b1_lbl = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_lbl.place(x=200, y=420, width=220, height=40)



        # Help button
        img4 = Image.open(r"E:\Nova Work\project-ml using python\facialrecognitionsystem\help.jpg")
        img4 = img4.resize((220,200), Image.Resampling.LANCZOS)  # high level img to lowlevel img
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b4 = Button(bg_img, image=self.photoimg4,command=self.help_desk, cursor="hand2")
        b4.place(x=1100, y=220, width=220, height=200)

        b4_lbl = Button(bg_img, text="Help", cursor="hand2",command=self.help_desk, font=("times new roman", 15, "bold"),
                        bg="darkblue",
                        fg="white")
        b4_lbl.place(x=1100, y=420, width=220, height=40)



        # Exit button
        img6 = Image.open(r"E:\Nova Work\project-ml using python\facialrecognitionsystem\exit2.png")
        img6 = img6.resize((220,200), Image.Resampling.LANCZOS)  # high level img to lowlevel img
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b6 = Button(bg_img, image=self.photoimg6,command=self.exit_sys, cursor="hand2")
        b6.place(x=500, y=500, width=220, height=220)

        b6_lbl = Button(bg_img, text="Exit", command=self.exit_sys,cursor="hand2", font=("times new roman", 15, "bold"),
                        bg="darkblue",
                        fg="white")
        b6_lbl.place(x=500, y=700, width=220, height=40)


















if __name__ == "__main__":
    root=Tk()
    obj=Student_management_system(root)
    root.mainloop()