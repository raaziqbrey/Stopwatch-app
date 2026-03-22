import time
import tkinter as tk
import math

class Stopwatch():
    def __init__(self):
        self.startTime = None
        self.elapsedTime = 0
        self.isRunning = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        self.root = tk.Tk()
        self.root.title("Stopwatch program")
        self.root.geometry("500x250")

        self.time_display = tk.Label(self.root, font=("Arial", 90), fg="#00FF00", bg= "Dark grey", text=f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}", width=7, height=1)
        self.time_display.grid(row=0, column=0, columnspan= 3)

        self.startButton = tk.Button(self.root, text="Start", fg="#b0b0b0", bg= "#004961", command=self.startStopWatch)
        self.startButton.grid(row=1, column=0)
 
        self.stopButton = tk.Button(self.root, text="Stop", fg="#b0b0b0", bg= "#004961", command=self.startStopWatch)
        self.stopButton.grid(row=1, column=1)
         
        self.resetButton = tk.Button(self.root, text="Reset", fg="#b0b0b0", bg= "#004961", command=self.resetWatch)
        self.resetButton.grid(row=1, column=2)

        self.root.bind("<space>", self.startStopWatch)
        self.root.bind("r", self.resetWatch)

        self.root.mainloop()

    
 
    def startStopWatch(self, event=None):
        if self.isRunning == False:
            self.startTime = time.time() - self.elapsedTime                                                                                                                                 
            self.isRunning = True

            self.root.after(1000, self.logWatchTime)
        else:
            self.isRunning = False
            self.root.after(1000, self.logWatchTime)

    def resetWatch(self, event=None):
        self.elapsedTime = 0
        self.isRunning = False
        self.time_display.config(text=f"{0:02}:{0:02}:{0:02}")
        self.startTime = None

    def logWatchTime(self):
        totalTime = self.elapsedTime
        if self.isRunning:
            totalTime = time.time() - self.startTime
            self.root.after(1000, self.logWatchTime)
        else:
            totalTime = self.elapsedTime

        self.hours = int(totalTime // 3600)
        self.minutes = int((totalTime % 3600) / 60)
        self.seconds = int(totalTime % 60)

        self.time_display.config(text=f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}")

stopwatch = Stopwatch()