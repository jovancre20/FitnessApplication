from tkinter import *
from PIL import ImageTk
from tkVideoPlayer import TkinterVideo


root=Tk()
root.title('Login Page')
root.geometry('800x550+50+40')
root.resizable(0,0)
#root.geometry('990x560+50+40')

videoplayer= TkinterVideo(master=root, scaled=TRUE)
videoplayer.load(r"vidsam1.mp4")
videoplayer.pack(expand=TRUE, fill="both")

videoplayer.play()



root.mainloop()