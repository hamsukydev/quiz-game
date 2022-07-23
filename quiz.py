import random
import sqlite3
import time
from tkinter import *
from tkinter import messagebox as mb


def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()
    login.title('Quiz App Login')

    user_name = StringVar()
    password = StringVar()

    login_canvas = Canvas(login, width=720, height=440, bg="#B64D4D")
    login_canvas.pack()

    login_frame = Frame(login_canvas, bg="orange")
    login_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(login_frame, text="Quiz App Login", fg="white", bg="orange")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2, rely=0.1)

    # USER NAME
    ulabel = Label(login_frame, text="Username", fg='white', bg='black')
    ulabel.place(relx=0.21, rely=0.4)
    uname = Entry(login_frame, bg='white', fg='black', textvariable=user_name)
    uname.config(width=42)
    uname.place(relx=0.31, rely=0.4)

    # PASSWORD
    plabel = Label(login_frame, text="Password", fg='white', bg='black')
    plabel.place(relx=0.215, rely=0.5)
    pas = Entry(login_frame, bg='white', fg='black', textvariable=password, show="*")
    pas.config(width=42)
    pas.place(relx=0.31, rely=0.5)

    def check():

        for a, b, c, d, e in logdata:
            if b == uname.get() and c == pas.get():
                print(logdata)
                menu(a)
                break
            elif len(uname.get()) == 0 and len(pas.get()) == 0:
                mb.showinfo("Error", "Username and Password Required!!")
            elif len(uname.get()) == 0 and len(pas.get()) != 0:
                mb.showinfo("Error", "Username Required!!")
            elif len(uname.get()) != 0 and len(pas.get()) == 0:
                mb.showinfo("Error", " Password Required!!")
            else:
                if len(uname.get()) != 0 and len(pas.get()) != 0:
                    mb.showinfo("Error", "Invalid Username and Password!!")

    # LOGIN BUTTON
    log = Button(login_frame, text='Login', padx=5, pady=5, width=5, command=check, fg="white", bg="black")
    log.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    log.place(relx=0.4, rely=0.6)

    login.mainloop()


def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    sup.title('Quiz App')

    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    age = StringVar()

    sup_canvas = Canvas(sup, width=720, height=440, bg="#FFBC25")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas, bg="#BADA55")
    sup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(sup_frame, text="Quiz App SignUp", fg="#FFA500", bg="#BADA55")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2, rely=0.1)

    # full name
    flabel = Label(sup_frame, text="Full Name", fg='white', bg='black')
    flabel.place(relx=0.21, rely=0.4)
    fname = Entry(sup_frame, bg='white', fg='black', textvariable=fname)
    fname.config(width=42)
    fname.place(relx=0.31, rely=0.4)

    # username
    ulabel = Label(sup_frame, text="Username", fg='white', bg='black')
    ulabel.place(relx=0.21, rely=0.5)
    user_tf = Entry(sup_frame, bg='white', fg='black')
    user_tf.config(width=42)
    user_tf.place(relx=0.31, rely=0.5)

    # password
    plabel = Label(sup_frame, text="Password", fg='white', bg='black')
    plabel.place(relx=0.215, rely=0.6)
    pas = Entry(sup_frame, bg='white', fg='black', textvariable=passW, show="*")
    pas.config(width=42)
    pas.place(relx=0.31, rely=0.6)

    # age
    clabel = Label(sup_frame, text="Age", fg='white', bg='black')
    clabel.place(relx=0.217, rely=0.7)
    age_tf = Entry(sup_frame, bg='white', fg='black')
    age_tf.config(width=42)
    age_tf.place(relx=0.31, rely=0.7)

    def addUserToDataBase():

        fullname = fname.get()
        username = user_tf.get()
        password = pas.get()
        age = age_tf.get()

        if len(fname.get()) == 0 and len(username) == 0 and len(pas.get()) == 0 and len(age) == 0:
            mb.showinfo("Error", "You haven't enter any field...Please Enter all the fields")

        elif len(username) == 0 and len(pas.get()) == 0:
            mb.showinfo("Error", "Username and password can't be empty")

        elif len(username) == 0 and len(pas.get()) != 0:
            mb.showinfo("Error", "Username can't be empty")

        elif len(username) != 0 and len(pas.get()) == 0:
            mb.showinfo("Error", "Password can't be empty")
        elif len(username) != 0 and len(pas.get()) != 0 and len(age) == 0:
            mb.showinfo("Error", "Age can't be empty")

        elif len(pas.get()) < 6:
            mb.showinfo("Error", "Password must be At least 6 No")
        elif len(username) <= 6:
            mb.showinfo("Error", "Username must be At least 6 Char")
        elif int(age) < 12:
            mb.showinfo("Error", "Username must be At least 12years Above")

        else:

            conn = sqlite3.connect('htech.db')
            create = conn.cursor()
            create.execute(
                """CREATE TABLE IF NOT EXISTS userSignUp (FULLNAME text, USERNAME text ,PASSWORD text ,AGE integer  )""")
            create.execute("INSERT INTO  userSignUp  VALUES (:fullname, :username, :password, :age)",
                           {"fullname": fullname, "username": username, "password": password, "age": age})
            conn.commit()
            create.execute('SELECT * FROM userSignUp')
            z = create.fetchall()
            print(z)
            # L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
            conn.close()
            loginPage(z)

    def gotoLogin():
        conn = sqlite3.connect('htech.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z = create.fetchall()
        loginPage(z)

    # signup BUTTON
    sp = Button(sup_frame, text='SignUp', padx=5, pady=5, width=5, command=addUserToDataBase, bg="black", fg="white")
    sp.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    sp.place(relx=0.4, rely=0.8)

    log = Button(sup_frame, text='Already have a Account?', padx=5, pady=5, width=5, command=gotoLogin, bg="#BADA55",
                 fg="black")
    log.configure(width=16, height=1, activebackground="#33B5E5", relief=FLAT)
    log.place(relx=0.393, rely=0.9)

    sup.mainloop()


def menu(abcdefgh):
    login.destroy()
    global menu
    menu = Tk()
    menu.title('Quiz App Menu')

    menu_canvas = Canvas(menu, width=720, height=440, bg="blue")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas, bg="#7FFFD4")
    menu_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    wel = Label(menu_canvas, text=' W E L C O M E  T O  Q U I Z  S T A T I O N ', fg="white", bg="green")
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1, rely=0.02)

    abcdefgh = 'Welcome ' + abcdefgh
    level34 = Label(menu_frame, text=abcdefgh, bg="black", font="calibri 18", fg="white")
    level34.place(relx=0.17, rely=0.15)

    level = Label(menu_frame, text='All Question must be answered !!', bg="orange", font="calibri 18")
    level.place(relx=0.25, rely=0.3)

    var = IntVar()
    easyR = Radiobutton(menu_frame, text='Click to Start', bg="#7FFFD4", font="calibri 16", value=1, variable=var)
    easyR.place(relx=0.25, rely=0.4)

    def navigate():

        x = var.get()
        print(x)
        if x == 1:
            menu.destroy()
            easy()
        else:
            pass

    letsgo = Button(menu_frame, text="Let's Go", bg="black", fg="white", font="calibri 12", command=navigate)
    letsgo.place(relx=0.25, rely=0.8)
    menu.mainloop()


