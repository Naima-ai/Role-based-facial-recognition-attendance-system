from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Student:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        #variables
        self.var_dept=StringVar()
        self.var_course = StringVar()
        self.var_year= StringVar()
        self.var_semester = StringVar()
        self.var_id = StringVar()
        self.var_name= StringVar()
        self.var_div = StringVar()
        self.var_email = StringVar()

        # bg image
        img = Image.open(r"E:\Nova Work\project-ml using python\facialrecognitionsystem\img1.jpg")
        img = img.resize((1530, 790), Image.Resampling.LANCZOS)  # high level img to lowlevel img
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1530, height=790)
        # label
        title_lbl = Label(bg_img, text="Student Management System", font=("times new roman", 35, "bold"),
                          bg="white", fg="black")
        title_lbl.place(x=0, y=100, width=1530, height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=200,width=1530,height=630)

        # left label frame

        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=800,height=550)

        # current course frame
        current_cou_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Course Information",
                                font=("times new roman", 12, "bold"))
        current_cou_frame.place(x=5, y=30, width=720, height=200)
        #department
        dep_lbl=Label(current_cou_frame, text="Department", font=("times new roman", 12, "bold"))
        dep_lbl.grid(row=0, column=0, padx=10)
        dep_combo=ttk.Combobox(current_cou_frame,textvariable=self.var_dept,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","CSE","BBA","ECONOMICS","ENGLISH")
        dep_combo.current(0) #in the tuple 0th index has val select department which will be shown here
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        # Course
        course_lbl = Label(current_cou_frame, text="Course", font=("times new roman", 12, "bold"))
        course_lbl.grid(row=0, column=2, padx=10)
        course_combo = ttk.Combobox(current_cou_frame,textvariable=self.var_course,font=("times new roman", 12, "bold"), state="readonly",width=20)
        course_combo["values"] = ("Select Course", "MATH201", "EEE102", "ENG101", "CSE431","PHY 102","LAB")
        course_combo.current(0)  # in the tuple 0th index has val select department which will be shown here
        course_combo.grid(row=0, column=3, padx=2, pady=10,sticky=W)
        # Year
        year_lbl = Label(current_cou_frame, text="Year", font=("times new roman", 12, "bold"))
        year_lbl.grid(row=1, column=0, padx=10)
        year_combo = ttk.Combobox(current_cou_frame,textvariable=self.var_year,font=("times new roman", 12, "bold"), state="readonly", width=20)
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)  # in the tuple 0th index has val select department which will be shown here
        year_combo.grid(row=1, column=1, padx=2, pady=10,sticky=W)

        # semester
        sem_lbl = Label(current_cou_frame, text="Semester", font=("times new roman", 12, "bold"))
        sem_lbl.grid(row=1, column=2, padx=10)
        sem_combo = ttk.Combobox(current_cou_frame,textvariable=self.var_semester, font=("times new roman", 12, "bold"), state="readonly", width=20)
        sem_combo["values"] = ("Select Semester", "1", "2", "3", "4","5","6","7","8","9","10","11","12")
        sem_combo.current(0)  # iyearn the tuple 0th index has val select department which will be shown here
        sem_combo.grid(row=1, column=3, padx=2, pady=10,sticky=W)

        # class student info frame
        class_stu_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Class student Information",
                                       font=("times new roman", 12, "bold"))
        class_stu_frame.place(x=5, y=240,width=720, height=270)

        #Id
        Id_lbl = Label(class_stu_frame, text="Student ID", font=("times new roman", 12, "bold"))
        Id_lbl.grid(row=0, column=0, padx=10,sticky=W)
        Id_entry=ttk.Entry(class_stu_frame,width=20,textvariable=self.var_id,font=("times new roman", 12, "bold"))
        Id_entry.grid(row=0,column=1,padx=2, pady=10,sticky=W)
        #student name
        name_lbl = Label(class_stu_frame, text="Student Name", font=("times new roman", 12, "bold"))
        name_lbl.grid(row=0, column=2, padx=10, sticky=W)
        name_entry = ttk.Entry(class_stu_frame, width=20,textvariable=self.var_name, font=("times new roman", 12, "bold"))
        name_entry.grid(row=0, column=3,padx=2, pady=10, sticky=W)

        #class division
        div_lbl = Label(class_stu_frame, text="Section", font=("times new roman", 12, "bold"))
        div_lbl.grid(row=2, column=0, padx=10, sticky=W)
        div_entry = ttk.Entry(class_stu_frame, width=20,textvariable=self.var_div, font=("times new roman", 12, "bold"))
        div_entry.grid(row=2, column=1, padx=2, pady=10,sticky=W)

        #Email
        mail_lbl = Label(class_stu_frame, text="Email ID", font=("times new roman", 12, "bold"))
        mail_lbl.grid(row=2, column=2, padx=10, sticky=W)
        mail_entry = ttk.Entry(class_stu_frame, width=20,textvariable=self.var_email, font=("times new roman", 12, "bold"))
        mail_entry.grid(row=2, column=3,padx=2, pady=10, sticky=W)


        #radio buttons
        self.var_rad1=StringVar()
        radiobtn1=ttk.Radiobutton(class_stu_frame,variable=self.var_rad1,text="Take a Photo",value="Yes")
        radiobtn1.grid(row=4,column=0,pady=10)


        radiobtn2 = ttk.Radiobutton(class_stu_frame,variable=self.var_rad1, text="No Photo", value="No")
        radiobtn2.grid(row=4, column=1)
        #buttonframe
        btn_frame=Frame(class_stu_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=130,width=715,height=30)

        save_btn=Button(btn_frame,width=17,text="Save",command=self.add_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        update_btn = Button(btn_frame, width=17, text="Update",command=self.update_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)
        reset_btn = Button(btn_frame, width=17, text="Reset",command=self.reset_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=2)
        delete_btn = Button(btn_frame, width=17, text="Delete",command=self.delete_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=3)
        #frame2
        btn_frame1 = Frame(class_stu_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=160, width=200, height=30)

        take_photo_btn = Button(btn_frame1, width=15, text="Take a Photo", command=self.generate_dataset,font=("times new roman", 13, "bold"), bg="blue",
                            fg="white")
        take_photo_btn.grid(row=0, column=1)




        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        Right_frame.place(x=820, y=10, width=650, height=550)

        #--search system---
        # class student info frame
        Search_frame = LabelFrame(Right_frame, bd=2, relief=RIDGE, text="Search System",
                                     font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=30, width=630, height=70)

        search_lbl = Label(Search_frame, text="Search By: ", font=("times new roman", 12, "bold"),bg="darkblue",fg="white")
        search_lbl.grid(row=0, column=0, padx=10, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=("times new roman", 12, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select","Roll No","Email","ID")
        search_combo.current(0)  # year the tuple 0th index has val select department which will be shown here
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(Search_frame, width=15, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search1_btn = Button(Search_frame, width=10, text="Search", font=("times new roman", 11, "bold"), bg="blue",
                            fg="white")
        search1_btn.grid(row=0, column=3,padx=4)
        showall_btn = Button(Search_frame, width=10, text="Show All", font=("times new roman", 11, "bold"), bg="blue",
                           fg="white")
        showall_btn.grid(row=0, column=4)

        #table frame
        table_frame = LabelFrame(Right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=130, width=630, height=150)
        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, column=("Dep", "Course", "Year","ID", "Name","Sem", "Email","Sec","Photo"))




        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("ID", text="Student ID")
        self.student_table.heading("Name", text="Student Name")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Sec", text="Section")
        self.student_table.heading("Photo", text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("Dep", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("ID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Sec", width=100)
        self.student_table.column("Photo",width=150)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)  #The event occurs when the user releases the mouse button after clicking on the self.student_table widget

        self.fetch_data()

        #function declaration
    def add_data(self):
            if self.var_dept.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
                messagebox.showerror("Error","All the fields are required",parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="work291999",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                       self.var_dept.get(),
                                                                                                       self.var_course.get(),
                                                                                                       self.var_year.get(),
                                                                                                       self.var_id.get(),
                                                                                                       self.var_name.get(),
                                                                                                       self.var_semester.get(),

                                                                                                       self.var_email.get(),
                                                                                                       self.var_div.get(),
                                                                                                       self.var_rad1.get()))
                                                                                                                             #the no of columns created in the database
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","successfully added",parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    #fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="work291999",
                                       database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from face_recognizer.student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus() #to get the data in the fields if we click the fetch datas data
        content=self.student_table.item(cursor_focus)
        data1=content["values"]
        self.var_dept.set(data1[0])
        self.var_course.set(data1[1])
        self.var_year.set(data1[2])
        self.var_id.set(data1[3])
        self.var_name.set((data1[4]))
        self.var_semester.set(data1[5])
        self.var_email.set(data1[6])
        self.var_div.set(data1[7])
        self.var_rad1.set(data1[8])

    #update function
    def update_data(self):
        if self.var_dept.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All the fields are required", parent=self.root)
        else:
            try:
                update1=messagebox.askyesno("Update","Do you want to update?",parent=self.root)
                if update1>0:

                    conn = mysql.connector.connect(host="localhost", username="root", password="work291999",
                                       database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set `Dep`=%s,`course`=%s,`year`=%s,`name`=%s,`semester`=%s,`email`=%s,`div`=%s,`photosample`=%s where `student_id`=%s",(
                        self.var_dept.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_name.get(),
                        self.var_semester.get(),
                        self.var_email.get(),
                        self.var_div.get(),
                        self.var_rad1.get(),
                        self.var_id.get()

                    ))
                else:
                    if not update1:
                        return
                messagebox.showinfo("succes","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()  #to get the updated values
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    #delete function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Id is required",parent=self.root)
        else:
            try:
                delete1=messagebox.askyesno("Delete","Do you want to delete?",parent=self.root)
                if delete1>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="work291999",
                                           database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql="delete from face_recognizer.student where student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete1:
                        return
                conn.commit()
                self.fetch_data()  # to get the updated values
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #reset function
    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("")
        self.var_email.set("")
        self.var_rad1.set("")

    #generate dataset for take photo
    def generate_dataset(self):
        if self.var_dept.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All the fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="work291999",
                           database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from face_recognizer.student")
                my_res=my_cursor.fetchall() #to store all data in this var
                id=0
                for x in my_res:
                    id+=1
                my_cursor.execute( "update student set `Dep`=%s,`course`=%s,`year`=%s,`name`=%s,`semester`=%s,`email`=%s,`div`=%s,`photosample`=%s where `student_id`=%s",
                (
                    self.var_dept.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_name.get(),
                    self.var_semester.get(),
                    self.var_email.get(),
                    self.var_div.get(),
                    self.var_rad1.get(),
                    self.var_id.get()==id+1

                ))
                conn.commit() #commit() method is used to save changes made to the database.
                self.fetch_data()
                self.reset_data()
                conn.close()

                #load predefined data on frontal face the default file from cv2 library of opencv

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    #first convert rgb images to greyscale
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5) #1.3 is the scaling factor by default and minimum neighbour is 5

                    for(x,y,w,h) in faces: #to make a rectangle to store the cropped images
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0) #to open the camera of laptop
                img_id=0 #calculation of samples of images. have to take 100
                while True:
                    ret,my_frame=cap.read() #read the captured images
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        crop_faces=cv2.resize(face_cropped(my_frame),(450,450)) #captured image is cropped
                        crop_faces=cv2.cvtColor(crop_faces,cv2.COLOR_BGR2GRAY)
                        file_name="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name,crop_faces)
                        cv2.putText(crop_faces,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2) #around face details shown
                        cv2.imshow("Cropped face",crop_faces) #to show face on camera

                    if cv2.waitKey(1)==13 or int(img_id)==100:    # checks if the key pressed is equal to the ASCII value of the "Enter" key. The ASCII value of the "Enter" key is 13. So, this condition checks if the user has pressed the "Enter" key converts the value of img_id to an integer using the int() function.
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","generating dataset completed!")
                self.train_classifier()

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for images_saved in path:
            # using LBPH algo
            # get the data from the folder
            con_img=Image.open(images_saved).convert('L') #greyscale image converted
            Np_image=np.array(con_img,'uint8')   #convert to grid,uint8 is a datatype
            id=int(os.path.split(images_saved)[1].split('.')[1])
            faces.append(Np_image)
            ids.append(id)
            #cv2.imshow("training",Np_image) #to show the window
            #cv2.waitKey(1)==13 #closes window after enter pressed
        ids=np.array(ids)  #88% efficient after using numpy
        #train the classifier
        clf=cv2.face.LBPHFaceRecognizer_create() #algo stored in clf
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","traing completed!")




if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()