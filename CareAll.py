from tkinter import *
from tkinter import ttk
import datetime
import smtplib
from matplotlib import pyplot as plt
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql
from matplotlib import style
style.use('ggplot')
from itertools import chain


image1 = 'image1.jpg'
image2 = 'image2.jpg'
image3 = 'image3.jpg'
global conn1,conn2


class CareAll:

    def __init__(self):
        self.root=Tk()
        self.root.title('Menu')
        conn1 = pymysql.connect("localhost", "root", "root", "CareAll")
        conn2 = conn1.cursor()
        conn2.execute('''create table if not exists old
        (ID INT NOT NULL PRIMARY KEY ,
        NAME VARCHAR(100),
        AGE INT NOT NULL,
        SPOUCE_NAME VARCHAR(100),
        SPOUCE_AGE INT,
        SALARY NOT NULL,);''')
        conn1.commit()
        conn2.execute('''create table if not exists Folks
        (NAME VARCHAR(100),
         AGE INT NOT NULL,
         MOBILE No. INT NOT NULL,
         SELF INTRO VARCHAR(200) NOT NULL,
         PRIMARY KEY MOBILE No. );''')
        conn1.commit()
        conn.close()
        l1 = Button(self.a, text='Retaired Folks', font='Papyrus 22 bold', fg='Yellow', bg='Black', width=19, padx=10,
                    borderwidth=0, command=self.old).place(x=100, y=300)

        l2 = Button(self.a, text='Young Folks', font='Papyrus 22 bold', fg='Yellow', bg='Black', width=19, padx=10,
                    borderwidth=0, command=self.young).place(x=100, y=400)
        
        self.root.mainloop()
