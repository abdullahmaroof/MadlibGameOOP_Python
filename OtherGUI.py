from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
from FileHandling import *

def againmain(root):
    root.destroy()
    class againwelcome:
        def __init__(self, root):
            self.root = root
            root.geometry("300x450")
            root.maxsize(300, 450)
            root.minsize(300, 450)
            root.iconbitmap('image.ico')
            root.title("madlibs - Home Page")
            root.configure(bg="sky blue")

            topframe = Frame(root, bg="gray92", height=60)
            headinglabel = Label(topframe, bg="gray92", text="Madlibs Games", font=("arial", 18, "bold"),
                                 justify=CENTER)

            topframe.pack(side=TOP, fill=BOTH, padx=20, pady=20)
            headinglabel.pack(side=TOP, fill=BOTH)

            secondframe = Frame(root, bg="gray92", height=60)
            subheadinglabel = Label(secondframe, bg="gray92", text="** Welcome **", font=("arial", 14, "bold"),
                                    justify=CENTER)

            secondframe.pack(side=TOP, fill=BOTH, padx=40, pady=20)
            subheadinglabel.pack(side=TOP, fill=BOTH)

            thirdframe = Frame(root, height=100, width=150, bg="gray92")
            self.logo_pic = Image.open("image.png")
            self.resizedlogo = self.logo_pic.resize((150, 100), Image.ANTIALIAS)
            self.logopic = ImageTk.PhotoImage(self.resizedlogo)
            logo_label = Label(thirdframe, bg="black", width=150, height=100, image=self.logopic)
            thirdframe.pack(side=TOP, pady=20, padx=40)
            logo_label.pack()

            fourthframe = Frame(root, height=50, bg="gray92")
            contbutton = Button(fourthframe, text="Continue", bg="DodgerBlue3", font=('Garuda', 15, 'bold'), width=18,
                                height=2, fg="mint cream", activebackground="mint cream",
                                activeforeground="DodgerBlue3", justify=CENTER, borderwidth=5,
                                command= lambda : form(root))
            fourthframe.pack(side=TOP, pady=10, padx=20)
            contbutton.pack()

            contlabel = Label(root, text="Press continue to play game......", bg="sky blue", font=('Garuda', 8))
            contlabel.pack(side=TOP, padx=20)

            bottom_frame = Frame(root, bg="DodgerBlue3", height=50)
            copytight_label = Label(bottom_frame, text="© Moattar Usmani BAIM-F20-009", bg="DodgerBlue3",
                                    font=('Garuda', 10, 'bold'))
            bottom_frame.pack(side=BOTTOM, fill=BOTH)
            copytight_label.pack(pady=5)

    root = Tk()
    obj = againwelcome(root)
    mainloop()


def form(root):
    root.destroy()

    class gameform:
        def __init__(self, root):
            self.root = root
            root.geometry("300x450")
            root.maxsize(300, 400)
            root.minsize(300, 400)
            root.iconbitmap('image.ico')
            root.title("madlibs - User Form")
            root.configure(bg="sky blue")

            topframe = Frame(root, bg="gray92", height=60)
            headinglabel = Label(topframe, bg="gray92", text="Madlibs Games", font=("arial", 18, "bold"),
                                 justify=CENTER)

            topframe.pack(side=TOP, fill=BOTH, padx=20, pady=20)
            headinglabel.pack(side=TOP, fill=BOTH)

            secondframe = Frame(root, bg="gray92", height=60)
            subheadinglabel = Label(secondframe, bg="gray92", text="** User Form **", font=("arial", 14, "bold"),
                                    justify=CENTER)

            secondframe.pack(side=TOP, fill=BOTH, padx=40, pady=20)
            subheadinglabel.pack(side=TOP, fill=BOTH)

            thirdframe = Frame(root, height=180, width=250, bg="sky blue")
            name_frame = Frame(thirdframe, width=300, height=40, bg="sky blue")
            name_label = Label(name_frame, width=6, height=2, text="Name", font=("arial", 12, "bold"),
                                justify=CENTER, bg="sky blue")
            self.name_entry = Entry(name_frame, width=30, borderwidth=4, justify=CENTER)
            age_frame = Frame(thirdframe, width=300, height=40, bg="sky blue")
            age_label = Label(age_frame, width=6, height=2, text="Age", font=("arial", 12, "bold"),
                                justify=CENTER, bg="sky blue")
            self.age_entry = Entry(age_frame, width=30, borderwidth=4, justify=CENTER)
            thirdframe.pack(side=TOP, pady=10, padx=20)
            name_frame.pack(side=TOP, pady=10)
            name_label.pack(side=LEFT, padx=15)
            self.name_entry.pack(side=LEFT, padx=15)
            age_frame.pack(side=TOP, pady=10)
            age_label.pack(side=LEFT, padx=15)
            self.age_entry.pack(side=LEFT, padx=15)


            fourthframe = Frame(root, height=50, bg="gray92")
            contbutton = Button(fourthframe, text="Continue", bg="DodgerBlue3", font=('Garuda', 10, 'bold'), width=18,
                                height=1, fg="mint cream", activebackground="mint cream",
                                activeforeground="DodgerBlue3", justify=CENTER, borderwidth=5,
                                command= lambda : self.enter_value())
            fourthframe.pack(side=TOP, pady=10, padx=20)
            contbutton.pack()

            contlabel = Label(root, text="Press continue to play game......", bg="sky blue", font=('Garuda', 8))
            contlabel.pack(side=TOP, padx=20)

            bottom_frame = Frame(root, bg="DodgerBlue3", height=50)
            copytight_label = Label(bottom_frame, text="© Moattar Usmani BAIM-F20-009", bg="DodgerBlue3",
                                    font=('Garuda', 10, 'bold'))
            bottom_frame.pack(side=BOTTOM, fill=BOTH)
            copytight_label.pack(pady=5)

        def earse(self):
            self.name_entry.delete(0, END)
            self.age_entry.delete(0, END)

        def enter_value(self):
            if self.name_entry.get() == "" or self.age_entry.get() == "":
                messagebox.showerror("ERROR", "Please fill all fields", parent=self.root)
            else:
                file.makingfile(self.name_entry.get(),self.age_entry.get())
                level(root)

    root = Tk()
    obj = gameform(root)
    mainloop()


