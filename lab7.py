from copyreg import pickle
from tkinter import *
from tkinter import messagebox
import time
import picamera
import RPi.GPIO as GPIO

camera = picamera.PiCamera()

redPin = 37
greenPin = 40
bluePin = 38

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)
GPIO.output(redPin, GPIO.LOW)
GPIO.output(greenPin, GPIO.LOW)
GPIO.output(bluePin, GPIO.LOW)


HEIGHT = 1016
WIDTH = 720

pi = Tk()
pi.geometry("1016x720")
pi.resizable(False, False)
pi.configure(background='#FFFFFF')

pi.title("Lab #7")
fram1 = Frame(pi,bg='#FFFFFF', bd=5)
fram1.place(relx=0.1, rely=0.1, relwidth=0.15, relheight=0.7, anchor='n')
offLabel = Label(fram1, bg='#FFFFFF', text="OFF", font=("Times New Roman", 20))
offLabel.place(relx=0.5, rely=0.1, relwidth=0.35, relheight=0.18, anchor='n')
dimLabel = Label(fram1, bg='#FFFFFF', text="DIM", font=("Times New Roman", 20))
dimLabel.place(relx=0.5, rely=0.3, relwidth=0.35, relheight=0.18, anchor='n')
flashLabel = Label(fram1, bg='#FFFFFF', text="FLASH", font=("Times New Roman", 20))
flashLabel.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.18, anchor='n')
onLabel = Label(fram1, bg='#FFFFFF', text="ON", font=("Times New Roman", 20))
onLabel.place(relx=0.5, rely=0.7, relwidth=0.35, relheight=0.18, anchor='n')


fram2 = Frame(pi,bg='#FFFFFF', bd=5)
fram2.place(relx=0.5, rely=0.01, relwidth=0.5, relheight=0.15, anchor='n')
redLabel = Label(fram2, bg='#FFFFFF', text="RED", font=("Times New Roman", 20))
redLabel.place(relx=0.2, rely=0.3, relwidth=0.55, relheight=0.18, anchor='n')
greenLabel = Label(fram2, bg='#FFFFFF', text="GREEN", font=("Times New Roman", 20))
greenLabel.place(relx=0.5, rely=0.3, relwidth=0.45, relheight=0.18, anchor='n')
blueLabel = Label(fram2, bg='#FFFFFF', text="BLUE", font=("Times New Roman", 20))
blueLabel.place(relx=0.8, rely=0.3, relwidth=0.4, relheight=0.18, anchor='n')

buttons = Frame(pi,bg='#FFFFFF', bd=5)
buttons.place(relx=0.5, rely=0.18, relwidth=0.5, relheight=0.60, anchor='n')
redOff = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: redData(1))
redOff.place(relx=0.2, rely=0.01, relwidth=0.15, relheight=0.18, anchor='n')
redDim = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: redData(2))
redDim.place(relx=0.2, rely=0.23, relwidth=0.15, relheight=0.18, anchor='n')
redFlash = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: redData(3))
redFlash.place(relx=0.2, rely=0.47, relwidth=0.15, relheight=0.18, anchor='n')
redOn = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: redData(4))
redOn.place(relx=0.2, rely=0.7, relwidth=0.15, relheight=0.18, anchor='n')
greenOff = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: greenData(1))
greenOff.place(relx=0.5, rely=0.01, relwidth=0.15, relheight=0.18, anchor='n')
greenDim = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: greenData(2))
greenDim.place(relx=0.5, rely=0.23, relwidth=0.15, relheight=0.18, anchor='n')
greenFlash = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: greenData(3))
greenFlash.place(relx=0.5, rely=0.47, relwidth=0.15, relheight=0.18, anchor='n')
greenOn = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: greenData(4))
greenOn.place(relx=0.5, rely=0.7, relwidth=0.15, relheight=0.18, anchor='n')
blueOff = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: blueData(1))
blueOff.place(relx=0.8, rely=0.01, relwidth=0.15, relheight=0.18, anchor='n')
blueDim = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: blueData(2))
blueDim.place(relx=0.8, rely=0.23, relwidth=0.15, relheight=0.18, anchor='n')
blueFlash = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: blueData(3))
blueFlash.place(relx=0.8, rely=0.47, relwidth=0.15, relheight=0.18, anchor='n')
blueOn = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: blueData(4))
blueOn.place(relx=0.8, rely=0.7, relwidth=0.15, relheight=0.18, anchor='n')

