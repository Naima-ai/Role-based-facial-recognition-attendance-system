from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
# --------------------------
from train import Train
from student import Student

from main import Face_recognition_System
from studentlogin import Student_management_system

from attendance import Attendance
from help import Help
import os


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")

        # variables
        self.var_ssq = StringVar()
        self.var_sa = StringVar()
        self.var_pwd = StringVar()
        self.var_rad1=StringVar()

        self.bg = ImageTk.PhotoImage(
            file=r"E:\Nova Work\project-ml using python\facialrecognitionsystem\img1.jpg")

        lb1_bg = Label(self.root, image=self.bg)
        lb1_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame1 = Frame(self.root, bg="#002B53")
        frame1.place(x=560, y=170, width=450, height=450)



        get_str = Label(frame1, text="Login", font=("times new roman", 20, "bold"), fg="white", bg="#002B53")
        get_str.place(x=140, y=100)

        # label1
        username = lb1 = Label(frame1, text="User email:", font=("times new roman", 15, "bold"), fg="white", bg="#002B53")
        username.place(x=30, y=160)

        # entry1
        self.txtuser = ttk.Entry(frame1, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=33, y=190, width=270)

        # label2
        pwd = lb1 = Label(frame1, text="Password:", font=("times new roman", 15, "bold"), fg="white", bg="#002B53")
        pwd.place(x=30, y=230)

        # entry2
        self.txtpwd = ttk.Entry(frame1, font=("times new roman", 15, "bold"))
        self.txtpwd.place(x=33, y=260, width=270)
        radiobtn1 = ttk.Radiobutton(frame1, variable=self.var_rad1, text="Teacher",value="Teacher")
        radiobtn1.place(x=30, y=330)
        radiobtn2 = ttk.Radiobutton(frame1, variable=self.var_rad1, text="Student",value="Student")
        radiobtn2.place(x=140, y=330)

        # Creating Button Login
        loginbtn = Button(frame1, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=0,
                          relief=RIDGE, fg="#002B53", bg="white", activeforeground="white", activebackground="#007ACC")
        loginbtn.place(x=33, y=370, width=270, height=35)

        # Creating Button Registration
        regbtn = Button(frame1, command=self.reg, text="Register", font=("times new roman", 10, "bold"), bd=0,
                          relief=RIDGE, fg="white", bg="#002B53", activeforeground="orange", activebackground="#002B53")
        regbtn.place(x=33, y=420, width=50, height=20)

        # Creating Button Forget
        forgetbtn = Button(frame1, command=self.forget_pwd, text="Forget", font=("times new roman", 10, "bold"), bd=0,
                          relief=RIDGE, fg="white", bg="#002B53", activeforeground="orange", activebackground="#002B53")
        forgetbtn.place(x=90, y=420, width=50, height=20)

    #  THis function is for open register window
    def reg(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if (self.txtuser.get() == "" or self.txtpwd.get() == ""):
            messagebox.showerror("Error", "All Field Required!")
        elif (self.txtuser.get() == "admin" and self.txtpwd.get() == "admin"):
            messagebox.showinfo("Sussessfully", "Welcome to Attendance Managment System Using Facial Recognition")
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn=mysql.connector.connect(host="localhost",username="root",password="work291999",database="face_recognizer")
            mycursor = conn.cursor()
            mycursor.execute("select * from regteach where email=%s and password=%s and role=%s", (
                self.txtuser.get(),
                self.txtpwd.get(),
                self.var_rad1.get(),
            ))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username and Password!")
            else:
                open_min = messagebox.askyesno("YesNo", "Access only Admin")
                print(open_min)
                if open_min > 0 and self.var_rad1.get() == "Teacher":
                        self.new_window = Toplevel(self.root)
                        self.app = Face_recognition_System(self.new_window)
                elif open_min > 0 and self.var_rad1.get() == "Student":

                      self.new_window = Toplevel(self.root)
                      self.app = Student_management_system(self.new_window)
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()


    # =======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_ssq.get() == "Select":
            messagebox.showerror("Error", "Select the Security Question!", parent=self.root2)
        elif (self.var_sa.get() == ""):
            messagebox.showerror("Error", "Please Enter the Answer!", parent=self.root2)
        elif (self.var_pwd.get() == ""):
            messagebox.showerror("Error", "Please Enter the New Password!", parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="work291999",database="face_recognizer")
            mycursor = conn.cursor()
            query = ("select * from regteach where email=%s and sq=%s and sa=%s")
            value = (self.txtuser.get(), self.var_ssq.get(), self.var_sa.get())
            mycursor.execute(query, value)
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please Enter the Correct Answer!", parent=self.root2)
            else:
                query = ("update regteach set password=%s where email=%s")
                value = (self.var_pwd.get(), self.txtuser.get())
                mycursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Successfully Your password has been rest, Please login with new Password!",
                                    parent=self.root2)

    # =====================Forget window=========================================
    def forget_pwd(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please Enter the Email ID to reset Password!")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="work291999",database="face_recognizer")
            mycursor = conn.cursor()
            query = ("select * from regteach where email=%s")
            value = (self.txtuser.get(),)
            mycursor.execute(query, value)
            row = mycursor.fetchone()
            # print(row)

            if row == None:
                messagebox.showerror("Error", "Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                l = Label(self.root2, text="Forget Password", font=("times new roman", 30, "bold"), fg="#002B53",
                          bg="#fff")
                l.place(x=0, y=10, relwidth=1)
                # -------------------fields-------------------
                # label1
                ssq = lb1 = Label(self.root2, text="Select Security Question:", font=("times new roman", 15, "bold"),
                                  fg="#002B53", bg="#F2F2F2")
                ssq.place(x=70, y=80)

                # Combo Box1
                self.combo_security = ttk.Combobox(self.root2, textvariable=self.var_ssq,
                                                   font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security["values"] = ("Select", "Your Date of Birth", "Your Nick Name", "Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70, y=110, width=270)

                # label2
                sa = lb1 = Label(self.root2, text="Security Answer:", font=("times new roman", 15, "bold"),
                                 fg="#002B53", bg="#F2F2F2")
                sa.place(x=70, y=150)

                # entry2
                self.txtpwd = ttk.Entry(self.root2, textvariable=self.var_sa, font=("times new roman", 15, "bold"))
                self.txtpwd.place(x=70, y=180, width=270)

                # label2
                new_pwd = lb1 = Label(self.root2, text="New Password:", font=("times new roman", 15, "bold"),
                                      fg="#002B53", bg="#F2F2F2")
                new_pwd.place(x=70, y=220)

                # entry2
                self.new_pwd = ttk.Entry(self.root2, textvariable=self.var_pwd, font=("times new roman", 15, "bold"))
                self.new_pwd.place(x=70, y=250, width=270)

                # Creating Button New Password
                reset_passbtn = Button(self.root2, command=self.reset_pass, text="Reset Password",
                                  font=("times new roman", 15, "bold"), bd=0, relief=RIDGE, fg="#fff", bg="#002B53",
                                  activeforeground="white", activebackground="#007ACC")
                reset_passbtn.place(x=70, y=300, width=270, height=35)




if __name__ == "__main__":
    root = Tk()
    app = Login(root)
    root.mainloop()