def level(root):
    root.destroy()

    class gamelevel:
        def __init__(self, root):
            self.root = root
            root.geometry("300x450")
            root.maxsize(300, 400)
            root.minsize(300, 400)
            root.iconbitmap('image.ico')
            root.title("madlibs - Game Level")
            root.configure(bg="sky blue")

            topframe = Frame(root, bg="gray92", height=60)
            headinglabel = Label(topframe, bg="gray92", text="Madlibs Games", font=("arial", 18, "bold"),
                                 justify=CENTER)

            topframe.pack(side=TOP, fill=BOTH, padx=20, pady=20)
            headinglabel.pack(side=TOP, fill=BOTH)

            secondframe = Frame(root, bg="gray92", height=60)
            subheadinglabel = Label(secondframe, bg="gray92", text="** Choose Game Level **", font=("arial", 12, "bold"),
                                    justify=CENTER)

            secondframe.pack(side=TOP, fill=BOTH, padx=40, pady=20)
            subheadinglabel.pack(side=TOP, fill=BOTH)

            thirdframe = Frame(root, height=100, width=250, bg="sky blue")
            self.CheckVar1 = IntVar()
            C1 = Radiobutton(thirdframe, text="Beginner Level", variable=self.CheckVar1,
                             value=1, font=('arial',12,"bold"), bg="sky blue")
            C2 = Radiobutton(thirdframe, text="Moderate Level", variable=self.CheckVar1,
                             value=2, font=('arial',12,"bold"), bg="sky blue")
            C3 = Radiobutton(thirdframe, text="Advance Level", variable=self.CheckVar1,
                             value=3, font=('arial',12,"bold"), bg="sky blue")
            thirdframe.pack(side=TOP, padx=20)
            C1.pack(pady=8)
            C2.pack(pady=8)
            C3.pack(pady=8)


            fourthframe = Frame(root, height=50, bg="gray92")
            contbutton = Button(fourthframe, text="Play Game", bg="DodgerBlue3", font=('Garuda', 10, 'bold'), width=18,
                                height=1, fg="mint cream", activebackground="mint cream",
                                activeforeground="DodgerBlue3", justify=CENTER, borderwidth=5
                                , command= lambda : self.gonext())
            fourthframe.pack(side=TOP, pady=10, padx=20)
            contbutton.pack()

            contlabel = Label(root, text="Press play game to test yourself......", bg="sky blue", font=('Garuda', 8))
            contlabel.pack(side=TOP, padx=20)

            bottom_frame = Frame(root, bg="DodgerBlue3", height=50)
            copytight_label = Label(bottom_frame, text="© Moattar Usmani BAIM-F20-009", bg="DodgerBlue3",
                                    font=('Garuda', 10, 'bold'))
            bottom_frame.pack(side=BOTTOM, fill=BOTH)
            copytight_label.pack(pady=5)

        def gonext(self):
            if(self.CheckVar1.get()==1):
                beglevel(root)
            elif (self.CheckVar1.get() == 2):
                modlevel(root)
            elif(self.CheckVar1.get() == 1):
                advlevel(root)
            else:
                messagebox.showerror("ERROR", "No option is selected", parent=self.root)

    root = Tk()
    obj = gamelevel(root)
    mainloop()

