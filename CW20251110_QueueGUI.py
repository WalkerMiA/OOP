import tkinter as tk
from tkinter import ttk
from tkinter import *

class Queue:
    def __init__(self):
        self.element = []
    def enqueue(self):
        x = valueTxt.get(1.0, "end-1c")
        self.element.append(x)
    def dequeue(self):
        self.element.remove(0)
    def displayQueue(self):
        print("Elements in Queue:")
        for i in self.element:
            print(i)







root = tk.Tk()
root.geometry("1280x720")

answer = Text(width=25, height=1)
answer.place(x=200, y=200)

createQueue = ttk.Button(root, text="Create Queue", width=15, command=lambda:() )
createQueue.place(x=200, y=150)

addQueue = ttk.Button(root, text="Add", width=10, command=lambda:())
addQueue.place(x=400, y=200)

removeQueue = ttk.Button(root, text="Remove From Queue", width=20, command=lambda:())
removeQueue.place(x=200, y=250)

showQueue = ttk.Button(root, text="Display Queue", width=15, command=lambda:())
showQueue.place(x=200, y=300)

root.mainloop()