import tkinter as tk
import os


class MainWindow:

    def __init__(self, master):
        self.master = master
        master.title("Заметки")
        self.create_button = tk.Button(master, text="Создать заметку", command=self.create_note)
        self.create_button.pack(pady=10)
        self.view_button = tk.Button(master, text="Просмотреть все заметки", command=self.view_notes)
        self.view_button.pack(pady=10)


def create_note(self):
    self.note_window = tk.Toplevel(self.master)
    self.note_window.title("Новая заметка")
    self.note_label = tk.Label(self.note_window, text="Введите заметку:")
    self.note_label.pack()
    self.note_text = tk.Text(self.note_window, height=10, width=50)
    self.note_text.pack(padx=10, pady=10)
    self.save_button = tk.Button(self.note_window, text="Сохранить", command=self.save_note)
    self.save_button.pack(side=tk.LEFT, padx=10)
    self.cancel_button = tk.Button(self.note_window, text="Отменить", command=self.note_window.destroy)
    self.cancel_button.pack(side=tk.RIGHT, padx=10)


def save_note(self):
    note_text = self.note_text.get("1.0", "end-1c")
    note_num = len([name for name in os.listdir() if name.endswith(".txt")])
    note_name = f"note{note_num}.txt"
    with open(note_name, "w") as note_file:
        note_file.write(note_text)

    self.note_window.destroy()


def view_notes(self):
    self.notes_window = tk.Toplevel(self.master)
    self.notes_window.title("Все заметки")
    self.notes_listbox = tk.Listbox(self.notes_window, height=10, width=50)
    self.notes_listbox.pack(padx=10, pady=10)
    for note_name in os.listdir():
        if note_name.endswith(".txt"):
            self.notes_listbox.insert(tk.END, note_name)

    self.view_button = tk.Button(self.notes_window, text="Просмотреть", command=self.view_note)
    self.view_button.pack(side=tk.LEFT, padx=10)
    self.edit_button = tk.Button(self.notes_window, text="Редактировать", command=self.edit_note)
    self.edit_button.pack(side=tk.LEFT, padx=10)
    self.delete_button = tk.Button(self.notes_window, text="Удалить", command=self.delete_note)
    self.delete_button.pack(side=tk.LEFT, padx=10)


def view_note(self):
    selected_note = self.notes_listbox.get(tk.ACTIVE)


    with open(selected_note, "r") as note_file:
        note_text = note_file.read()
    self.view_window = tk.Toplevel(self.master)
    self.view_window.title(selected_note)
    note_label = tk.Label(self.view_window, text=note_text)
    note_label.pack(padx=10, pady=10)


def edit_note(self):
    selected_note = self.notes_listbox.get(tk.ACTIVE)
    with open(selected_note, "r") as note_file:
        note_text = note_file.read()

    self.edit_window = tk.Toplevel(self.master)
    self.edit_window.title(f"Редактирование {selected_note}")
    self.note_label = tk.Label(self.edit_window, text="Отредактируйте заметку:")
    self.note_label.pack()

    self.note_text = tk.Text(self.edit_window, height=10, width=50)
    self.note_text.insert(tk.END, note_text)
    self.note_text.pack(padx=10, pady=10)

    self.save_button = tk.Button(self.edit_window, text="Сохранить", command=lambda: self.save_edited(selected_note))
    self.save_button.pack(side=tk.LEFT, padx=10)
    self.cancel_button = tk.Button(self.edit_window, text="Отменить", command=self.edit_window.destroy)
    self.cancel_button.pack(side=tk.RIGHT, padx=10)


def save_edited(self, note_name):
    note_text = self.note_text.get("1.0", "end-1c")


    with open(note_name, "w") as note_file:
        note_file.write(note_text)
    self.edit_window.destroy()


def delete_note(self):
    selected_note = self.notes_listbox.get(tk.ACTIVE)
    os.remove(selected_note)
    self.notes_listbox.delete(tk.ACTIVE)

root = tk.Tk()
app = MainWindow(root)
root.mainloop()