rotationFrame = Frame(pi,bg='#FFFFFF', bd=5)
rotationFrame.place(relx=0.9, rely=0.01, relwidth=0.15, relheight=0.18, anchor='n')
rotationLabel = Label(rotationFrame, bg='#FFFFFF', text="Rotation", font=("Times New Roman", 20))
rotationLabel.place(relx=0.2, rely=0.2, relwidth=0.65, relheight=0.3)

cameraFrame = Frame(pi,bg='#FFFFFF', bd=5)
cameraFrame.place(relx=0.9, rely=0.2, relwidth=0.15, relheight=0.45, anchor='n')
cameraLabel = Label(cameraFrame, bg='#FFFFFF', text="Camera", font=("Times New Roman", 20))
cameraLabel.place(relx=0.2, rely=0.05, relwidth=0.65, relheight=0.3)

exitFrame = Frame(pi,bg='#FFFFFF', bd=5)
exitFrame.place(relx=0.9, rely=0.7, relwidth=0.15, relheight=0.18, anchor='n')

rotationText = Text(rotationFrame, bg='#FFFFFF', height=4, width=5, font=("Times New Roman", 15))
rotationText.place(relx=0.2, rely=0.5, relwidth=0.65, relheight=0.3)
startButton = Button(cameraFrame, padx=40, pady=20, text="Start", font=("Times New Roman", 15), command=lambda: displayData(1))
startButton.place(relx=0.2, rely=0.35, relwidth=0.65, relheight=0.2)
stopButton = Button(cameraFrame, padx=40, pady=20, text="Stop", font=("Times New Roman", 15), command=lambda: displayData(2))
stopButton.place(relx=0.2, rely=0.65, relwidth=0.65, relheight=0.2)
exitButton = Button(exitFrame, padx=40, pady=20, text="Exit", font=("Times New Roman", 15), command=lambda: displayData(3))
exitButton.place(relx=0.2, rely=0.15, relwidth=0.65, relheight=0.6)


r = GPIO.PWM(redPin, 1000)
g = GPIO.PWM(greenPin, 1000)
b = GPIO.PWM(bluePin, 1000)

def redData(val):
    if val == 1:
        r.stop()
        redOff = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="Green", command=lambda: redData(1))
        redOff.place(relx=0.2, rely=0.01, relwidth=0.15, relheight=0.18, anchor='n')
        redDim = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: redData(2))
        redDim.place(relx=0.2, rely=0.23, relwidth=0.15, relheight=0.18, anchor='n')
        redFlash = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: redData(3))
        redFlash.place(relx=0.2, rely=0.47, relwidth=0.15, relheight=0.18, anchor='n')
        redOn = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: redData(4))
        redOn.place(relx=0.2, rely=0.7, relwidth=0.15, relheight=0.18, anchor='n')
    elif val == 2:
        r.start(100)
        r.ChangeFrequency(100)
        r.ChangeDutyCycle(10)
        redOff = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: redData(1))
        redOff.place(relx=0.2, rely=0.01, relwidth=0.15, relheight=0.18, anchor='n')
        redDim = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="Green", command=lambda: redData(2))
        redDim.place(relx=0.2, rely=0.23, relwidth=0.15, relheight=0.18, anchor='n')
        redFlash = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: redData(3))
        redFlash.place(relx=0.2, rely=0.47, relwidth=0.15, relheight=0.18, anchor='n')
        redOn = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: redData(4))
        redOn.place(relx=0.2, rely=0.7, relwidth=0.15, relheight=0.18, anchor='n')
    elif val == 3:
        r.start(100)
        r.ChangeFrequency(1)
        r.ChangeDutyCycle(50)
        redOff = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: redData(1))
        redOff.place(relx=0.2, rely=0.01, relwidth=0.15, relheight=0.18, anchor='n')
        redDim = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: redData(2))
        redDim.place(relx=0.2, rely=0.23, relwidth=0.15, relheight=0.18, anchor='n')
        redFlash = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="Green", command=lambda: redData(3))
        redFlash.place(relx=0.2, rely=0.47, relwidth=0.15, relheight=0.18, anchor='n')
        redOn = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: redData(4))
        redOn.place(relx=0.2, rely=0.7, relwidth=0.15, relheight=0.18, anchor='n')
    elif val == 4:
        r.start(100)
        redOff = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: redData(1))
        redOff.place(relx=0.2, rely=0.01, relwidth=0.15, relheight=0.18, anchor='n')
        redDim = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: redData(2))
        redDim.place(relx=0.2, rely=0.23, relwidth=0.15, relheight=0.18, anchor='n')
        redFlash = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: redData(3))
        redFlash.place(relx=0.2, rely=0.47, relwidth=0.15, relheight=0.18, anchor='n')
        redOn = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="Green", command=lambda: redData(4))
        redOn.place(relx=0.2, rely=0.7, relwidth=0.15, relheight=0.18, anchor='n')

