from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import csv
from tkinter import filedialog
myData=[]


class Attendance:

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
        title_lbl = Label(bg_img, text="Attendance Sheet", font=("times new roman", 35, "bold"),
                          bg="white", fg="black")
        title_lbl.place(x=0, y=100, width=1530, height=45)
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=200, width=1530, height=630)


        # up label frame

        up_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        up_frame.place(x=10, y=10, width=1500, height=350)

        #scroll bar
        scroll_x=ttk.Scrollbar(up_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(up_frame, orient=VERTICAL)

        self.AttendanceReportTbl=ttk.Treeview(main_frame,column=("ID","Name","Dep","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTbl.xview)
        scroll_y.config(command=self.AttendanceReportTbl.yview)

        self.AttendanceReportTbl.heading("ID",text="Student ID")
        self.AttendanceReportTbl.heading("Name", text="Student Name")
        self.AttendanceReportTbl.heading("Dep", text="Department")
        self.AttendanceReportTbl.heading("Time", text="Time")
        self.AttendanceReportTbl.heading("Date", text="Date")
        self.AttendanceReportTbl.heading("Attendance", text="Attendance")

        self.AttendanceReportTbl["show"]="headings"


        self.AttendanceReportTbl.pack(fill=BOTH,expand=1)

        # buttonframe
        btn_frame = Frame(main_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=650, y=500, width=360, height=30)

        save_btn = Button(btn_frame, width=17, text="Import csv", command=self.imprt_csv,
                          font=("times new roman", 13, "bold"),
                          bg="blue", fg="white")
        save_btn.grid(row=0, column=0)
        update_btn = Button(btn_frame, width=17, text="Export csv",command=self.export_csv,
                            font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2)


#fetch data
    def fetchData(self,rows):   #tbl data inserted here
        self.AttendanceReportTbl.delete(*self.AttendanceReportTbl.get_children())
        for i in rows:
            self.AttendanceReportTbl.insert("",END,values=i)
    def imprt_csv(self):
        global myData
        myData.clear()
        file_name=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(file_name) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)
    #---export data

    def export_csv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(file_name,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
            for i in exp_write:
                 exp_write.writerow(i)
            messagebox.showinfo("Data Export","Your data is saved to"+os.path.basename(file_name)+ "successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)























if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()