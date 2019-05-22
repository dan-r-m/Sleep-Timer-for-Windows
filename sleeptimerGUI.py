from tkinter import *
import os

HEIGHT = 600
WIDTH = 600
after = None
BackgroundColor = "white"
UserEntryColor = "#80C1FF"
ClockBackgroundColor="#80C1FF"
ClockColor = "white"

def cancelCountdown():
    global after
    timer = False
    clockDisplay.config(text="00:00")
    clockDisplay.after_cancel(after)
    #print("Countdown cancelled.")

    
def calcTime(seconds):
    minutes = int(seconds) / 60
    seconds = int(seconds) % 60
    minutes = int(minutes)
    seconds = int(seconds)
    return str(minutes)+":"+str(seconds)
    
def shutdownProc():
    print("Shutting down...")
    os.system("shutdown /s")


def updateTime(seconds):
    global after
    if seconds==0:
        shutdownProc()
    else:
        seconds = int(seconds)-1
        clockDisplay.config(text=calcTime(seconds))
        #print(calcTime(seconds))
        after = clockDisplay.after(1000, updateTime, seconds)


def submitMinutes(minutes):
    seconds = int(minutes) * 60
    clockDisplay.config(text=calcTime(seconds))
    #print("this is the time left:\n", calcTime(seconds))
    updateTime(seconds)


root = Tk()


canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frameMain = Frame(root, bg=BackgroundColor, height=HEIGHT, width=WIDTH)
frameMain.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)


#user entry frame area
frameUpper = Frame(frameMain, bg=UserEntryColor)
frameUpper.place(anchor=N, relx=0.5, rely=0.1, relwidth=0.75, relheight=0.4)

label = Label(frameUpper, bg=UserEntryColor, text="Minutes until shutdown: ")
label.place(anchor=N, relx=0.3, rely=0.2, relwidth=0.4, relheight=0.2)

entry = Entry(frameUpper, bd=5)
entry.place(anchor=N, relx=0.7, rely=0.2, relwidth=0.4, relheight=0.2)

button = Button(frameUpper, text="Submit", command=lambda: submitMinutes(entry.get()))
button.place(anchor=N, relx=0.35, rely=0.6, relwidth=0.3, relheight=0.2)

cancelButton = Button(frameUpper, text="Cancel", command=cancelCountdown)
cancelButton.place(anchor=N, relx=0.7, rely=0.6, relwidth=0.3, relheight=0.2)


#clock frame area
frameLower = Frame(frameMain, bg=ClockBackgroundColor)
frameLower.place(anchor=N, relx=0.5, rely=0.5, relwidth=0.75, relheight=0.35)

clockLabel = Label(frameLower, bg=ClockColor, text="Time Until Shutdown: ")
clockLabel.place(anchor = N, relx=0.5, rely=0.2, relwidth=0.4, relheight=0.2)

clockDisplay = Label(frameLower, bg=ClockColor, text="00:00")
clockDisplay.place(anchor = N, relx=0.5, rely=0.4, relwidth=0.4, relheight=0.4)


root.mainloop()
