import tkinter as tk
from time import sleep
try:
    root = tk.Tk()
    root.title("__JARVIS__")
    root.attributes("-topmost", True)
    label = tk.Label(root, text="Loading...")
    label.pack()

    while True:
        with open(r"guicomms.txt", "rt") as file:
            text12 = file.read()
            if "<null>" in text12:
                root.destroy()
            else:
                label.config(text=text12)
        root.update()

        if not root.winfo_exists():
            break
except tk.TclError:
    pass
