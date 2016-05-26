from tkinter import *
from tkinter import ttk
from random import randint
import time

class mainWindow():
    def __init__(self):
        self.root = Tk()
        self.root.title("Translator Quiz")

        self.questionslist = [
        {"pinyin": "ni hao", "english": "hello"},
        {"pinyin": "bai bai", "english": "bye bye"},
        {"pinyin": "xie-xie", "english": "thanks"}
        ]

        self.highestindex = len(self.questionslist)
        self.currentquestion = randint(0,self.highestindex-1)
        self.questionnumber = 1

    def resetScore(self):
        self.answercorrect = 0
        self.answerwrong = 0

    def testanswer(self, caller):
        submittedanswer = self.translatedanswer.get()

        if submittedanswer.lower() == self.questionslist[self.currentquestion]["english"]:
            self.answercorrect += 1
        else:
            self.answerwrong += 1

        self.currentquestion = randint(0,self.highestindex-1)

        if caller == "excercise":
            self.exerciseframe.destroy()
            self.exerciseTest()
        elif caller == "timetest":
            global endtimer
            endtimer = time.time()
            if self.questionnumber < 20:
                self.questionnumber += 1
                self.timedTestframe.destroy()
                self.timedTest()
            else:
                self.timedTestframe.destroy()
                self.scorescreen()



    def mainmenu(self):
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        label = ttk.Label(self.mainframe, text="Please select a mode to start you exercise.", font=("Arial", 15))
        label.grid(column=0, row=0, columnspan=3, sticky=(E))

        modeonebutton = ttk.Button(self.mainframe, text="Exercise", command=self.startExerciseTest)
        modetwobutton = ttk.Button(self.mainframe, text="Timed test", command=self.startTimedTest)
        aboutbutton = ttk.Button(self.mainframe, text="About", command=self.abouttranslator)

        modeonebutton.grid(column=1, row=1)
        modetwobutton.grid(column=1, row=2)
        aboutbutton.grid(column=2, row=3)

        self.root.mainloop()

    def startExerciseTest(self):
        self.mainframe.destroy()
        self.resetScore()
        self.exerciseTest()

    def startTimedTest(self):
        self.mainframe.destroy()
        self.resetScore()

        global starttimer
        starttimer = time.time()

        global endtimer
        endtimer = time.time()

        self.timedTest()

    def stopExercise(self):
        self.exerciseframe.destroy()
        self.mainmenu()

    def exitscorescreen(self):
        self.questionnumber = 0
        self.scorescreenframe.destroy()
        self.mainmenu()

    def exerciseTest(self):

        self.exerciseframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.exerciseframe.grid(column=0, row=0, sticky=(N,W,E,S))
        self.exerciseframe.columnconfigure(0, weight=1)
        self.exerciseframe.rowconfigure(0, weight=1)

        exerciselabel1 = ttk.Label(self.exerciseframe, text="Translate:", font=("Arial", 20))
        exerciselabel1.grid(column=0,row=0,sticky=(W))

        exerciselabel2 = ttk.Label(self.exerciseframe, text=self.questionslist[self.currentquestion]["pinyin"], font=("Arial", 25))
        exerciselabel2.grid(column=1,row=0,sticky=(N))

        exerciselabelcorrectanswers = ttk.Label(self.exerciseframe, text="Correct answers: "+str(self.answercorrect), font=("Arial", 10))
        exerciselabelcorrectanswers.grid(column=0,row=3)

        exerciselabelwronganswers = ttk.Label(self.exerciseframe, text="Wrong answers: "+str(self.answerwrong), font=("Arial", 10))
        exerciselabelwronganswers.grid(column=0,row=4)

        self.translatedanswer = ttk.Entry(self.exerciseframe)
        self.translatedanswer.grid(column=1,row=1)

        exercisebutton1 = ttk.Button(self.exerciseframe, text="Submit", command= lambda: self.testanswer("excercise"))
        exercisebutton1.grid(column=2,row=3)

        exercisebutton2 = ttk.Button(self.exerciseframe, text="Quit", command=self.stopExercise)
        exercisebutton2.grid(column=2,row=4)


        self.root.mainloop()


    def timedTest(self):

        self.timedTestframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.timedTestframe.grid(column=0, row=0, sticky=(N,W,E,S))
        self.timedTestframe.columnconfigure(0, weight=1)
        self.timedTestframe.rowconfigure(0, weight=1)

        timedTestlabel1 = ttk.Label(self.timedTestframe, text="#"+str(self.questionnumber)+" of 20", font=("Arial", 20))
        timedTestlabel1.grid(column=0,row=0,sticky=(W))

        timedTestlabel2 = ttk.Label(self.timedTestframe, text=self.questionslist[self.currentquestion]["pinyin"], font=("Arial", 25))
        timedTestlabel2.grid(column=1,row=0,sticky=(N))

        timedTestlabelcorrectanswers = ttk.Label(self.timedTestframe, text="Correct answers: "+str(self.answercorrect), font=("Arial", 10))
        timedTestlabelcorrectanswers.grid(column=0,row=3)

        exerciselabelwronganswers = ttk.Label(self.timedTestframe, text="Wrong answers: "+str(self.answerwrong), font=("Arial", 10))
        exerciselabelwronganswers.grid(column=0,row=4)

        self.translatedanswer = ttk.Entry(self.timedTestframe)
        self.translatedanswer.grid(column=1,row=1)

        timedTestbutton1 = ttk.Button(self.timedTestframe, text="Submit", command= lambda: self.testanswer("timetest"))
        timedTestbutton1.grid(column=2,row=3)

        timedTestbutton2 = ttk.Button(self.timedTestframe, text="Quit", command=self.scorescreen)
        timedTestbutton2.grid(column=2,row=4)


        self.root.mainloop()

    def abouttranslator(self):
        print("About this program")

    def scorescreen(self):
        timervalue = (endtimer - starttimer)

        self.scorescreenframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.scorescreenframe.grid(column=0, row=0, sticky=(N,W,E,S))
        self.scorescreenframe.columnconfigure(0, weight=1)
        self.scorescreenframe.rowconfigure(0, weight=1)

        scorelabel1 = ttk.Label(self.scorescreenframe, text="Correct answers: ", font=("Arial", 15), anchor=E, width=15)
        scorelabel1.grid(column=0,row=0)

        scorelabel1 = ttk.Label(self.scorescreenframe, text=self.answercorrect, font=("Arial", 20), anchor=CENTER, width=5, foreground="green")
        scorelabel1.grid(column=1,row=0)

        scorelabel1 = ttk.Label(self.scorescreenframe, text="Wrong answers: ", font=("Arial", 15), anchor=E, width=15)
        scorelabel1.grid(column=0,row=1)

        scorelabel1 = ttk.Label(self.scorescreenframe, text=self.answerwrong, font=("Arial", 20), anchor=CENTER, width=5, foreground="red")
        scorelabel1.grid(column=1,row=1, sticky=(W))

        scorelabel1 = ttk.Label(self.scorescreenframe, text="Total time: ", font=("Arial", 15), anchor=E, width=15)
        scorelabel1.grid(column=0,row=2)

        scorelabel1 = ttk.Label(self.scorescreenframe, text=str(int(timervalue))+" sec", font=("Arial", 20), anchor=CENTER, width=5)
        scorelabel1.grid(column=1,row=2, sticky=(W))

        scorelabel1 = ttk.Label(self.scorescreenframe, text="Avg time per question: ", font=("Arial", 15), anchor=E, width=15)
        scorelabel1.grid(column=0,row=3)

        scorelabel1 = ttk.Label(self.scorescreenframe, text=str(int(timervalue/self.questionnumber))+" sec", font=("Arial", 20), anchor=CENTER, width=5)
        scorelabel1.grid(column=1,row=3, sticky=(W))

        scorelabel1 = ttk.Label(self.scorescreenframe, text="Questions tried: ", font=("Arial", 15), anchor=E, width=15)
        scorelabel1.grid(column=0,row=4)

        scorelabel1 = ttk.Label(self.scorescreenframe, text=str(self.questionnumber), font=("Arial", 20), anchor=CENTER, width=5)
        scorelabel1.grid(column=1,row=4, sticky=(W))

        scorebutton = ttk.Button(self.scorescreenframe, text="Mainmenu", command=self.exitscorescreen, width=15)
        scorebutton.grid(column=2,row=5)

start = mainWindow()
start.mainmenu()
