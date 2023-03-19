from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

import os
from tkinter.ttk import Combobox
import pyttsx3 as pyt
from PIL import *
from plyer import *
import time



class menu:
    def tab():
        tub=Tk()
        tub.geometry("1000x720")
        #tub.iconbitmap("bank_def_icon.ico")
        tub.title('Main menu')
        tub.config(bg="cornflowerblue")

        f = Frame(tub, borderwidth=2, relief="raised")
        l_menu=Label(f,text="MENU",font=("rockwell",30,"bold"),fg='black',bg="Light green")
        l_menu.pack(pady=0)
        f.pack(pady=0)
        

        pic = Image.open("home agri-buddy 2.jpg")
        photo = ImageTk.PhotoImage(pic)        
        label = Label(tub,image=photo)
        label.image = photo
        label.pack(side=TOP)

        # Clock
        def time1():
            s = time.strftime(' %H:%M:%S %p ')
            lbl.config(text = s)
            lbl.after(1000, time)
        f = Frame(tub, borderwidth=1, relief="solid")
        lbl= Label(f, font=('calibri',20,'bold'), background='cyan', foreground='black')
        lbl.pack()
        f.place(x=10,y=10)
        time1()
        

        '''f = Frame(tub, borderwidth=4, relief="raised")
        pic = Image.open("index3.png")
        photo = ImageTk.PhotoImage(pic)        
        label = Label(f,image=photo)
        label.image = photo
        label.pack()
        f.place(x=490,y=5)'''

    

        def opt1():
            rem.voices()
            

        def opt2():
            crop.details()

        def opt3():
            video.player()


        # Option1
        f = Frame(tub, borderwidth=4, relief="raised")
        pic = Image.open("essay.png")
        photo = ImageTk.PhotoImage(pic)        
        label = Label(f,image=photo)
        label.image = photo
        label.pack()
        f.place(x=20,y=200)

        f = Frame(tub, borderwidth=3, relief="raised")
        l_opt1=Button(f,text="Reminder",font=("Arial Rounded MT Bold",20,"bold"),fg='black',bg="grey",command=opt1)
        l_opt1.pack()
        f.place(x=30,y=415)

        # option2
        f = Frame(tub, borderwidth=3, relief="raised")
        pic2 = Image.open("images (2).png")
        photo = ImageTk.PhotoImage(pic2)        
        label = Label(f,image=photo)
        label.image = photo
        label.pack()
        f.place(x=380,y=280)

        f = Frame(tub, borderwidth=3, relief="raised")
        l_opt1=Button(f,text="Crop details",font=("Arial Rounded MT Bold",20,"bold"),fg='black',bg="grey",command=opt2)
        l_opt1.pack()
        f.place(x=380,y=500)

        # option3
        f = Frame(tub, borderwidth=3, relief="raised")    
        pic5 = Image.open("f710fa0f-b891-42ec-9be7-e926281da0bd.png")
        photo = ImageTk.PhotoImage(pic5)        
        label = Label(f,image=photo)
        label.image = photo
        label.pack()
        f.place(x=720,y=200)

        f = Frame(tub, borderwidth=3, relief="raised")
        l_opt1=Button(f,text="Videos",font=("Arial Rounded MT Bold",20,"bold"),fg='black',bg="grey",command=opt3)
        l_opt1.pack()
        f.place(x=745,y=415)

        def Exit():
            answer = messagebox.askquestion('Exit Program','Do You Really Want To Exit?')
            if answer == 'yes':
                tub.destroy()

            else:
                pass

        f = Frame(tub, borderwidth=0)
        l_opt1=Button(f,text="Exit",font=("Arial Rounded MT Bold",14,"bold"),fg='white',bg="red",
                      command=Exit)
        l_opt1.pack()
        f.place(x=870,y=5)


