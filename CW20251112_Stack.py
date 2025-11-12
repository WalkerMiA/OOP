import tkinter as tk
from tkinter import ttk
from tkinter import *

class Stack:
    def __init__(self):
        self.element = []
    def push(self):
        self.element.append((text_Box.get(1.0, "end-1c")))
    def pop(self):
        self.element.pop()
    def displayStack(self):
        print("Elements in Stack:")
        for i in self.element:
            print(i)




s1 = Stack()
s1.push()
s1.displayStack()

root = tk.Tk()
root.geometry("1280x720")

text_Box = Text(width=25, height=1)
text_Box.place(x=200, y=200)

add_Button = ttk.Button(root, text="Add", width=10, command=lambda:())
add_Button.place(x=400, y=200)



root.mainloop()