def beglevel(root):
    root.destroy()

    class gamelevel:
        def __init__(self, root):
            self.root = root
            root.geometry("500x750")
            root.maxsize(500, 750)
            root.minsize(500, 750)
            root.iconbitmap('image.ico')
            root.title("madlibs Game - Beginner Level")
            root.configure(bg="sky blue")

            topframe = Frame(root, bg="gray92", height=60)
            headinglabel = Label(topframe, bg="gray92", text="Madlibs Games", font=("arial", 18, "bold"),
                                 justify=CENTER)

            topframe.pack(side=TOP, fill=BOTH, padx=20, pady=20)
            headinglabel.pack(side=TOP, fill=BOTH)

            secondframe = Frame(root, bg="gray92", height=200)
            storylabel = Label(secondframe, font=("arial",10), bg="gray92",
                               text='A _________ (Adjective) Child asked his Mother:\n\n_______, (Noun 1) Why are some of Your Hairs'
                                    ' _______ (Verb) Grey?\n\n\nThe Mother Tried to Use\n\nThis _________ (Noun 2) to Teach her Child:'
                                    '\n\nIt is Because of ____ (Pronoun), Dear.\n\nEvery Bad _____ (Noun 3) of Yours will Turn one '
                                    'of My _____ (Noun 4) Grey!.\n\n\nThe child replied ______ (Adverb):\n\nNow I know why Grandmother '
                                    'has only Grey Hairs on Her Head.')
            secondframe.pack(side=TOP, pady=10, padx=20, fill=BOTH)
            storylabel.pack()
            thirdframe = Frame(root, bg="gray92", height=250)
            part1frame = Label(thirdframe, bg="orange", height=2, text="Fill the Blanks", font=("arial",12,"bold"))
            part2frame = Frame(thirdframe, bg="gray92", height=210)
            part2left1 = Frame(part2frame, bg="gray92", width=60, height=210)
            blank1 = Label(part2left1, width=12, height=2, text="Adjective", font=("arial", 10),
                               justify=CENTER, bg="gray92")
            blank2 = Label(part2left1, width=12, height=2, text="Noun 1", font=("arial",10),
                               justify=CENTER, bg="gray92")
            blank3 = Label(part2left1, width=12, height=2, text="Verb", font=("arial", 10),
                           justify=CENTER, bg="gray92")
            blank4 = Label(part2left1, width=12, height=2, text="Noun 2", font=("arial", 10),
                           justify=CENTER, bg="gray92")
            part2right1 = Frame(part2frame, bg="gray92", width=60, height=210)
            self.blank1entry = Entry(part2right1, width=15, borderwidth=4, justify=CENTER)
            self.blank2entry = Entry(part2right1, width=15, borderwidth=4, justify=CENTER)
            self.blank3entry = Entry(part2right1, width=15, borderwidth=4, justify=CENTER)
            self.blank4entry = Entry(part2right1, width=15, borderwidth=4, justify=CENTER)
            part2left2 = Frame(part2frame, bg="gray92", width=60, height=210)
            blank5 = Label(part2left2, width=12, height=2, text="Pronoun", font=("arial", 10),
                           justify=CENTER, bg="gray92")
            blank6 = Label(part2left2, width=12, height=2, text="Noun 3", font=("arial", 10),
                           justify=CENTER, bg="gray92")
            blank7 = Label(part2left2, width=12, height=2, text="Noun 4", font=("arial", 10),
                           justify=CENTER, bg="gray92")
            blank8 = Label(part2left2, width=12, height=2, text="Adverb", font=("arial", 10),
                           justify=CENTER, bg="gray92")
            part2right2 = Frame(part2frame, bg="gray92", width=60, height=210)
            self.blank5entry = Entry(part2right2, width=15, borderwidth=4, justify=CENTER)
            self.blank6entry = Entry(part2right2, width=15, borderwidth=4, justify=CENTER)
            self.blank7entry = Entry(part2right2, width=15, borderwidth=4, justify=CENTER)
            self.blank8entry = Entry(part2right2, width=15, borderwidth=4, justify=CENTER)
            thirdframe.pack(side=TOP, pady=10, padx=20, fill=BOTH)
            part1frame.pack(side=TOP, fill=BOTH)
            part2frame.pack(side=TOP, fill=BOTH, expand=1)
            part2left1.pack(side=LEFT, fill=BOTH)
            blank1.pack(side=TOP, pady=10)
            blank2.pack(side=TOP, pady=10)
            blank3.pack(side=TOP, pady=10)
            blank4.pack(side=TOP, pady=10)
            part2right1.pack(side=LEFT, fill=BOTH)
            self.blank1entry.pack(side=TOP, pady=15, padx=14)
            self.blank2entry.pack(side=TOP, pady=18, padx=14)
            self.blank3entry.pack(side=TOP, pady=18, padx=14)
            self.blank4entry.pack(side=TOP, pady=15, padx=14)
            part2left2.pack(side=LEFT, fill=BOTH)
            blank5.pack(side=TOP, pady=10)
            blank6.pack(side=TOP, pady=10)
            blank7.pack(side=TOP, pady=10)
            blank8.pack(side=TOP, pady=10)
            part2right2.pack(side=LEFT, fill=BOTH)
            self.blank5entry.pack(side=TOP, pady=15, padx=14)
            self.blank6entry.pack(side=TOP, pady=18, padx=14)
            self.blank7entry.pack(side=TOP, pady=18, padx=14)
            self.blank8entry.pack(side=TOP, pady=15, padx=14)

            fourthframe = Frame(root, bg="sky blue", height=40)
            hinttbutton = Button(fourthframe, text="Hint", bg="DodgerBlue3", font=('Garuda', 10, 'bold'), width=18,
                                height=1, fg="mint cream", activebackground="mint cream",
                                activeforeground="DodgerBlue3", justify=CENTER, borderwidth=5
                                 , command= lambda : self.hints())
            compbutton = Button(fourthframe, text="Finish", bg="DodgerBlue3", font=('Garuda', 10, 'bold'), width=18,
                                 height=1, fg="mint cream", activebackground="mint cream",
                                 activeforeground="DodgerBlue3", justify=CENTER, borderwidth=5
                                , command= lambda : self.finish())

            fourthframe.pack(side=TOP, pady=5, padx=70, fill=BOTH)
            hinttbutton.pack(side=LEFT, padx=10)
            compbutton.pack(side=LEFT, padx=10)


            bottom_frame = Frame(root, bg="DodgerBlue3", height=50)
            copytight_label = Label(bottom_frame, text="© Moattar Usmani BAIM-F20-009", bg="DodgerBlue3",
                                    font=('Garuda', 10, 'bold'))
            bottom_frame.pack(side=BOTTOM, fill=BOTH)
            copytight_label.pack(pady=5)

        def hints(self):
            if(self.blank1entry.get()==""):
                messagebox.showinfo("Hint Adjective", "First letter C & similar word intrested", parent=self.root)

            elif (self.blank2entry.get() == ""):
                messagebox.showinfo("Hint Noun 1", "First letter M & derived from mother", parent=self.root)

            elif (self.blank3entry.get() == ""):
                messagebox.showinfo("Hint Verb", "First letter T & similar word rotate", parent=self.root)

            elif (self.blank4entry.get() == ""):
                messagebox.showinfo("Hint Noun 2", "First letter O & similar word moment or event", parent=self.root)

            elif (self.blank5entry.get() == ""):
                messagebox.showinfo("Hint Pronoun", "First letter Y & use to refer someone", parent=self.root)

            elif (self.blank6entry.get() == ""):
                messagebox.showinfo("Hint Noun 3", "First letter A & act of doing something", parent=self.root)

            elif (self.blank7entry.get() == ""):
                messagebox.showinfo("Hint Noun 4", "First letter H & thing we comb", parent=self.root)

            elif (self.blank8entry.get() == ""):
                messagebox.showinfo("Hint Adverb", "First letter I & definition: with no intention of causing harm", parent=self.root)

            else:
                messagebox.showinfo("No Hint", "All boxes are filled", parent=self.root)

        def finish(self):
            if(not(self.blank1entry.get() == "Curious" or self.blank1entry.get() == "curious" or self.blank1entry.get() == "CURIOUS")):
                messagebox.showerror("Wrong Adjective", "You lose, try again", parent=self.root)
                self.blank1entry.delete(0, END)

            elif(not (self.blank2entry.get() == "Mommy" or self.blank2entry.get() == "mommy" or self.blank2entry.get() == "MOMMY")):
                messagebox.showerror("Wrong Noun 1", "You lose, try again", parent=self.root)
                self.blank2entry.delete(0, END)

            elif(not(self.blank3entry.get() == "Turning" or self.blank3entry.get() == "turning" or self.blank3entry.get() == "TURNING")):
                messagebox.showerror("Wrong Verb", "You lose, try again", parent=self.root)
                self.blank3entry.delete(0, END)

            elif(not(self.blank4entry.get() == "Occasion" or self.blank4entry.get() == "occasion" or self.blank4entry.get() == "OCCASION")):
                messagebox.showerror("Wrong Noun 2", "You lose, try again", parent=self.root)
                self.blank4entry.delete(0, END)

            elif(not(self.blank5entry.get() == "You" or self.blank5entry.get() == "you" or self.blank5entry.get() == "YOU")):
                messagebox.showerror("Wrong Pronoun", "You lose, try again", parent=self.root)
                self.blank5entry.delete(0, END)

            elif(not(self.blank6entry.get() == "Action" or self.blank6entry.get() == "action" or self.blank6entry.get() == "ACTION")):
                messagebox.showerror("Wrong Noun 3", "You lose, try again", parent=self.root)
                self.blank6entry.delete(0, END)

            elif(not(self.blank7entry.get() == "Hair" or self.blank7entry.get() == "hair" or self.blank7entry.get() == "HAIR")):
                messagebox.showerror("Wrong Noun 4", "You lose, try again", parent=self.root)
                self.blank7entry.delete(0, END)

            elif(not(self.blank8entry.get() == "Innocently" or self.blank8entry.get() == "innocently" or self.blank8entry.get() == "INNOCENTLY")):
                messagebox.showerror("Wrong Adverb", "You lose, try again", parent=self.root)
                self.blank8entry.delete(0,END)

            else:
                messagebox.showinfo("WON!!!", "You Won the Game", parent=self.root)
                forbeglevel.makingfile()
                againmain(root)

    root = Tk()
    obj = gamelevel(root)
    mainloop()


