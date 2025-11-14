import tkinter as tk
from tkinter import ttk
from tkinter import *

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

def create_queue():
    global queue
    queue = Queue()
    output.config(text="Queue Created")

def add_to_queue():
    global queue
    x = valueTxt.get(1.0, "end-1c").strip()
    if x:
        queue.enqueue(x)
        valueTxt.delete(1.0, tk.END)
        output.config(text=f"Added '{x}' to queue")
    else:
        output.config(text="Enter a value before adding")

def remove_from_queue():
    global queue
    if queue.element:
        removed = queue.element.pop(0)
        output.config(text=f"Removed '{removed}' from queue")
    else:
        output.config(text="Queue is empty")

def display_queue():
    global queue
    if queue.element:
        output.config(text=f"Queue contents: {queue.element}")
    else:
        output.config(text="Queue is empty")

root = tk.Tk()
root.geometry("1280x720")

output = tk.Label(root, text="", anchor="w", justify="left")
output.place(x=200, y=350)

valueTxt = Text(width=25, height=1)
valueTxt.place(x=200, y=200)

createQueue = ttk.Button(root, text="Create Queue", width=15, command=create_queue )
createQueue.place(x=200, y=150)

addQueue = ttk.Button(root, text="Add", width=10, command=add_to_queue)
addQueue.place(x=400, y=200)

removeQueue = ttk.Button(root, text="Remove From Queue", width=20, command=remove_from_queue)
removeQueue.place(x=200, y=250)

showQueue = ttk.Button(root, text="Display Queue", width=15, command=display_queue)
showQueue.place(x=200, y=300)

root.mainloop()