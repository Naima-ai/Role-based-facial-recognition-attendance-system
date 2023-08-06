from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Help:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")


        img = Image.open(r"E:\Nova Work\project-ml using python\facialrecognitionsystem\img1.jpg")
        img = img.resize((1530, 790), Image.Resampling.LANCZOS)  # high level img to lowlevel img
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1530, height=790)
        # label
        title_lbl = Label(bg_img, text="Help Desk", font=("times new roman", 35, "bold"),
                          bg="white", fg="black")
        title_lbl.place(x=0, y=100, width=1530, height=45)

        help_lbl = Label(bg_img, text="Email: teamE@gmail.com", font=("times new roman", 20, "bold"),
                          bg="white", fg="black")
        help_lbl.place(x=550, y=200)







if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()