def easy():
    global e
    e = Tk()
    e.title('Quiz App - Easy Level')

    easy_canvas = Canvas(e, width=720, height=440, bg="orange")
    easy_canvas.pack()

    easy_frame = Frame(easy_canvas, bg="#BADA55")
    easy_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    def countDown():
        check = 0
        for k in range(20, 0, -1):

            if k == 1:
                check = -1
            timer.configure(text=k)
            easy_frame.update()
            time.sleep(1)

        timer.configure(text="Times up!")
        if check == -1:
            return (-1)
        else:
            return 0

    global score
    score = 0

    easyQ = [
        [
            "What will be the output of the following Python code? \nl=[1, 0, 2, 0, 'hello', '', []] \nlist(filter(bool, nl))",
            "[1, 0, 2, ‘hello’, '', []]",
            "Error",
            "[1, 2, ‘hello’]",
            "[1, 0, 2, 0, ‘hello’, '', []]"
        ],
        [
            "What will be the output of the following Python expression if the value of x is 34? \nprint(“%f”%x)",
            "34.00",
            "34.000000",
            "34.0000",
            "34.00000000"

        ],
        [
            "What will be the value of X in the following Python expression? \nX = 2+9*((3*12)-8)/10",
            "30.8",
            "27.2",
            "28.4",
            "30.0"
        ],
        [
            "Which of these in not a core data type?",
            "Tuples",
            "Dictionary",
            "Lists",
            "Class"
        ],
        [
            "Which of the following represents the bitwise XOR operator?",
            "&",
            "!",
            "^",
            "|"
        ],
        [
            "Which of the following is not an exception handling keyword in Python?",
            "accept",
            "finally",
            "except",
            "try"
        ]
    ]
    answer = [
        "[1, 2, ‘hello’]",
        "34.000000",
        "27.2",
        "Class",
        "^",
        "accept"
    ]
    li = ['', 0, 1, 2, 3, 4, 5]
    x = random.choice(li[1:])

    ques = Label(easy_frame, text=easyQ[x][0], font="calibri 12", bg="orange")
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    var = StringVar()

    a = Radiobutton(easy_frame, text=easyQ[x][1], font="calibri 10", value=easyQ[x][1], variable=var, bg="#BADA55")
    a.place(relx=0.5, rely=0.42, anchor=CENTER)

    b = Radiobutton(easy_frame, text=easyQ[x][2], font="calibri 10", value=easyQ[x][2], variable=var, bg="#BADA55")
    b.place(relx=0.5, rely=0.52, anchor=CENTER)

    c = Radiobutton(easy_frame, text=easyQ[x][3], font="calibri 10", value=easyQ[x][3], variable=var, bg="#BADA55")
    c.place(relx=0.5, rely=0.62, anchor=CENTER)

    d = Radiobutton(easy_frame, text=easyQ[x][4], font="calibri 10", value=easyQ[x][4], variable=var, bg="#BADA55")
    d.place(relx=0.5, rely=0.72, anchor=CENTER)

    li.remove(x)

    timer = Label(e)
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)

    def display():

        if len(li) == 1:
            e.destroy()
            showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End', command=calc)

        if li:
            x = random.choice(li[1:])
            ques.configure(text=easyQ[x][0])

            a.configure(text=easyQ[x][1], value=easyQ[x][1])

            b.configure(text=easyQ[x][2], value=easyQ[x][2])

            c.configure(text=easyQ[x][3], value=easyQ[x][3])

            d.configure(text=easyQ[x][4], value=easyQ[x][4])

            li.remove(x)
            y = countDown()
            if y == -1:
                display()

    def calc():
        global score
        if (var.get() in answer):
            score += 1
        display()

    submit = Button(easy_frame, command=calc, text="Submit", fg="white", bg="black")
    submit.place(relx=0.5, rely=0.82, anchor=CENTER)

    nextQuestion = Button(easy_frame, command=display, text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.87, rely=0.82, anchor=CENTER)

    # pre=Button(easy_frame,command=display, text="Previous", fg="white", bg="black")
    # pre.place(relx=0.75, rely=0.82, anchor=CENTER)

    y = countDown()
    if y == -1:
        display()
    e.mainloop()