class rem:
    def voices():

        t=Toplevel()

        a = pyt.init()
        voices = a.getProperty('voices')
        a.setProperty('voice',voices[1].id)
        t.title('Notifier')
        t.geometry("500x300")
        #img = Image.open()
        #
        # tkimage = ImageTk.PhotoImageI(img)
        #img_lbl = Label(t,image=tkimage).grid()

        def getdetail():
            get_title = title.get()
            get_msg = msg.get()
            get_time = time1.get()

            if get_title== "" or get_msg == "" or get_time == "":
                messagebox.showerror("Alert", "All field are required!" )
            else:
                int_time = float(get_time)
                min_to_sec = int_time * 60
                messagebox.showinfo("notifier set", 'set notification?')

                time.sleep(min_to_sec)
                notification.notify(title=get_title, message=get_msg,app_name = "notifier", timeout=10)
                
                a.say(get_msg)
                a.runAndWait()

        #label 1
        t_label = Label(t,text='Title to notify', font=("poppins",10))
        t_label.place(x=12,y=70)

        #entry1

        title = Entry(t,width="25",font=("poppins",10))
        title.place(x=123,y=70,height=25)

        #label2

        m_label = Label(t,text="Display Msg", font=('poppins',10))
        m_label.place(x=12,y=120)

        # entry 2

        msg = Entry(t,width="25",font=('poppins',10))
        msg.place(x=123,y=115,height=25)

        #lbl 3

        time_label = Label(t,text="Set time", font=('poppins',10))
        time_label.place(x=12,y=178)

        #entry 3

        time1 = Entry(t, width='5', font=('poppins', 13))
        time1.place(x=123,y=175,height=25)

        #label 4

        time_min_label = Label(t,text='min', font=('poppins',10))
        time_min_label.place(x=175,y=180)


        b1 = Button(t,text='set notification', font=('poppins', 10, 'bold'), fg=('#ffffff'), bg=("#528DFF")
                        , width=20, relief='raised' ,command = getdetail )
        b1.place(x=170,y=230)
        t.resizable(8,0)
        t.mainloop()

class video:
    def player():
        root= Tk()
        root.geometry("450x420")
        root.title('Related Videos')

        f = Frame(root, borderwidth=1, relief="groove")
        l_menu=Label(f,text="Related Videos",font=("rockwell",18,"bold"),fg='black',bg="lightpink")
        l_menu.pack(pady=5)
        f.pack(pady=5)

        lb=Listbox(root,width=35,height=12,font=("Helvetica",15),bg="wheat")
        lb.pack()

        def ffplay(event):
            if lb.curselection():
                file=lb.curselection()[0]
                os.startfile(lb.get(file))

        for file in os.listdir():
            if file.endswith(".mp4"): 
                lb.insert(0,file)

        bstart=Button(root,text="Start Movie",font=("Arial",14),bg="Tan")
        bstart.pack(fill='x',expand='no')
        bstart.bind("<ButtonPress-1>",ffplay)

        def top():
            root.destroy()
        bstop=Button(root,text="Close",font=("Arial",14),bg="Tan",command=top)
        bstop.pack(fill='x',expand='no')

        root.mainloop()

