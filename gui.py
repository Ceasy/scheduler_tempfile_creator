import tkinter as tk
import py7zr
import shutil
import os
from tkinter import ttk, messagebox
from scheduler import TaskScheduler
from constants import TEMP_DEST_PATH, ZIP_NAME, TXT_NAME


def create_temp_file(username, content):
    file_path = os.path.join(TEMP_DEST_PATH.format(username), TXT_NAME)
    with open(file_path, "w") as file:
        file.write(content)
    return file_path


class AppGui:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("Creator temp pass")

        self.app.iconbitmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ico', 'ico.ico'))
        self.app.resizable(False, False)

        frame = ttk.Frame(self.app, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Username:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.username_entry = ttk.Entry(frame)
        self.username_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(frame, text="Password ZIP:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.password_entry = ttk.Entry(frame)
        self.password_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(frame, text=".txt file content:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.content_text = tk.Text(frame, height=10, width=40)
        self.content_text.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(frame, text="ZIP File lifetime(day):").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.lifetime_entry = ttk.Entry(frame)
        self.lifetime_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5)

        ttk.Button(frame, text="Start", command=self.start_process).grid(row=5, column=0, columnspan=2, pady=20)

    def start_process(self):
        username = self.username_entry.get()
        zip_password = self.password_entry.get()
        content = self.content_text.get("1.0", tk.END).strip()
        lifetime = int(self.lifetime_entry.get())

        temp_file_path = create_temp_file(username, content)

        with py7zr.SevenZipFile(ZIP_NAME, mode='w', password=zip_password) as archive:
            archive.write(temp_file_path, TXT_NAME)

        os.remove(temp_file_path)

        dest_path = os.path.join(TEMP_DEST_PATH.format(username), ZIP_NAME)

        print(dest_path)
        shutil.move(ZIP_NAME, dest_path)

        TaskScheduler.create_task(username, lifetime)

        messagebox.showinfo("Успешно", "Файл и задача успешно созданы!")

    def run(self):
        self.app.mainloop()