def showMark(mark):
    sh = Tk()
    sh.title('Your Marks')
    sh.maxsize(500, 650)
    sh.minsize(500, 650)
    label = Label(sh, text="Result", font="time 25 bold", bg="blue")
    label.grid(row=0, column=0, columnspan=20)

    p1 = Label(sh, text="Name", font="time 15 bold")
    p1.grid(row=1, column=0, padx=10, pady=10)

    p2 = Label(sh, text="Username", font="time 15 bold")
    p2.grid(row=1, column=1, padx=10, pady=10)

    p2 = Label(sh, text="Password", font="time 15 bold")
    p2.grid(row=1, column=2, padx=10, pady=10)

    p4 = Label(sh, text="Age", font="time 15 bold")
    p4.grid(row=1, column=3, padx=10, pady=10)

    p5 = Label(sh, text="Mark", font="time 15 bold")
    p5.grid(row=1, column=4, padx=10, pady=10)

    mb.showinfo("Result", f"{int(mark), 6 - int(mark)}")
    conn = sqlite3.connect('htech.db')
    r_set = conn.cursor()

    r_set.execute("INSERT INTO userSignUp (mark)VALUES('mark')")


    r_set.execute('''SELECT * from userSignUp ''')
    r = r_set.fetchall()

    num = 2
    for i in r:
        name = Label(sh, text=i[0], font="time 12 bold", fg="blue")
        name.grid(row=num, column=0, padx=10, pady=10)

        username = Label(sh, text=i[1], font="time 12 bold", fg="blue")
        username.grid(row=num, column=1, padx=10, pady=10)

        password = Label(sh, text=i[2], font="time 12 bold", fg="blue")
        password.grid(row=num, column=2, padx=10, pady=10)

        age = Label(sh, text=i[3], font="time 12 bold", fg="blue")
        age.grid(row=num, column=3, padx=10, pady=10)

        markl=Label(sh, text=int(mark), font="time 12 bold", fg="blue")
        markl.grid(row=4, column=4, padx=10, pady=10)


        num = num + 1

    sh.mainloop()

def start():
    global root
    root = Tk()
    root.title('Welcome To Quiz App')
    canvas = Canvas(root, width=720, height=440, bg='yellow')
    canvas.grid(column=0, row=1)
    img = PhotoImage(file="output-onlinepngtools.png")
    canvas.create_image(50, 10, image=img, anchor=NW)

    button = Button(root, text='Start', command=signUpPage, bg="red", fg="yellow")
    button.configure(width=102, height=2, activebackground="#33B5E5", relief=RAISED)
    button.grid(column=0, row=2)

    root.mainloop()


if __name__ == '__main__':
    start()
