import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.attributes('-fullscreen', True)
def exit_fullscreen(event=None):
    root.attributes('-fullscreen', False)
root.bind('<Escape>', exit_fullscreen)

root.title("ttk example")



label = ttk.Label(root, text="Hello, ttk!")
label.pack(side="top", fill="x", expand=True, pady=10)

button = ttk.Button(root, text="Account")
button.pack(side="top", pady=10)

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