def greenData(val):
    if val == 1:
        g.stop()
        greenOff = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="Green", command=lambda: greenData(1))
        greenOff.place(relx=0.5, rely=0.01, relwidth=0.15, relheight=0.18, anchor='n')
        greenDim = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: greenData(2))
        greenDim.place(relx=0.5, rely=0.23, relwidth=0.15, relheight=0.18, anchor='n')
        greenFlash = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: greenData(3))
        greenFlash.place(relx=0.5, rely=0.47, relwidth=0.15, relheight=0.18, anchor='n')
        greenOn = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: greenData(4))
        greenOn.place(relx=0.5, rely=0.7, relwidth=0.15, relheight=0.18, anchor='n')

    elif val == 2:
        g.start(100)
        g.ChangeFrequency(100)
        g.ChangeDutyCycle(10)
        greenOff = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: greenData(1))
        greenOff.place(relx=0.5, rely=0.01, relwidth=0.15, relheight=0.18, anchor='n')
        greenDim = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="Green", command=lambda: greenData(2))
        greenDim.place(relx=0.5, rely=0.23, relwidth=0.15, relheight=0.18, anchor='n')
        greenFlash = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: greenData(3))
        greenFlash.place(relx=0.5, rely=0.47, relwidth=0.15, relheight=0.18, anchor='n')
        greenOn = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: greenData(4))
        greenOn.place(relx=0.5, rely=0.7, relwidth=0.15, relheight=0.18, anchor='n')

    elif val == 3:
        g.start(100)
        g.ChangeFrequency(1)
        g.ChangeDutyCycle(50)
        greenOff = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: greenData(1))
        greenOff.place(relx=0.5, rely=0.01, relwidth=0.15, relheight=0.18, anchor='n')
        greenDim = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: greenData(2))
        greenDim.place(relx=0.5, rely=0.23, relwidth=0.15, relheight=0.18, anchor='n')
        greenFlash = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="Green", command=lambda: greenData(3))
        greenFlash.place(relx=0.5, rely=0.47, relwidth=0.15, relheight=0.18, anchor='n')
        greenOn = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: greenData(4))
        greenOn.place(relx=0.5, rely=0.7, relwidth=0.15, relheight=0.18, anchor='n')

    elif val == 4:
        g.start(100)
        greenOff = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: greenData(1))
        greenOff.place(relx=0.5, rely=0.01, relwidth=0.15, relheight=0.18, anchor='n')
        greenDim = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: greenData(2))
        greenDim.place(relx=0.5, rely=0.23, relwidth=0.15, relheight=0.18, anchor='n')
        greenFlash = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: greenData(3))
        greenFlash.place(relx=0.5, rely=0.47, relwidth=0.15, relheight=0.18, anchor='n')
        greenOn = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="Green", command=lambda: greenData(4))
        greenOn.place(relx=0.5, rely=0.7, relwidth=0.15, relheight=0.18, anchor='n')


