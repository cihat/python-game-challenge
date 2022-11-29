from tkinter import messagebox


def show_alert(type, title, message):
    if type == "info":
        messagebox.showinfo(title, message)
    elif type == "warning":
        messagebox.showwarning(title, message)
    elif type == "error":
        messagebox.showerror(title, message)
    else:
        print("Invalid type")
