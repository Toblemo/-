import sqlite3
import tkinter as tk
from tkinter import ttk

class Main_Window():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x750")
        self.root.title("Электронный журнал")

        # Логотип по центру экрана
        self.logo = tk.PhotoImage(file="book.png")
        self.label = tk.Label(self.root, image=self.logo)
        self.label.pack(anchor='center', expand=1)

        self.main_menu = tk.Menu()
        self.file_menu = tk.Menu(tearoff=0)
        self.ref_menu = tk.Menu(tearoff=0)
        self.nomer_menu = tk.Menu(tearoff=0)
        self.otch_menu = tk.Menu(tearoff=0)
        self.help_menu = tk.Menu(tearoff=0)

        self.file_menu.add_command(label="Выход", command=quit)
        self.ref_menu.add_command(label="Журнал", command=self.open_abonents_window)
        self.ref_menu.add_command(label="Группы")
        self.nomer_menu.add_command(label='Дисциплины')
        self.nomer_menu.add_command(label='Преподаватели')
        self.nomer_menu.add_command(label='Студенты')
        self.otch_menu.add_command(label="Сформировать отчёт")
        self.help_menu.add_command(label="Руководство пользователя")
        self.help_menu.add_command(label="О программе")

        self.main_menu.add_cascade(label="Файл", menu=self.file_menu)
        self.main_menu.add_cascade(label="Справочники", menu=self.ref_menu)
        self.main_menu.add_cascade(label="Перечень данных", menu=self.nomer_menu)
        self.main_menu.add_cascade(label="Отчеты", menu=self.otch_menu)
        self.main_menu.add_cascade(label="Справка", menu=self.help_menu)

        self.root.config(menu=self.main_menu)

    def open_abonents_window(self):
        self.root.withdraw()
        Abonents_Window()

class Abonents_Window():
    def __init__(self):
        self.root2 = tk.Tk()
        self.root2.geometry("920x500")
        self.root2.title("Электронный журнал / Записи")
        self.root2.protocol('WM_DELETE_WINDOW', lambda: self.quit_abonents_window())
        self.main_view = win
        self.db = db

        self.table_frame = tk.Frame(self.root2, bg='blue')
        self.add_edit_frame = tk.Frame(self.root2, bg='red')

        self.table_frame.place(relx=0, rely=0, relheight=1, relwidth=0.6)
        self.add_edit_frame.place(relx=0.6, rely=0, relheight=1, relwidth=0.4)

        self.table_abonents = ttk.Treeview(self.table_frame, columns=('discipline_mark', 'date_ofcompletion', 'pass'),
                                           height=15, show='headings')
        self.table_abonents.column("discipline_mark", width=200, anchor=tk.NW)
        self.table_abonents.column("date_ofcompletion", width=200, anchor=tk.NW)
        self.table_abonents.column("pass", width=120, anchor=tk.CENTER)

        self.table_abonents.heading("discipline_mark", text='Оценка')
        self.table_abonents.heading("date_ofcompletion", text='Дата проведения занятия')
        self.table_abonents.heading("pass", text='Отметка о пропуске')

        self.scroll_bar = ttk.Scrollbar(self.table_frame)
        self.table_abonents['yscrollcommand'] = self.scroll_bar.set
        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

        self.table_abonents.place(relx=0, rely=0, relheight=0.9, relwidth=0.97)

        self.esearch = ttk.Entry(self.table_frame)
        self.esearch.place(relx=0.02, rely=0.92, relheight=0.05, relwidth=0.7)

        self.butsearch = tk.Button(self.table_frame, text="Найти")
        self.butsearch.place(relx=0.74, rely=0.92, relheight=0.05, relwidth=0.2)

        self.lname = tk.Label(self.add_edit_frame, text="Оценка")
        self.lname.place(relx=0.04, rely=0.02, relheight=0.05, relwidth=0.4)
        self.ename = ttk.Entry(self.add_edit_frame)
        self.ename.place(relx=0.45, rely=0.02, relheight=0.05, relwidth=0.5)

        self.laddress = tk.Label(self.add_edit_frame, text="Дата проведения занятия")
        self.laddress.place(relx=0.04, rely=0.12, relheight=0.05, relwidth=0.4)
        self.eaddress = ttk.Entry(self.add_edit_frame)
        self.eaddress.place(relx=0.45, rely=0.12, relheight=0.05, relwidth=0.5)

        self.lphone = tk.Label(self.add_edit_frame, text="Отметка о пропуске")
        self.lphone.place(relx=0.04, rely=0.22, relheight=0.05, relwidth=0.4)

        self.ephone = ttk.Entry(self.add_edit_frame)
        self.ephone.place(relx=0.45, rely=0.22, relheight=0.05, relwidth=0.5)

        self.butadd = tk.Button(self.add_edit_frame, text="Добавить запись")
        self.butadd.place(relx=0.1, rely=0.33, relheight=0.07, relwidth=0.8)

        self.butdel = tk.Button(self.add_edit_frame, text="Удалить запись")
        self.butdel.place(relx=0.1, rely=0.44, relheight=0.07, relwidth=0.8)

        self.buted = tk.Button(self.add_edit_frame, text="Редактировать запись")
        self.buted.place(relx=0.1, rely=0.55, relheight=0.07, relwidth=0.8)

        self.butsave = tk.Button(self.add_edit_frame, text="Сохранить изменения")
        self.butsave.place(relx=0.1, rely=0.66, relheight=0.07, relwidth=0.8)

        self.butquit = tk.Button(self.add_edit_frame, text="Закрыть")
        self.butquit.place(relx=0.1, rely=0.77, relheight=0.07, relwidth=0.8)

    def quit_abonents_window(self):
        self.root2.destroy()
        self.main_view.root.deiconify()

class DB:
    def __init__(self):
        self.conn = sqlite3.connect('journal_directory.db')
        self.c = self.conn.cursor()
        self.create_table_abonents()
        self.conn.commit()

    def create_table_abonents(self):
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS "records" (
                   "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                   "discipline_mark" TEXT NOT NULL,
                   "date_ofcompletion" TEXT NOT NULL,
                   "middle_name" TEXT,
                   "pass" INTEGER
                   )'''
        )

db = DB()
win = Main_Window()
win.root.mainloop()