#------------------------OLD DATA--------------------------------------------

    def old(self):
        self.a.destroy()
        l1 = Button(self.a, text='ADD retaired folks', font='Papyrus 22 bold', fg='Orange', bg='Black', width=15, padx=10,
                    command=self.addold).place(x=12, y=100)
        l2 = Button(self.a, text='Search Retaired folks', font='Papyrus 22 bold', fg='Orange', bg='Black', width=15, padx=10,
                    command=self.search_retaired).place(x=12, y=200)

        l4 = Button(self.a, text='All Retaired Folks', font='Papyrus 22 bold', fg='Orange', bg='Black', width=15, padx=10,
                    command=self.all_retaired).place(x=12, y=300)
        l4 = Button(self.a, text='<< Main Menu', font='Papyrus 22 bold', fg='Orange', bg='Black', width=15, padx=10,
                    command=self.mainmenu).place(x=12, y=500)

    def addold(self):
        self.fid=StringVar()
        self.name = StringVar()
        self.age = IntVar()
        self.spoucename = StringVar()
        self.spouseage = IntVar()
        self.salary = IntVar()
        self.f1 = Frame(self.a, height=500, width=650, bg='black')
        self.f1.place(x=500, y=100)
        l1 = Label(self.f1, text='Folks Id : ', font='Papyrus 12 bold', fg='Orange', bg='Black', pady=1).place(x=50,
                                                                                                              y=50)
        e1 = Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.aid).place(x=180, y=50)
        l2 = Label(self.f1, text='Name : ', font='Papyrus 12 bold', fg='Orange', bg='Black', pady=1). \
            place(x=50, y=100)
        e2 = Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.aname).place(x=180, y=100)
        l3 = Label(self.f1, text='Spouse Name : ', font='Papyrus 12 bold', fg='orange', bg='Black', pady=1).place(x=50,
                                                                                                             y=150)
        e3 = Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.aauthor).place(x=180, y=150)
        l4 = Label(self.f1, text='Age : ', font='Papyrus 12 bold', fg='orange', bg='Black', pady=1).place(x=50, y=200)
        e2 = Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.agenre).place(x=180, y=200)
        l4 = Label(self.f1, text='Salary : ', font='Papyrus 12 bold', fg='orange', bg='Black', pady=1).place(x=50,
                                                                                                             y=250)
        e2 = Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.acopies).place(x=180, y=250)
        self.f1.grid_propagate(0)
        b1 = Button(self.f1, text='Add', font='Papyrus 10 bold', fg='black', bg='orange', width=15, bd=3,
                    command=self.addolddata).place(x=150, y=400)

        b2 = Button(self.f1, text='Back', font='Papyrus 10 bold', fg='black', bg='orange', width=15, bd=3,
                    command=self.rm).place(x=350, y=400)



    
    def addolddata(self):
        a = self.fid.get()
        b = self.name.get()
        c = self.age.get()
        d = self.spoucename.get()
        e = self.spouceage.get()
        f = self.salary.get()
        conn1 = pymysql.connect("localhost", "root", "root", "CareAll")
        conn2 = conn1.cursor()
        conn2.execute("select * from book_info where  ID =%s ", (a))
        z = conn.fetchone()
        if z is None:
            if (a and b and c and f) == "" or (a and b and c and d and e and f) :
                messagebox.showinfo("Error", "Fields cannot be empty.")
                return
            else:
                conn.execute("insert into book_info values (%s,%s,%s,%s,%s)",
                             (a, b, c, d, e,f))

                conn1.commit()
                messagebox.showinfo("Success", "folk added successfully")
                self.fid.set(" ")
                self.name.set(" ")
                self.age.set(" ")
                self.spoucename.set(" ")
                self.spouceage.set(" ")
                self.salary.set(" ")
                return


        else:
            messagebox.showinfo("Error", "folk Id already present.")
            self.fid.set(" ")
            self.name.set(" ")
            self.age.set(" ")
            self.spoucename.set(" ")
            self.spouceage.set(" ")
            self.salary.set(" ")
            conn2.close()

            return


    def search_retaired(self):
        self.oid = StringVar()
        self.f1 = Frame(self.a, height=500, width=650, bg='black')
        self.f1.place(x=500, y=100)
        l1 = Label(self.f1, text='Enter a Book-Name: ', font=('Papyrus 10 bold'), bd=2, fg='orange',
                   bg='black').place(x=20, y=40)
        e1 = Entry(self.f1, width=25, bd=5, bg='orange', fg='black', textvariable=self.sid).place(x=260, y=40)
        b1 = Button(self.f1, text='Search', bg='orange', font='Papyrus 10 bold', width=9, bd=2,
                    command=self.serch1).place(x=500, y=37)
        b1 = Button(self.f1, text='Back', bg='orange', font='Papyrus 10 bold', width=10, bd=2, command=self.rm).place(
            x=250, y=450)

    def create_tree(self, plc, lists):
        self.tree = ttk.Treeview(plc, height=13, column=(lists), show='headings')
        n = 0
        while n is not len(lists):
            self.tree.heading("#" + str(n + 1), text=lists[n])
            self.tree.column("" + lists[n], width=100)
            n = n + 1
        return self.tree

    def all_retaired(self):
        self.l1=("ID","Name","Age","Spouse","Spouce Name ","Spouce Age","Mobile No.")
        self.trees=self.create_tree(self.f1,self.l1)
        self.trees.place(x=50, y=150)
        conn = pymysql.connect("localhost", "root", "root", "CareAll")
        conn1 = conn.cursor()
        conn1.execute("select * from Old_Data")
        d = conn1.fetchall()
        if d is not None:
            for row in d:
                self.trees.insert("", END, values=row)

            conn.commit()
            return
        else:
            messagebox.showinfo("Error", " Data not present")
            conn.close()
            return

