from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import pygame
import datetime
import time


def set():
    global t
    rem=sd.askstring("Время напоминания","Введите время в формате ЧЧ:ММ (24-часовой формат)")
    if rem:
        try:
            hour=int(rem.split(":")[0])#разделили переменную  rem часы
            minute = int(rem.split(":")[1])#разделили переменную  rem на список и взяли [1] минуты
            now=datetime.datetime.now()
            print(now)
            dt=now.replace(hour=hour,minute=minute,second=0)
            print(dt)
            t=dt.timestamp()
            print(t)
        except ValueError:
            mb.showerror("Ошибка!","Неверный формат ввода")


def check():
    global t
    if t:
        now=time.time()
        print("Текущее время",now)
        if now>=t:
            play_snd()
            t=None
    window.after(10000,check)

def play_snd():
    pygame.mixer.init()
    pygame.mixer.music.load("rem.mp3")
    pygame.mixer.music.play()


t=None

window=Tk()
window.title("Напоминание со звуком")
label=Label(text="Установите напоминание")
label.pack()
set_button=Button(text="Установить напоминание", command=set)
set_button.pack()

check()
window.mainloop()
