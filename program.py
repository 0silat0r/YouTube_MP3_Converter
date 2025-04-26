import os
import tkinter
from tkinter import *
from pytube import YouTube
from PIL import Image, ImageTk

def mp3_converter():
    print("Lütfen bekleyin kurulum başlatılıyor...")
    link = t1.get(1.0,"end-1c")
    path = "Downloads/"
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download(path)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(f"{yt.title} Başariyla Indirildi!")
    print("Indirilen müziği Downloads klasörünün içinde bulabilirsiniz.")
    t1.delete("1.0","end")

program = tkinter.Tk()
program.geometry("330x280")
program.title("YouTube MP3 Converter")

img = Image.open("pictures/mp3_logo.jpg")
resize_img = img.resize((165,140))
img2 = ImageTk.PhotoImage(resize_img)
img_lbl = Label(image=img2)
img_lbl.image = img2
img_lbl.pack()

l1 = Label(program, text="Video Source Link")
l1.pack()
t1 = Text(program, width=38, height=1)
t1.pack()
b1 = Button(program, text="Convert To MP3",command=mp3_converter)
b1.pack()
b2 = Button(program, text="Quit",command=program.destroy)
b2.pack()

l2 = Label(program, text='Programming by 0silat0r')
l2.pack()
program.mainloop()