#--------------------------------Young Data---------------------------------    
    def young(self):
        self.a.destroy()
        l1 = Button(self.a, text='ADD Young folks', font='Papyrus 22 bold', fg='Orange', bg='Black', width=15, padx=10,
                    command=self.addYoung).place(x=12, y=100)
        l2 = Button(self.a, text='Search Retaired folks', font='Papyrus 22 bold', fg='Orange', bg='Black', width=15, padx=10,
                    command=self.search_young).place(x=12, y=200)

        l4 = Button(self.a, text='All Young Folks', font='Papyrus 22 bold', fg='Orange', bg='Black', width=15, padx=10,
                    command=self.all_young).place(x=12, y=300)
        l4 = Button(self.a, text='<< Main Menu', font='Papyrus 22 bold', fg='Orange', bg='Black', width=15, padx=10,
                    command=self.mainmenu).place(x=12, y=500)


    def addYoung(self):
        self.yid = StringVar()
        self.name = StringVar()
        self.age = IntVar()
        self.mobile = StringVar()
        self.intro = stringVar()
        self.f1 = Frame(self.a, height=500, width=650, bg='black')
        self.f1.place(x=500, y=100)
        l1 = Label(self.f1, text='Id : ', font='Papyrus 12 bold', fg='Orange', bg='Black', pady=1).place(x=50,
                                                                                                              y=50)
        e1 = Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.aid).place(x=180, y=50)
        l2 = Label(self.f1, text='Name : ', font='Papyrus 12 bold', fg='Orange', bg='Black', pady=1). \
            place(x=50, y=100)
        e2 = Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.aname).place(x=180, y=100)
        l3 = Label(self.f1, text='Mobile No. : ', font='Papyrus 12 bold', fg='orange', bg='Black', pady=1).place(x=50,
                                                                                                             y=150)
        e3 = Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.aauthor).place(x=180, y=150)
        l4 = Label(self.f1, text='Self Intro : ', font='Papyrus 12 bold', fg='orange', bg='Black', pady=1).place(x=50, y=200)
        e2 = Entry(self.f1, width=45, bg='orange', fg='black', textvariable=self.agenre).place(x=180, y=200)
        self.f1.grid_propagate(0)
        b1 = Button(self.f1, text='Add', font='Papyrus 10 bold', fg='black', bg='orange', width=15, bd=3,
                    command=self.addydata).place(x=150, y=400)

        b2 = Button(self.f1, text='Back', font='Papyrus 10 bold', fg='black', bg='orange', width=15, bd=3,
                    command=self.rm).place(x=350, y=400)


    def addydata(self):
        a = self.yid.get()
        b = self.name.get()
        c = self.age.get()
        d = self.mobile.get()
        e = self.intro.get()
        conn1 = pymysql.connect("localhost", "root", "root", "CareAll")
        conn2 = conn1.cursor()
        conn2.execute("select * from book_info where  ID =%s ", (a))
        z = conn.fetchone()
        if z is None:
            if (a and b and c and d and e and f) =="":
                messagebox.showinfo("Error", "Fields cannot be empty.")
                return
            else:
                conn.execute("insert into book_info values (%s,%s,%s,%s,%s)",
                             (a, b, c, d, e))

                conn1.commit()
                messagebox.showinfo("Success", "Young Folk data added successfully")
                self.yid.set(" ")
                self.name.set(" ")
                self.age.set(" ")
                self.mobile.set(" ")
                self.intro.set(" ")
                
                return


        else:
            messagebox.showinfo("Error", "Folk Id already present.")
            self.yid.set(" ")
            self.name.set(" ")
            self.age.set(" ")
            self.mobile.set(" ")
            self.intro.set(" ")
            conn2.close()

            return


#========================SEARCHING GUI FOR YOUNG==================================================================================

    def search_young(self):
        self.yid = StringVar()
        self.f1 = Frame(self.a, height=500, width=650, bg='black')
        self.f1.place(x=500, y=100)
        l1 = Label(self.f1, text='Enter a Book-Name: ', font=('Papyrus 10 bold'), bd=2, fg='orange',
                   bg='black').place(x=20, y=40)
        e1 = Entry(self.f1, width=25, bd=5, bg='orange', fg='black', textvariable=self.sid).place(x=260, y=40)
        b1 = Button(self.f1, text='Search', bg='orange', font='Papyrus 10 bold', width=9, bd=2,
                    command=self.serch1).place(x=500, y=37)
        b1 = Button(self.f1, text='Back', bg='orange', font='Papyrus 10 bold', width=10, bd=2, command=self.rm).place(
            x=250, y=450)

    def create_tree(self, plc, lists):
        self.tree = ttk.Treeview(plc, height=13, column=(lists), show='headings')
        n = 0
        while n is not len(lists):
            self.tree.heading("#" + str(n + 1), text=lists[n])
            self.tree.column("" + lists[n], width=100)
            n = n + 1
        return self.tree


        
    def all_young(self):
        self.l1=("Name","ID","Booked","Rating","Mobile No.")
        self.trees=self.create_tree(self.f1,self.l1)
        self.trees.place(x=50, y=150)
        conn = pymysql.connect("localhost", "root", "root", "CareAll")
        conn1 = conn.cursor()
        conn1.execute("select * from Young_Data")
        d = conn1.fetchall()
        if d is not None:
            for row in d:
                self.trees.insert("", END, values=row)

            conn.commit()
            return
        else:
            messagebox.showinfo("Error", " Data not present")
            conn.close()
            return



    def rm(self):
        self.f1.destroy()

    def mainmenu(self):
        self.root.destroy()
        a = menu()
        
