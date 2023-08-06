from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:

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
        title_lbl = Label(bg_img, text="Train dataset", font=("times new roman", 35, "bold"),
                          bg="white", fg="black")
        title_lbl.place(x=0, y=100, width=1530, height=45)

        #button
        b1 = Button(bg_img,text="Train Data",command=self.train_classifier, cursor="hand2",font=("times new roman",30,"bold"),bg="darkblue",fg="white")
        b1.place(x=0, y=200, width=1530, height=60)

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
            cv2.imshow("training",Np_image) #to show the window
            cv2.waitKey(1)==13 #closes window after enter pressed
        ids=np.array(ids)  #88% efficient after using numpy
        #train the classifier
        clf=cv2.face.LBPHFaceRecognizer_create() #algo stored in clf
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","traing completed!")



                                                                 #"E:\Nova Work\project-ml using python\facialrecognitionsystem\data\user.3.1.jpg"
                                                                    #0                                                                   1
                                                                    #to get the id we split user.3.1 where user=0 3=1 1=2 index so split .1 means id







if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()