class crop:
    def details():
        r = Tk()
        r.title('Agryi Buddy')
        r.config(bg='Cornflowerblue')
        r.geometry("1000x720")
        
        '''#pic = Image.open("home agri-buddy 3.jpg")
        photo = ImageTk.PhotoImage(pic)        
        label = Label(r,image=photo)
        label.image = photo
        label.pack(side=TOP)'''

        def file():
            t = cr.get()
            op = open('crop.txt','r+')
            op.seek(0,0)
            x = op.readlines()
            for y in x:
                if t in y:
                    listbox.insert(INSERT,y)
            op.close()

        def Enter1():
            t=se.get()
            messagebox.showinfo("Seasons",'Your Choice is'+t)


        def Enter2():
            listbox.delete(1.0,END)
            t=cr.get()
            messagebox.showinfo("Crops","Your choice is"+t)
            file()

        def clear():
            listbox.delete(1.0,END)
            se.delete(0,END)
            cr.delete(0,END)



        lst1 = ['Corn','Tomato','Cucumber','Eggplant','Pumpkin','Watermelon','Okra','Chilli','Muskmelon','BottleGourd']
        lst2 = ['Beet','Broccoli','Carrots','Cauliflower','Green onions','Kale','Radishes','Spinach']
        lst3 = ['Sweet Pepper','Cucumber','Tomato','Radish','Beans','Brinjal','Okra','Green chillies']

        cat  = {'Summer Season':lst1 , 'Winter Season':lst2, 'Monsoon Season':lst3}

        def getupdateddata(str):
            cr['values'] = cat[se.get()]


        # Seasons

        If = LabelFrame(r,text='Seasons', font=('arial',20,'bold','italic'), bg='greenyellow', fg='Black')
        If.place(x=60,y=150)

        se = Combobox(If,font='calibri', textvariable=StringVar(),values = list(cat.keys()))
        se.bind('<<ComboboxSelected>>', getupdateddata)
        se.pack()

        ## CROPS

        If = LabelFrame(r,text ='Crops',font = ('airal',20,'bold','italic'), bg='greenyellow',fg = 'black')
        If.place(x=300,y=150)

        cr = Combobox(If,font='calibri',textvariable=StringVar())
        cr.pack()

        '''pic = Image.open('home agri-buddy 2.jpg')
        photo = ImageTk.PhotoImage(pic)
        label.image = photo
        label.pack()'''
    
        frame = Frame(r,borderwidth=2, relief='solid')
        I_head = Label(frame,text = 'Crops Details', font=('cooperblack', 35,'bold'), bg='lightgreen')
        I_head.pack()
        frame.place(x=350,y=5)

        # info
        frame = Frame(r,borderwidth=2,relief='solid')
        scrollbar=Scrollbar(r,orient='vertical')

        listbox = Text(frame,width=28,height=17,yscrollcommand=scrollbar.set, font = ('Helvetica',20),bg='ghostwhite')

        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side = RIGHT,fill = Y)
        listbox.pack(side = LEFT , fill = BOTH)
        frame.place(x=540,y=120)



        I_but = Button(r,text='Enter', font=('Copper black',15), command = Enter1,bg='powderblue')
        I_but.place(x=115,y=240)

        I_but =Button(r,text='Enter', font=('copper black',15),command = Enter2,bg='powderblue')
        I_but.place(x=355,y=240)

        I_but = Button(r,text='Clear',font=('cooper black',15),command=clear,bg='powderblue')
        I_but.place(x=240,y=320)
        r.mainloop()

root=Tk()
root.geometry("1000x720")
#root.iconbitmap("login_7yU_icon.ico")
root.title(' Agri-Buddy \ Login page ')
root.config(bg="light green")


def use():
    user=username.get()
    pw=password.get()

    if user=="a" and pw=="b":
        root.destroy()

        menu.tab()

    else:
        username.delete(0,END)
        password.delete(0,END)
        
        pop=Tk()
        t="Invalid Username or Password. Check it again."

        l=Message(pop,text=t,font=("Cooper black",30,"bold"),bg="dark blue",fg="red")
        l.pack()

        b=Button(pop,text="Ok",font=("rockwell extra bold",20),command=pop.destroy,bg="grey")
        b.pack()


def Exit():
    answer = messagebox.askquestion('Exit Program','Do You Really Want To Exit?')
    if answer == 'yes':
        root.destroy()

    else:
        pass      
    
#BG Image        
pic = Image.open("home agri-buddy.jpg")
photo = ImageTk.PhotoImage(pic)        
label = Label(root,image=photo)
label.image = photo
label.place(x=0,y=0)

#User name
l_user=Label(root, text='Username:',bg="wheat",font=("rockwell",20))
l_user.grid(row=0, sticky=W, padx=300, pady=80)

username=Entry(root,font=("rockwell",20))
username.place(x=450,y=80)

# Password
l_pass=Label(root, text='Password:',bg="wheat",font=("rockwell",20))
l_pass.place(x=300,y=140)

password=Entry(root,font=("rockwell",20),show="*")
password.place(x=450,y=137)

# Buttons
save=Button(root,text="Login",font=("arial",15,"bold"),fg='green',command=use)
save.place(x=420,y=220)

back=Button(root,text="Exit",font=("arial",15,"bold"),fg='red',command=Exit)
back.place(x=560,y=220)
root.mainloop()  