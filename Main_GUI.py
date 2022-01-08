from tkinter import *
from PIL import ImageTk, Image
from OtherGUI import *

def maingui():
    class welcome:
        def __init__(self, root):
            self.root = root
            root.geometry("300x450")
            root.maxsize(300,450)
            root.minsize(300,450)
            root.iconbitmap('image.ico')
            root.title("madlibs - Home Page")
            root.configure(bg="sky blue")

            topframe = Frame(root, bg="gray92", height=60)
            headinglabel = Label(topframe, bg="gray92", text="Madlibs Games", font=("arial",18,"bold"), justify=CENTER)

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

            contlabel = Label(root, text="Press continue to play game......", bg="sky blue", font=('Garuda',8))
            contlabel.pack(side=TOP,padx=20)

            bottom_frame = Frame(root, bg="DodgerBlue3", height=50)
            copytight_label = Label(bottom_frame, text="© Moattar Usmani BAIM-F20-009", bg="DodgerBlue3",
                                    font=('Garuda', 10, 'bold'))
            bottom_frame.pack(side=BOTTOM, fill=BOTH)
            copytight_label.pack(pady=5)







    root = Tk()
    obj = welcome(root)
    mainloop()


maingui()
