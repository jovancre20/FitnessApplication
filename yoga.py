
import datetime
from tkinter import *
import tkinter as tk
#from tkinter import filedialog
from tkVideoPlayer import TkinterVideo
from tkinter import messagebox
import login_page as lp

#code for functions

def update_duration(event):
    """ updates the duration after finding the duration """
    duration = vid_player.video_info()["duration"]
    end_time["text"] = str(datetime.timedelta(seconds=duration))
    progress_slider["to"] = duration


def update_scale(event):
    """ updates the scale value """
    progress_value.set(vid_player.current_duration())


def load_video():
    """ loads the video """
    """file_path = filedialog.askopenfilename()

    if file_path:
        vid_player.load(file_path)

        progress_slider.config(to=0, from_=0)
        play_pause_btn["text"] = "Play"
        progress_value.set(0)"""
    
    vid_player.load("suryanamaskar.mp4")

    progress_slider.config(to=140, from_=20)
    play_pause_btn["text"] = "Play"
    progress_value.set(0)

def secondyoga():
    """ loads the video """
    vid_player.load("pranayam.mp4")

    progress_slider.config(to=0, from_=53)
    play_pause_btn["text"] = "Play"
    progress_value.set(0)

def thirdyoga():
    """ loads the video """
    vid_player.load("anulom.mp4")

    progress_slider.config(to=0, from_=100)
    play_pause_btn["text"] = "Play"
    progress_value.set(0)

def fourthyoga():
    """ loads the video """
    vid_player.load("vidsam1.mp4")

    progress_slider.config(to=0, from_=0)
    play_pause_btn["text"] = "Play"
    progress_value.set(0)

def fifthyoga():
    """ loads the video """
    vid_player.load("vidsam1.mp4")

    progress_slider.config(to=0, from_=0)
    play_pause_btn["text"] = "Play"
    progress_value.set(0)

def sixthyoga():
    """ loads the video """
    vid_player.load("vidsam1.mp4")

    progress_slider.config(to=12, from_=3)
    play_pause_btn["text"] = "Play"
    progress_value.set(0)

def seek(value):
    """ used to seek a specific timeframe """
    vid_player.seek(int(value))


def skip(value: int):
    """ skip seconds """
    vid_player.seek(int(progress_slider.get())+value)
    progress_value.set(progress_slider.get() + value)


def play_pause():
    #vid_player.load("vidsam1.mp4")

    #progress_slider.config(to=0, from_=0)
    #play_pause_btn["text"] = "Play"
    #progress_value.set(0)

    """ pauses and plays """
    if vid_player.is_paused():
        vid_player.play()
        play_pause_btn["text"] = "Pause"

    else:
        vid_player.pause()
        play_pause_btn["text"] = "Play"


def video_ended(event):
    """ handle video ended """
    progress_slider.set(progress_slider["to"])
    play_pause_btn["text"] = "Play"
    progress_slider.set(0)

def back_to_menu():
    root.destroy()

#code for gui

root = Toplevel(lp.window1)
#root = tk.Tk()
root.title("Yoga")
root.state("zoomed")

p1=PhotoImage(file='titlelogo.png')
root.iconphoto(False,p1)

title1=Label(root,text="Select your Yoga Exercise",font=("times new roman",18,"bold"),bd=5,relief=GROOVE,bg="chocolate1")
title1.pack(side=TOP,fill=X)

button1=Button(root, text="Surya Namaskar",width=20,height=1,command= load_video)
button1.place(x=10,y=40)

button2=Button(root, text="Pranayam",width=20,height=1, command=secondyoga)
button2.place(x=200,y=40)

button3=Button(root, text="Anuloam Viloam",width=20,height=1,command=thirdyoga)
button3.place(x=400,y=40)

#button4=Button(root, text="",width=20,height=1,command=fourthyoga)
#button4.place(x=600,y=0)

#button5=Button(root, text="Biceps",width=20,height=1, command=fifthyoga)
#button5.place(x=800,y=0)


load_btn = tk.Button(root, width=0, text="", command=fourthyoga, bd=0)
load_btn.pack()

vid_player = TkinterVideo(scaled=True, master=root)
vid_player.pack(expand=True, fill="both")

play_pause_btn = tk.Button(root, text="Play", command=play_pause)
play_pause_btn.pack()

skip_plus_5sec = tk.Button(root, text="Skip -5 sec", command=lambda: skip(-5))
skip_plus_5sec.pack(side="left")

start_time = tk.Label(root, text=str(datetime.timedelta(seconds=0)))
start_time.pack(side="left")

progress_value = tk.IntVar(root)
    
progress_slider = tk.Scale(root, variable=progress_value, from_=0, to=0, orient="horizontal", command=seek)
# progress_slider.bind("<ButtonRelease-1>", seek)
progress_slider.pack(side="left", fill="x", expand=True)

end_time = tk.Label(root, text=str(datetime.timedelta(seconds=0)))
end_time.pack(side="left")

vid_player.bind("<<Duration>>", update_duration)
vid_player.bind("<<SecondChanged>>", update_scale)
vid_player.bind("<<Ended>>", video_ended )

skip_plus_5sec = tk.Button(root, text="Skip +5 sec", command=lambda: skip(5))
skip_plus_5sec.pack(side="left")

button7=Button(root, text="MainMenu",width=10,height=2, command=back_to_menu)
button7.pack()
#button7.place(x=10,y=500)

root.mainloop()

