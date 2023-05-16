import tkinter as tk  # библиотека для создания граф. приложений
from tkinter import *
from tkinter import messagebox

def getLoginPassword(): #Объявляем функцию.
    login = str(login_tf.get()) #С помощью метода .get получаем из поля ввода с именем login_tf, которое ввёл пользователь и конвертируем строку.
    password = str(password_tf.get()) #С помощью метода .get получаем из поля ввода с именем password_tf, которое ввёл пользователь и конвертируем строку.
   
    if (login == "admin" and password == "123"):
        messagebox.showinfo('Success', f'Доступ разрешен!')
    else:
        messagebox.showerror('Fail', f'Доступ запрещен!')


window = Tk()  # Создаём окно приложения.
window.title("Tortotoro")  # Добавляем название приложения.
window.geometry("500x500")  # Размер окна


frame = Frame(
    window,  # Обязательный параметр, который указывает окно для размещения Frame.
    padx=10,  # Задаём отступ по горизонтали.
    pady=10,  # Задаём отступ по вертикали.
)


frame.pack(expand=True)  # Не забываем позиционировать виджет в окне. Здесь используется метод pack. С помощью свойства expand=True указываем, что Frame заполняет весь контейнер, созданный для него.



login_lb = Label(frame, text="Login:  ")
login_lb.grid(row=3, column=1)  # 3я строка, 1й столбец

password_lb = Label(frame, text="Password:  ", pady=10)
password_lb.grid(row=4, column=1)

login_tf = Entry(
    frame,  # Используем нашу заготовку с настроенными отступами.
)
login_tf.grid(row=3, column=2)

password_tf = Entry(
    frame,  # Используем нашу заготовку с настроенными отступами.
)
password_tf.grid(row=4, column=2)



authorization_btn = Button(
    frame,  # Заготовка с настроенными отступами.
    text="Next",  # Надпись на кнопке.
    command=getLoginPassword,
    padx=30,  # Задаём отступ по горизонтали

)
authorization_btn.grid(row=5, column=2)  # Размещаем кнопку в ячейке, расположенной ниже, чем наши надписи, но во втором столбце, то есть под ячейками для ввода информации.

   
window.mainloop()  # Запуск цикла событий (окно не будет закрываться)
