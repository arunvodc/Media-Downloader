##__author__ = 'Arun'

import pafy
import string
from tkinter import *
from tkinter.filedialog import askdirectory

downVal = 0
glob = 0
link = ""
filepath = ""

def pipe():
    global link
    link = url.get()
    Label(root,text="",bg="white",height=50,width=500).place(x=0,y=325)
    if link is not "":
        obj = select(root)
        obj.downType()

def pipe_sel():
    def directory():
        global filepath
        filepath = askdirectory()
        Label(root,text="",compound=CENTER,width=500,bg="white").place(x=360,y=400)
        Label(root,text=filepath,compound=CENTER,fg="black").place(x=360,y=400) #------------------------------------------------
    Label(root,text="",bg="white",height=50,width=500).place(x=0,y=320)
    obj = download(root)
    print(glob)
    Label(root,text="",bg="white",height=50,width=500).place(x=0,y=325)
    if glob == 1:
        obj.video()
    elif glob == 2:
        obj.vOnly()
    elif glob == 3:
        obj.aOnly()
    else:
        a=1
    Label(root,text="Choose destination directory",bg="white",fg="black").place(x=370,y=335)
    global fpath
    fpath = Button(root,text="Browse",width = 10,command=directory).place(x=411,y=360)

class select(Frame):
    def _init_(self):
        Frame.__init__(self)

    def downType(self):
        var = IntVar()
        def sel():
            global glob
            glob = var.get()


        Label(root,text="Select Type",compound=LEFT,fg="black",bg="white").place(x=30,y=325)
        Radiobutton(root,text="Video: Normal",variable=var,compound=CENTER,command=sel,value=1,bg="white").place(x=30,y=350)
        Radiobutton(root,text="Video Only",variable=var,compound=CENTER,command=sel,value=2,bg="white").place(x=30,y=380)
        Radiobutton(root,text="Audio Only",variable=var,compound=CENTER,command=sel,value=3,bg="white").place(x=30,y=410)
        downloadButton = Button(root, text = 'Select', width = 10, command = pipe_sel).place(x=411,y=440)

class download(Frame):
        def video(self):
            def callback2():
                array[opt].download(filepath)
            down = pafy.new(link)
            array = down.streams
            var2 = IntVar()
            Label(root,text="Select media quality",compound=LEFT,fg="black",bg="white").place(x=30,y=325)
            c = -1
            for res in array:
                c=c+1
                string = str(res)
                res_text = string[string.index(':')+1:string.index('@')].upper()+"-"+string[string.index('@')+1:]
                Radiobutton(root,text=res_text,variable=var2,value=c,bg="white").place(x=30,y=350+c*30)
            c=c+1
            opt = 3
            downloadButton = Button(root, text = 'Download', width = 10, command = callback2).place(x=411,y=350+c*30)

        def vOnly(self):
            def callback2():
                array[opt].download(filepath)
            down = pafy.new(link)
            array = down.videostreams
            var2 = IntVar()
            Label(root,text="Select media quality",compound=LEFT,fg="black",bg="white").place(x=30,y=325)
            c = -1
            for res in array:
                c=c+1
                string = str(res)
                res_text = string[string.index(':')+1:string.index('@')].upper()+"-"+string[string.index('@')+1:]
                Radiobutton(root,text=res_text,variable=var2,value=c,bg="white").place(x=30,y=350+c*30)
            c=c+1
            opt = 3
            downloadButton = Button(root, text = 'Download', width = 10, command = callback2).place(x=411,y=350+c*30)

        def aOnly(self):
            def callback2():
                array[opt].download(filepath)
            down = pafy.new(link)
            array = down.audiostreams
            var2 = IntVar()
            Label(root,text="Select media quality",compound=LEFT,fg="black",bg="white").place(x=30,y=325)
            c = -1
            for res in array:
                c=c+1
                string = str(res)
                res_text = string[string.index(':')+1:string.index('@')].upper()+"-"+string[string.index('@')+1:]
                Radiobutton(root,text=res_text,variable=var2,value=c,bg="white").place(x=350,y=350+c*30)
            c=c+1
            opt = 3
            downloadButton = Button(root, text = 'Download', width = 10, command = callback2).place(x=411,y=350+c*30)

root = Tk()
root.wm_title("myTubeVids")
root.minsize(width=900,height=600)
root.maxsize(width=900,height=1200)
root.configure(background='white')
logo = PhotoImage(file = "C:/Users/Arun/Documents/Python/myTubeVids/Logo/MyTubeVids_Logo.gif")
# till aobve, integrated
Label(root, compound = CENTER, width = 270, height = 220, image = logo).pack()

Label(root, compound = CENTER, text = "\nPaste YouTube Link below\n", background = 'white').pack()

url = Entry(root, width = 60)
url.pack()
url.focus_set()

searchButton = Button(root, text = 'Search', width = 10, command = pipe).pack()

root.mainloop()
