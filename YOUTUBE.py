from tkinter import *
from turtle import position
from pytube import YouTube

root = Tk()
root.geometry('500x400')
root.resizable(0,0)
root.title("MY YOUTUBE DOWNLOADER")

Label(root,text= 'YOUTUBE DOWNLOADER', font= 'Helvetica 10 bold', activeforeground = 'yellow').pack()


link = StringVar()


Label(root, text= 'add link below:'.upper(), font='arial 10 bold').place(x=170, y=60)
link_enter = Entry(root, width = 70, textvariable=link).place(x=32,y=90)


def Downloader():

    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='downloaded sucessfully'.upper(), font='arial 10 italic', bg='white purple', )



Button(root, text='DOWNLOAD', font='Franklin 20 bold', bg='pale violet red',padx=3, command=Downloader).place(x=180, y=150)

root.mainloop()