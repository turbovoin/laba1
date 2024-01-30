import tkinter as tk
from tkinter import messagebox
import customtkinter



def login():
    username = username_entry.get()
    password = password_entry.get()


    if username == "admin" and password == "password":

        login_window.destroy()

        create_main_window()
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль")



def create_main_window():
    main_window = customtkinter.CTk()
    main_window.title("Главное окно")


    logout_button = customtkinter.CTkButton(main_window, text="Выйти", command=main_window.destroy)
    logout_button.pack(pady=10)


    main_window.mainloop()



login_window = customtkinter.CTk()
login_window.title("Вход в систему")


username_label = customtkinter.CTkLabel(login_window, text="Логин:")
username_label.pack()
username_entry = customtkinter.CTkEntry(login_window)
username_entry.pack(pady=10)

password_label = customtkinter.CTkLabel(login_window, text="Пароль:")
password_label.pack()
password_entry = customtkinter.CTkEntry(login_window, show="*")
password_entry.pack(pady=10)


login_button = customtkinter.CTkButton(login_window, text="Войти", command=login)
login_button.pack(pady=10)


login_window.mainloop()