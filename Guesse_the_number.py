from tkinter import *
from tkinter import messagebox
import random


def win():
    try:
        item = int(txt.get())
        if item < 0 or item > 10:
            messagebox.showwarning('WRONG', "Ошибка")
            label.config(text="Ты ввел некоректное число\nВведи число от 0 до 10")
        elif item != number:
            if messagebox.askyesno('GAME OVER', "Не угадал :(\nХочешь попробовать еще раз?"):
                label.config(text=random.choice(['У тебя все получится!', 'Ты молодец!\nУпорству тебе не занимать!',
                                                 'Только великие идут до конца!', 'Дорогу осилит идущий']))
            else:
                label.config(text="Спасибо за игру!\nЖду тебя еще раз ;)")
                label.pack(ipadx=100, ipady=100)
                txt.destroy()
                btn.destroy()
        else:
            label.config(text="Ты победил! Поздравляю!\nЖду тебя еще раз ;)")
            label.pack(ipadx=100, ipady=100)
            txt.destroy()
            btn.destroy()
    except ValueError:
        messagebox.showwarning('WRONG', "Ошибка")
        label.config(text="Ты ввел неккоректный символ\nВведи число от 0 до 10")


number = random.randrange(11)
window = Tk()
window.geometry('800x300')
window.title("Игра 'Угадай число'")
label = Label(window, text="Привет! Это игра 'Угадай число'.\nДля тебя загадано число от 0 до 10.\nПопробуй угадать ;)",
              font=("Arial Bold", 30))
label.pack(anchor="center", ipadx=10, ipady=10)
txt = Entry(window, width=20, font=("Arial Bold", 20))
txt.pack(anchor="center", ipadx=10, ipady=10)
btn = Button(window, text="Ответ", font=("Arial Bold", 20), bg="black", fg="white", command=win)
btn.pack(anchor="center", ipadx=10, ipady=10)
window.mainloop()