def modlevel(root):
    root.destroy()

    class gamelevel:
        def __init__(self, root):
            self.root = root
            root.geometry("500x750")
            root.maxsize(500, 750)
            root.minsize(500, 750)
            root.iconbitmap('image.ico')
            root.title("madlibs Game - Moderate Level")
            root.configure(bg="sky blue")

            topframe = Frame(root, bg="gray92", height=60)
            headinglabel = Label(topframe, bg="gray92", text="Madlibs Games", font=("arial", 18, "bold"),
                                 justify=CENTER)

            topframe.pack(side=TOP, fill=BOTH, padx=20, pady=20)
            headinglabel.pack(side=TOP, fill=BOTH)

            secondframe = Frame(root, bg="gray92", height=200)
            storylabel = Label(secondframe, font=("arial",10), bg="gray92",
                               text='After a long night of _________ (Noun 1) love, the guy notices a photo\n of another man, on the wall.\n\n'
                                    'He  _______ (Verb 1) to worry\n\n\"Is this your husband?\" he ________ (Adverb) asks.\nShe replies, _________ (Verb 2) up to him.'
                                    '\n\n\"Your boyfriend then?\" he  _______ (Verb 3). \"No, not at all,\"\n\nShe says, nibbling away at his _____ (Noun 2).\n'
                                    '\n\"Is it your dad or your brother?\" he _____ (Verb 4),  hoping to be reassured.\n\n\"No, no, no! You are so ______ (Adjective) when you\'re\n')
            secondframe.pack(side=TOP, pady=10, padx=20, fill=BOTH)
            storylabel.pack()
            thirdframe = Frame(root, bg="gray92", height=250)
            part1frame = Label(thirdframe, bg="orange", height=2, text="Fill the Blanks", font=("arial",12,"bold"))
            part2frame = Frame(thirdframe, bg="gray92", height=210)
            part2left1 = Frame(part2frame, bg="gray92", width=60, height=210)
            blank1 = Label(part2left1, width=12, height=2, text="Noun 1", font=("arial", 10),
                               justify=CENTER, bg="gray92")
            blank2 = Label(part2left1, width=12, height=2, text="Verb 1", font=("arial",10),
                               justify=CENTER, bg="gray92")
            blank3 = Label(part2left1, width=12, height=2, text="Adverb", font=("arial", 10),
                           justify=CENTER, bg="gray92")
            blank4 = Label(part2left1, width=12, height=2, text="Verb 2", font=("arial", 10),
                           justify=CENTER, bg="gray92")
            part2right1 = Frame(part2frame, bg="gray92", width=60, height=210)
            self.blank1entry = Entry(part2right1, width=15, borderwidth=4, justify=CENTER)
            self.blank2entry = Entry(part2right1, width=15, borderwidth=4, justify=CENTER)
            self.blank3entry = Entry(part2right1, width=15, borderwidth=4, justify=CENTER)
            self.blank4entry = Entry(part2right1, width=15, borderwidth=4, justify=CENTER)
            part2left2 = Frame(part2frame, bg="gray92", width=60, height=210)
            blank5 = Label(part2left2, width=12, height=2, text="Verb 3", font=("arial", 10),
                           justify=CENTER, bg="gray92")
            blank6 = Label(part2left2, width=12, height=2, text="Noun 2", font=("arial", 10),
                           justify=CENTER, bg="gray92")
            blank7 = Label(part2left2, width=12, height=2, text="Verb 4", font=("arial", 10),
                           justify=CENTER, bg="gray92")
            blank8 = Label(part2left2, width=12, height=2, text="Adjective", font=("arial", 10),
                           justify=CENTER, bg="gray92")
            part2right2 = Frame(part2frame, bg="gray92", width=60, height=210)
            self.blank5entry = Entry(part2right2, width=15, borderwidth=4, justify=CENTER)
            self.blank6entry = Entry(part2right2, width=15, borderwidth=4, justify=CENTER)
            self.blank7entry = Entry(part2right2, width=15, borderwidth=4, justify=CENTER)
            self.blank8entry = Entry(part2right2, width=15, borderwidth=4, justify=CENTER)
            thirdframe.pack(side=TOP, pady=10, padx=20, fill=BOTH)
            part1frame.pack(side=TOP, fill=BOTH)
            part2frame.pack(side=TOP, fill=BOTH, expand=1)
            part2left1.pack(side=LEFT, fill=BOTH)
            blank1.pack(side=TOP, pady=10)
            blank2.pack(side=TOP, pady=10)
            blank3.pack(side=TOP, pady=10)
            blank4.pack(side=TOP, pady=10)
            part2right1.pack(side=LEFT, fill=BOTH)
            self.blank1entry.pack(side=TOP, pady=15, padx=14)
            self.blank2entry.pack(side=TOP, pady=18, padx=14)
            self.blank3entry.pack(side=TOP, pady=18, padx=14)
            self.blank4entry.pack(side=TOP, pady=15, padx=14)
            part2left2.pack(side=LEFT, fill=BOTH)
            blank5.pack(side=TOP, pady=10)
            blank6.pack(side=TOP, pady=10)
            blank7.pack(side=TOP, pady=10)
            blank8.pack(side=TOP, pady=10)
            part2right2.pack(side=LEFT, fill=BOTH)
            self.blank5entry.pack(side=TOP, pady=15, padx=14)
            self.blank6entry.pack(side=TOP, pady=18, padx=14)
            self.blank7entry.pack(side=TOP, pady=18, padx=14)
            self.blank8entry.pack(side=TOP, pady=15, padx=14)

            fourthframe = Frame(root, bg="sky blue", height=40)
            hinttbutton = Button(fourthframe, text="Hint", bg="DodgerBlue3", font=('Garuda', 10, 'bold'), width=18,
                                height=1, fg="mint cream", activebackground="mint cream",
                                activeforeground="DodgerBlue3", justify=CENTER, borderwidth=5
                                 , command= lambda : self.hints())
            compbutton = Button(fourthframe, text="Finish", bg="DodgerBlue3", font=('Garuda', 10, 'bold'), width=18,
                                 height=1, fg="mint cream", activebackground="mint cream",
                                 activeforeground="DodgerBlue3", justify=CENTER, borderwidth=5
                                , command= lambda : self.finish())

            fourthframe.pack(side=TOP, pady=5, padx=70, fill=BOTH)
            hinttbutton.pack(side=LEFT, padx=10)
            compbutton.pack(side=LEFT, padx=10)


            bottom_frame = Frame(root, bg="DodgerBlue3", height=50)
            copytight_label = Label(bottom_frame, text="© Moattar Usmani BAIM-F20-009", bg="DodgerBlue3",
                                    font=('Garuda', 10, 'bold'))
            bottom_frame.pack(side=BOTTOM, fill=BOTH)
            copytight_label.pack(pady=5)

        def hints(self):
            if(self.blank1entry.get()==""):
                messagebox.showinfo("Hint Noun 1", "First letter M & the process of making or producing something", parent=self.root)

            elif (self.blank2entry.get() == ""):
                messagebox.showinfo("Hint Verb 1", "First letter B & similar word is start", parent=self.root)

            elif (self.blank3entry.get() == ""):
                messagebox.showinfo("Hint Adverb", "First letter N & in an anxious or apprehensive manner", parent=self.root)

            elif (self.blank4entry.get() == ""):
                messagebox.showinfo("Hint Verb 2", "First letter S & settle or move into a warm, comfortable position", parent=self.root)

            elif (self.blank5entry.get() == ""):
                messagebox.showinfo("Hint Verb 3", "First letter C & similar word carry on with", parent=self.root)

            elif (self.blank6entry.get() == ""):
                messagebox.showinfo("Hint Noun 2", "First letter E & an organ sensitive to sound in other animals", parent=self.root)

            elif (self.blank7entry.get() == ""):
                messagebox.showinfo("Hint Verb 4", "First letter I & ask for information from someone", parent=self.root)

            elif (self.blank8entry.get() == ""):
                messagebox.showinfo("Hint Adjective", "First letter H & definition: having a high degree of heat or a high temperature", parent=self.root)

            else:
                messagebox.showinfo("No Hint", "All boxes are filled", parent=self.root)

        def finish(self):
            if(not(self.blank1entry.get() == "Making" or self.blank1entry.get() == "making" or self.blank1entry.get() == "MAKING")):
                messagebox.showerror("Wrong Noun 1", "You lose, try again", parent=self.root)
                self.blank1entry.delete(0, END)

            elif(not (self.blank2entry.get() == "Begins" or self.blank2entry.get() == "begins" or self.blank2entry.get() == "BEGINS")):
                messagebox.showerror("Wrong Verb 1", "You lose, try again", parent=self.root)
                self.blank2entry.delete(0, END)

            elif(not(self.blank3entry.get() == "Nervously" or self.blank3entry.get() == "nervously" or self.blank3entry.get() == "NERVOUSLY")):
                messagebox.showerror("Wrong Adverb", "You lose, try again", parent=self.root)
                self.blank3entry.delete(0, END)

            elif(not(self.blank4entry.get() == "Snuggling" or self.blank4entry.get() == "snuggling" or self.blank4entry.get() == "SUNGGLING")):
                messagebox.showerror("Wrong Verb 2", "You lose, try again", parent=self.root)
                self.blank4entry.delete(0, END)

            elif(not(self.blank5entry.get() == "Continues" or self.blank5entry.get() == "continues" or self.blank5entry.get() == "CONTINUES")):
                messagebox.showerror("Wrong Verb 3", "You lose, try again", parent=self.root)
                self.blank5entry.delete(0, END)

            elif(not(self.blank6entry.get() == "Ear" or self.blank6entry.get() == "ear" or self.blank6entry.get() == "EAR")):
                messagebox.showerror("Wrong Noun 2", "You lose, try again", parent=self.root)
                self.blank6entry.delete(0, END)

            elif(not(self.blank7entry.get() == "Inquires" or self.blank7entry.get() == "inquires" or self.blank7entry.get() == "INQUIRES")):
                messagebox.showerror("Wrong Verb 4", "You lose, try again", parent=self.root)
                self.blank7entry.delete(0, END)

            elif(not(self.blank8entry.get() == "Hot" or self.blank8entry.get() == "hot" or self.blank8entry.get() == "HOT")):
                messagebox.showerror("Wrong Adjective", "You lose, try again", parent=self.root)
                self.blank8entry.delete(0,END)

            else:
                messagebox.showinfo("WON!!!", "You Won the Game", parent=self.root)
                formodlevel.makingfile()
                againmain(root)


    root = Tk()
    obj = gamelevel(root)
    mainloop()


