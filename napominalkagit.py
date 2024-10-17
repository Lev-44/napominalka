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
            now=datetime.datetime.now()#получим текущую дату и время
            print(now)
            dt=now.replace(hour=hour,minute=minute,second=0)#мы к строке применили реплэйс и заменяем на наши заданные минуты и часы
            print(dt)#в строке время когда должен будет звонить таймер
            t=dt.timestamp()#преобразовываем в питоновскую дату милиарды секунд с 1970 года
            print(t)
        except ValueError:
            mb.showerror("Ошибка!","Неверный формат ввода")


def check():#проверка наступило ли время сработки
    global t#разрешаем менять та же что в коде
    if t:
        now=time.time()#текущее время
        print("Текущее время",now)
        if now>=t:# если  текущее время больше времени сработки
            play_snd()#музыка пошель
            t=None#сбрасываем таймер чтоб снова не сработал
    window.after(10000,check)#рекурсия сама себя проверяет через 10 сек вызывается check 10000 это delay

def play_snd():  #блок воспроизведения mp3файла в той же папке что и pyth файл
    pygame.mixer.init()
    pygame.mixer.music.load("rem.mp3")
    pygame.mixer.music.play()


t=None  #переменная в ней ничего нет

window=Tk()
window.title("Напоминание со звуком")
label=Label(text="Установите напоминание")
label.pack()
set_button=Button(text="Установить напоминание", command=set)
set_button.pack()

check()
window.mainloop()
