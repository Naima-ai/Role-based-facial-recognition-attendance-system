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


class Face_recognizer:

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
        title_lbl = Label(bg_img, text="Record Attendance", font=("times new roman", 35, "bold"),
                          bg="white", fg="black")
        title_lbl.place(x=0, y=100, width=1530, height=45)

        # button
        b1 = Button(bg_img, text="Record", cursor="hand2",command=self.face_rec,font=("times new roman", 30, "bold"), bg="darkblue", fg="white")
        b1.place(x=600, y=500, width=400, height=60)


    #--attendance

    def mark_attendance(self,i,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            mydataList=f.readlines()    #to read the file and show it in sheet
            name_list=[]
            for  line in mydataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (n not in name_list) and (d not in name_list)):   #so that if an attendance is taken its not recorded again
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y") #day,mon,year
                dtString=now.strftime("%H:%M:%S") #time
                f.writelines(f"\n{i},{n},{d},{dtString},{d1},Present")




    #face recognition
    def face_rec(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) #to creat a rectangle in face
                id,predict=clf.predict(gray_image[y:y+h,x:x+w]) #predict from preinstalled images
                confidence=int((100*(1-predict/300))) #formula for confidence in the algo
                conn = mysql.connector.connect(host="localhost", username="root", password="work291999", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select name from face_recognizer.student where student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Dep from face_recognizer.student where student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("select student_id from face_recognizer.student where student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(map(str,i))



                if confidence > 77:
                    cv2.putText(img,f"ID:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) #(x,y-55) means top of rectangle
                    cv2.putText(img, f"Name:{n}", (x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x + w, y + h), (0,0,255),3)
                    cv2.putText(img, "Unknown Face",(x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord=[x,y,w,h]
            return coord

        def record(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade =cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #detection algo
        clf=cv2.face.LBPHFaceRecognizer_create() #for recognition
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=record(img,clf,faceCascade)
            cv2.imshow("Record attendance",img)
            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root=Tk()
    obj=Face_recognizer(root)
    root.mainloop()