def advlevel(root):
    root.destroy()

    class gamelevel:
        def __init__(self, root):
            self.root = root
            root.geometry("500x750")
            root.maxsize(500, 750)
            root.minsize(500, 750)
            root.iconbitmap('image.ico')
            root.title("madlibs Game - Advance Level")
            root.configure(bg="sky blue")

            topframe = Frame(root, bg="gray92", height=60)
            headinglabel = Label(topframe, bg="gray92", text="Madlibs Games", font=("arial", 18, "bold"),
                                 justify=CENTER)

            topframe.pack(side=TOP, fill=BOTH, padx=20, pady=20)
            headinglabel.pack(side=TOP, fill=BOTH)

            secondframe = Frame(root, bg="gray92", height=200)
            storylabel = Label(secondframe, font=("arial",10), bg="gray92",
                               text='A _________ (Adjective) Child asked his Mother:\n\n_______, (Noun 1) Why are some of Your Hairs'
                                    ' _______ (Verb) Grey?\n\n\nThe Mother Tried to Use\n\nThis _________ (Noun 2) to Teach her Child:'
                                    '\n\nIt is Because of ____ (Pronoun), Dear.\n\nEvery Bad _____ (Noun 3) of Yours will Turn one '
                                    'of My _____ (Noun 4) Grey!.\n\n\nThe child replied ______ (Adverb):\n\nNow I know why Grandmother '
                                    'has only Grey Hairs on Her Head.')
            secondframe.pack(side=TOP, pady=10, padx=20, fill=BOTH)
            storylabel.pack()
            thirdframe = Frame(root, bg="gray92", height=250)
            part1frame = Label(thirdframe, bg="orange", height=2, text="Fill the Blanks", font=("arial",12,"bold"))
            part2frame = Frame(thirdframe, bg="gray92", height=210)
            part2left1 = Frame(part2frame, bg="gray92", width=60, height=210)
            blank1 = Label(part2left1, width=12, height=2, text="Adjective", font=("arial", 10),
                               justify=CENTER, bg="gray92")
            blank2 = Label(part2left1, width=12, height=2, text="Noun 1", font=("arial",10),
                               justify=CENTER, bg="gray92")
            blank3 = Label(part2left1, width=12, height=2, text="Verb", font=("arial", 10),
                           justify=CENTER, bg="gray92")
            blank4 = Label(part2left1, width=12, height=2, text="Noun 2", font=("arial", 10),
                           justify=CENTER, bg="gray92")
            part2right1 = Frame(part2frame, bg="gray92", width=60, height=210)
            self.blank1entry = Entry(part2right1, width=15, borderwidth=4, justify=CENTER)
            self.blank2entry = Entry(part2right1, width=15, borderwidth=4, justify=CENTER)
            self.blank3entry = Entry(part2right1, width=15, borderwidth=4, justify=CENTER)
            self.blank4entry = Entry(part2right1, width=15, borderwidth=4, justify=CENTER)
            part2left2 = Frame(part2frame, bg="gray92", width=60, height=210)
            blank5 = Label(part2left2, width=12, height=2, text="Pronoun", font=("arial", 10),
                           justify=CENTER, bg="gray92")
            blank6 = Label(part2left2, width=12, height=2, text="Noun 3", font=("arial", 10),
                           justify=CENTER, bg="gray92")
            blank7 = Label(part2left2, width=12, height=2, text="Noun 4", font=("arial", 10),
                           justify=CENTER, bg="gray92")
            blank8 = Label(part2left2, width=12, height=2, text="Adverb", font=("arial", 10),
                           justify=CENTER, bg="gray92")
            part2right2 = Frame(part2frame, bg="gray92", width=60, height=210)
            self.blank5entry = Entry(part2right2, width=15, borderwidth=4, justify=CENTER)
            self.blank6entry = Entry(part2right2, width=15, borderwidth=4, justify=CENTER)
            self.blank7entry = Entry(part2right2, width=15, borderwidth=4, justify=CENTER)
            self.blank8entry = Entry(part2right2, width=15, borderwidth=4, justify=CENTER)
            thirdframe.pack(side=TOP, pady=10, padx=20, fill=BOTH)
            part1frame.pack(side=TOP, fill=BOTH)
            part2frame.pack(side=TOP, fill=BOTH, expand=1)
            part2left1.pack(side=LEFT, fill=BOTH)
            blank1.pack(side=TOP, pady=10)
            blank2.pack(side=TOP, pady=10)
            blank3.pack(side=TOP, pady=10)
            blank4.pack(side=TOP, pady=10)
            part2right1.pack(side=LEFT, fill=BOTH)
            self.blank1entry.pack(side=TOP, pady=15, padx=14)
            self.blank2entry.pack(side=TOP, pady=18, padx=14)
            self.blank3entry.pack(side=TOP, pady=18, padx=14)
            self.blank4entry.pack(side=TOP, pady=15, padx=14)
            part2left2.pack(side=LEFT, fill=BOTH)
            blank5.pack(side=TOP, pady=10)
            blank6.pack(side=TOP, pady=10)
            blank7.pack(side=TOP, pady=10)
            blank8.pack(side=TOP, pady=10)
            part2right2.pack(side=LEFT, fill=BOTH)
            self.blank5entry.pack(side=TOP, pady=15, padx=14)
            self.blank6entry.pack(side=TOP, pady=18, padx=14)
            self.blank7entry.pack(side=TOP, pady=18, padx=14)
            self.blank8entry.pack(side=TOP, pady=15, padx=14)

            fourthframe = Frame(root, bg="sky blue", height=40)
            hinttbutton = Button(fourthframe, text="Hint", bg="DodgerBlue3", font=('Garuda', 10, 'bold'), width=18,
                                height=1, fg="mint cream", activebackground="mint cream",
                                activeforeground="DodgerBlue3", justify=CENTER, borderwidth=5
                                 , command= lambda : self.hints())
            compbutton = Button(fourthframe, text="Finish", bg="DodgerBlue3", font=('Garuda', 10, 'bold'), width=18,
                                 height=1, fg="mint cream", activebackground="mint cream",
                                 activeforeground="DodgerBlue3", justify=CENTER, borderwidth=5
                                , command= lambda : self.finish())

            fourthframe.pack(side=TOP, pady=5, padx=70, fill=BOTH)
            hinttbutton.pack(side=LEFT, padx=10)
            compbutton.pack(side=LEFT, padx=10)


            bottom_frame = Frame(root, bg="DodgerBlue3", height=50)
            copytight_label = Label(bottom_frame, text="© Moattar Usmani BAIM-F20-009", bg="DodgerBlue3",
                                    font=('Garuda', 10, 'bold'))
            bottom_frame.pack(side=BOTTOM, fill=BOTH)
            copytight_label.pack(pady=5)

        def hints(self):
            if(self.blank1entry.get()==""):
                messagebox.showinfo("Hint Adjective", "First letter C & similar word intrested", parent=self.root)

            elif (self.blank2entry.get() == ""):
                messagebox.showinfo("Hint Noun 1", "First letter M & derived from mother", parent=self.root)

            elif (self.blank3entry.get() == ""):
                messagebox.showinfo("Hint Verb", "First letter T & similar word rotate", parent=self.root)

            elif (self.blank4entry.get() == ""):
                messagebox.showinfo("Hint Noun 2", "First letter O & similar word moment or event", parent=self.root)

            elif (self.blank5entry.get() == ""):
                messagebox.showinfo("Hint Pronoun", "First letter Y & use to refer someone", parent=self.root)

            elif (self.blank6entry.get() == ""):
                messagebox.showinfo("Hint Noun 3", "First letter A & act of doing something", parent=self.root)

            elif (self.blank7entry.get() == ""):
                messagebox.showinfo("Hint Noun 4", "First letter H & thing we comb", parent=self.root)

            elif (self.blank8entry.get() == ""):
                messagebox.showinfo("Hint Adverb", "First letter I & definition: with no intention of causing harm", parent=self.root)

            else:
                messagebox.showinfo("No Hint", "All boxes are filled", parent=self.root)

        def finish(self):
            if(not(self.blank1entry.get() == "Curious" or self.blank1entry.get() == "curious" or self.blank1entry.get() == "CURIOUS")):
                messagebox.showerror("Wrong Adjective", "You lose, try again", parent=self.root)
                self.blank1entry.delete(0, END)

            elif(not (self.blank2entry.get() == "Mommy" or self.blank2entry.get() == "mommy" or self.blank2entry.get() == "MOMMY")):
                messagebox.showerror("Wrong Noun 1", "You lose, try again", parent=self.root)
                self.blank2entry.delete(0, END)

            elif(not(self.blank3entry.get() == "Turning" or self.blank3entry.get() == "turning" or self.blank3entry.get() == "TURNING")):
                messagebox.showerror("Wrong Verb", "You lose, try again", parent=self.root)
                self.blank3entry.delete(0, END)

            elif(not(self.blank4entry.get() == "Occasion" or self.blank4entry.get() == "occasion" or self.blank4entry.get() == "OCCASION")):
                messagebox.showerror("Wrong Noun 2", "You lose, try again", parent=self.root)
                self.blank4entry.delete(0, END)

            elif(not(self.blank5entry.get() == "You" or self.blank5entry.get() == "you" or self.blank5entry.get() == "YOU")):
                messagebox.showerror("Wrong Pronoun", "You lose, try again", parent=self.root)
                self.blank5entry.delete(0, END)

            elif(not(self.blank6entry.get() == "Action" or self.blank6entry.get() == "action" or self.blank6entry.get() == "ACTION")):
                messagebox.showerror("Wrong Noun 3", "You lose, try again", parent=self.root)
                self.blank6entry.delete(0, END)

            elif(not(self.blank7entry.get() == "Hair" or self.blank7entry.get() == "hair" or self.blank7entry.get() == "HAIR")):
                messagebox.showerror("Wrong Noun 4", "You lose, try again", parent=self.root)
                self.blank7entry.delete(0, END)

            elif(not(self.blank8entry.get() == "Innocently" or self.blank8entry.get() == "innocently" or self.blank8entry.get() == "INNOCENTLY")):
                messagebox.showerror("Wrong Adverb", "You lose, try again", parent=self.root)
                self.blank8entry.delete(0,END)

            else:
                messagebox.showinfo("WON!!!", "You Won the Game", parent=self.root)
                foradvlevel.makingfile()
                againmain(root)

    root = Tk()
    obj = gamelevel(root)
    mainloop()
