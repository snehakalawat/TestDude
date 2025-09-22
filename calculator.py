import tkinter as tk
from tkinter import messagebox


def click(event):
    try:
        text = event.widget.cget("text")
        if text == "=":
            try:
                result = eval(str(entry.get()))
                entry_var.set(result)
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
                entry_var.set("")
        elif text == "C":
            entry_var.set("")
        else:
            entry_var.set(entry_var.get() + text)
    except Exception as e:
        messagebox.showerror("Error", str(e))



root = tk.Tk()
root.title("Tkinter Calculator")
root.geometry("300x400")
root.resizable(False, False)


entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 18", justify="right")
entry.pack(fill="x", ipadx=8, ipady=8, pady=10)


buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]


frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(side="top", expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(row_frame, text=btn_text, font="Arial 16", width=5, height=2)
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        btn.bind("<Button-1>", click)


root.mainloop()