#-------------------------Booking Young Folks---------------------------------
    def booking(self):
        Bookdate = datetime.date.today()
        rd = datetime.date.today() + datetime.timedelta(7)
        bookname = self.yname.get()
        Liid = self.yid.get()
        conn = pymysql.connect("localhost", "root", "root", "CareAll")
        conn1 = conn.cursor()
        conn2 = conn.cursor()
        conn3 = conn.cursor()
        conn1.execute("select Name, ID from Young_data where Name=%s", bookname)
        conn2.execute("select * from Student_details where Young data=%s", Liid)
        conn3.execute("select * from book_issued where Old_data=%s AND STUDENT_ID= %s ", (bookname, Liid))
        cn = conn3.fetchone()
        bn = conn2.fetchone()
        an = conn1.fetchone()
        if (bookname and Liid != ""):
            if an is not None:
                if an[1] > 0:
                    if bn is not None:
                        if cn is None:
                            conn1.execute("insert into Young_book values (%s,%s,%s,%s)",
                                          (bookname, Liid, bookdate, rd))

                            conn.commit()

                            book=self.aname.get()
                            conn1.execute("select * Young from Young_book where Book_name=%s",(book))
                            book_re=conn1.fetchone()
                            if book_re is None:
                                cop=1
                                conn1.execute("insert into  Young_book values(%s,%s)",
                                              (book,cop))
                                conn.commit()
                            else:
                                conn1.execute("update  Young_book set Copies=Copies+1 where Book_name=%s",(book))
                                conn.commit()
                            conn1.close()
                            messagebox.showinfo("Updated", "Folk Booked sucessfully.")
                            
                            return
                        else:
                            messagebox.showinfo("Error", "Folk Already Book.")
                            self.name.set(" ")
                            self.yid.set(" ")
                            return
                    else:
                        messagebox.showinfo("Error", " ID Not Avalaible.")
                        self.name.set(" ")
                        self.yid.set(" ")
                        return
                else:
                    messagebox.showinfo("Unavailable", "Folk unavailable.\nThere are no Folk .")
                    self.name.set(" ")
                    self.yid.set(" ")

                    return
            else:
                messagebox.showinfo("Error", "folk Not Available.")
                self.name.set(" ")
                self.yid.set(" ")
                return
        else:
            messagebox.showinfo("Error", "Fields cannot be blank.")
            self.yid.set(" ")
            self.folk.set(" ")
            return



#====================START==============================================================================================
def canvases(images, w, h):
    photo = Image.open(images)
    photo1 = photo.resize((w, h), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(photo1)

    canvas = Canvas(root1, width='%d' % w, height='%d' % h)
    canvas.grid(row=0, column=0)
    canvas.grid_propagate(0)
    canvas.create_image(0, 0, anchor=NW, image=photo2)
    canvas.image = photo2
    return canvas


root1 = Tk()
root1.title("CareAll")

w = root1.winfo_screenwidth()
h = root1.winfo_screenheight()
canvas = canvases(image3, w, h)


#===========================DATABASE====================================================================================
def Database():
    global conn, cursor
    conn = pymysql.connect("localhost", "root", "root", "CareAll")
    cursor = conn.cursor()


b=CareAll()






















        
        
