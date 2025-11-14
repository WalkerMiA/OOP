import tkinter as tk
from tkinter import ttk
from tkinter import *

class Stack:
    def __init__(self):
        self.element = []
    def push(self, x):
        self.element.append(x)
    def pop(self):
        self.element.pop()
    def displayStack(self):
        print("Elements in Stack:")
        for i in self.element:
            print(i)

def create_stack():
    global stack
    stack = Stack()
    output.config(text="Stack Created")

def add_to_stack():
    global stack
    x = valueTxt.get(1.0, "end-1c").strip()
    if x:
        stack.push(x)
        valueTxt.delete(1.0, tk.END)
        output.config(text=f"Added '{x}' to stack")
    else:
        output.config(text=f"Enter a value to add to stack")

def remove_from_stack():
    global stack
    if stack.element:
        removed = stack.pop()
        output.config(text=f"Removed '{removed}' from stack")

def display_stack():
    global stack
    if stack.element:
        output.config(text=f"Stack contents: {stack.element}")
    else:
        output.config(text="Stack is empty")


root = tk.Tk()
root.geometry("1280x720")

output = tk.Label(root, text="", anchor="w", justify="left")
output.place(x=200, y=350)

valueTxt = Text(width=25, height=1)
valueTxt.place(x=200, y=200)

createStack = ttk.Button(root, text="Create Stack", width=15, command=create_stack )
createStack.place(x=200, y=150)

addStack = ttk.Button(root, text="Add", width=10, command=add_to_stack)
addStack.place(x=400, y=200)

removeStack = ttk.Button(root, text="Remove From Stack", width=20, command=remove_from_stack)
removeStack.place(x=200, y=250)

showStack = ttk.Button(root, text="Display Stack", width=15, command=display_stack)
showStack.place(x=200, y=300)

root.mainloop()