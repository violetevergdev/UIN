import tkinter as tk
from tkinter import ttk


def out(uin):
    root = tk.Tk()
    root.geometry('250x130')
    root.resizable(False, False)
    root.attributes("-topmost", True)
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.wm_geometry("+%d+%d" % (x, y))
    root.title("Генератор УИН")

    # Создание фреймов для разделения интерфейса
    output_frame = tk.Frame(root)
    output_frame.pack(pady=15)

    uin_label = tk.Label(output_frame, text="Ваш УИН: ", font=20)
    uin_label.pack()
    uin_entry = tk.Entry(output_frame, font=20, width=24, justify='center')
    uin_entry.insert(0, uin)
    uin_entry.pack()

    def copy():
        uin_entry.clipboard_clear()
        uin_entry.clipboard_append(uin_entry.get())

    copy_btn = ttk.Button(output_frame, text='Копировать', command=copy)
    copy_btn.pack(side=tk.BOTTOM, pady=15)

    tk.mainloop()