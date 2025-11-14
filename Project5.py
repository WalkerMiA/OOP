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

class Queue:
    def __init__(self):
        self.element = []
    def enqueue(self, x):
        self.element.append(x)
    def dequeue(self):
        self.element.remove(0)
    def displayQueue(self):
        print("Elements in Queue:")
        for i in self.element:
            print(i)

#Functions for Stack
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
    #global stack
    if stack.element:
        removed = stack.element.pop(-1)
        output.config(text=f"Removed '{removed}' from stack")

def display_stack():
    global stack
    if stack.element:
        output.config(text=f"Stack contents: {stack.element}")
    else:
        output.config(text="Stack is empty")

#Functions for Queue
def create_queue():
    global queue
    queue = Queue()
    outputQueue.config(text="Queue Created")

def add_to_queue():
    global queue
    x = queueTxt.get(1.0, "end-1c").strip()
    if x:
        queue.enqueue(x)
        queueTxt.delete(1.0, tk.END)
        outputQueue.config(text=f"Added '{x}' to queue")
    else:
        outputQueue.config(text="Enter a value before adding")

def remove_from_queue():
    global queue
    if queue.element:
        removed = queue.element.pop(0)
        outputQueue.config(text=f"Removed '{removed}' from queue")
    else:
        outputQueue.config(text="Queue is empty")

def display_queue():
    global queue
    if queue.element:
        outputQueue.config(text=f"Queue contents: {queue.element}")
    else:
        outputQueue.config(text="Queue is empty")

#main
root = tk.Tk()
root.geometry("1280x720")

#Stack Buttons
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

#Queue buttons
outputQueue = tk.Label(root, text="", anchor="w", justify="left")
outputQueue.place(x=500, y=350)

queueTxt = Text(width=25, height=1)
queueTxt.place(x=500, y=200)

createQueue = ttk.Button(root, text="Create Queue", width=15, command=create_queue )
createQueue.place(x=500, y=150)

addQueue = ttk.Button(root, text="Add", width=10, command=add_to_queue)
addQueue.place(x=700, y=200)

removeQueue = ttk.Button(root, text="Remove From Queue", width=20, command=remove_from_queue)
removeQueue.place(x=500, y=250)

showQueue = ttk.Button(root, text="Display Queue", width=15, command=display_queue)
showQueue.place(x=500, y=300)

root.mainloop()