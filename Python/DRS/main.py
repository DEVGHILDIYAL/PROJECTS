import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import time
import imutils

SET_WIDTH = 650
SET_HEIGHT = 368

window = tkinter.Tk()
window.title("Decision Review System")
cv_image = cv2.cvtColor(cv2.imread("images/welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_image))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()

stream = cv2.VideoCapture("images/clip.mp4")
flag = True
def play(speed):
    global flag
    print(f"Speed is : {speed}")

    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(132, 26, fill='black', font="Times 26 bold", text="Decision Pending")
    flag = not flag
def pending(decision):
    # 1. DIsplay decision pending Image
    frame = cv2.cvtColor(cv2.imread("images/pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    # 2. Wait for 1 sec
    time.sleep(1)

    # 3. Display sponser image
    frame = cv2.cvtColor(cv2.imread("images/sponsor.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    # 4. Wait for 1.5 second
    time.sleep(1.5)

    # 5. Display out/not out image
    if decision == 'out':
        decisionImg = "images/out.png"
    elif decision == 'not out':
        decisionImg = "images/not_out.png"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is OUT")

def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is NOT OUT")

#BUTTONS
btn = tkinter.Button(window, text="<< Previous (fast)", width=50, command=partial(play, -15))
btn.pack()

btn = tkinter.Button(window, text="<< Previous (slow)", width=50, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="Next (fast) >>", width=50, command=partial(play, 15))
btn.pack()

btn = tkinter.Button(window, text="Next (slow) >>", width=50, command=partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text="Give Out", width=50, command=out)
btn.pack()

btn = tkinter.Button(window, text="Give Not Out", width=50, command=not_out)
btn.pack()

window.mainloop()