def blueData(val):
    if val == 1:
        b.stop()
        blueOff = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="Blue", command=lambda: blueData(1))
        blueOff.place(relx=0.8, rely=0.01, relwidth=0.15, relheight=0.18, anchor='n')
        blueDim = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: blueData(2))
        blueDim.place(relx=0.8, rely=0.23, relwidth=0.15, relheight=0.18, anchor='n')
        blueFlash = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: blueData(3))
        blueFlash.place(relx=0.8, rely=0.47, relwidth=0.15, relheight=0.18, anchor='n')
        blueOn = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: blueData(4))
        blueOn.place(relx=0.8, rely=0.7, relwidth=0.15, relheight=0.18, anchor='n')
    elif val == 2:
        b.start(100)
        b.ChangeFrequency(100)
        b.ChangeDutyCycle(10)
        blueOff = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: blueData(1))
        blueOff.place(relx=0.8, rely=0.01, relwidth=0.15, relheight=0.18, anchor='n')
        blueDim = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="Green", command=lambda: blueData(2))
        blueDim.place(relx=0.8, rely=0.23, relwidth=0.15, relheight=0.18, anchor='n')
        blueFlash = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: blueData(3))
        blueFlash.place(relx=0.8, rely=0.47, relwidth=0.15, relheight=0.18, anchor='n')
        blueOn = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: blueData(4))
        blueOn.place(relx=0.8, rely=0.7, relwidth=0.15, relheight=0.18, anchor='n')
    elif val == 3:
        b.start(100)
        b.ChangeFrequency(1)
        b.ChangeDutyCycle(50)
        blueOff = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: blueData(1))
        blueOff.place(relx=0.8, rely=0.01, relwidth=0.15, relheight=0.18, anchor='n')
        blueDim = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: blueData(2))
        blueDim.place(relx=0.8, rely=0.23, relwidth=0.15, relheight=0.18, anchor='n')
        blueFlash = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="Green", command=lambda: blueData(3))
        blueFlash.place(relx=0.8, rely=0.47, relwidth=0.15, relheight=0.18, anchor='n')
        blueOn = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: blueData(4))
        blueOn.place(relx=0.8, rely=0.7, relwidth=0.15, relheight=0.18, anchor='n')
    elif val == 4:
        b.start(100)
        blueOff = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: blueData(1))
        blueOff.place(relx=0.8, rely=0.01, relwidth=0.15, relheight=0.18, anchor='n')
        blueDim = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: blueData(2))
        blueDim.place(relx=0.8, rely=0.23, relwidth=0.15, relheight=0.18, anchor='n')
        blueFlash = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="White", command=lambda: blueData(3))
        blueFlash.place(relx=0.8, rely=0.47, relwidth=0.15, relheight=0.18, anchor='n')
        blueOn = Radiobutton(buttons, padx=10, pady=10, bg='#FFFFFF', selectcolor="Green", command=lambda: blueData(4))
        blueOn.place(relx=0.8, rely=0.7, relwidth=0.15, relheight=0.18, anchor='n')

def getInput():
    inp = rotationText.get("1.0", "end-1c")
    return inp

def displayData(val):
    if (val == 1):
        camera.rotation = getInput()
        if(camera.previewing):
            print("A preview window is already open. Close it first by pressing STOP.")
        else:
            camera.start_preview(fullscreen=False, window=(100,200,1016,720))
    elif (val == 2):
        camera.stop_preview()
        count = 0
    elif (val == 3):
        camera.stop_preview()
        pi.quit()
        pi.destroy()
    return
    
try:
    while True:
        pi.mainloop()
except KeyboardInterrupt:
    print("Lab 4 is done. BYE.")
    camera.stop_preview()
    pi.quit()
    pi.destroy()    