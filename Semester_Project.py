import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.attributes('-fullscreen', True)
def exit_fullscreen(event=None):
    root.attributes('-fullscreen', False)
root.bind('<Escape>', exit_fullscreen)

root.title("ttk example")



label = ttk.Label(root, text="Shopping App and Log Analyzer", font=("Arial", 18))
label.place(x=5, y=5)

button = ttk.Button(root, text="Account", command=lambda:(show_account_screen(loginpage)))
button.place(x=1750, y=5)
def show_account_screen(loginpage)
    
button = ttk.Button(root, text="Exit", width=5, command=lambda: (exit_button_click(root)))
button.place(x=1860, y=5)
def exit_button_click(window):
    window.destroy()

style = ttk.Style(root)
style.configure('TButton', font=('Arial', 12), foreground='blue')

combo = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combo.pack(pady=30)

combo.set("Select an option")

def on_combobox_selected(event):
    selected_value = combo.get()
    print(f"Selected: {selected_value}")

combo.bind("<<ComboboxSelected>>", on_combobox_selected)
root.mainloop()