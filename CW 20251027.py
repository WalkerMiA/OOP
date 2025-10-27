import matplotlib.pyplot as plt
import numpy as np
import tkinter

'''x = np.array(["c1", "c2", "c3", "c4"])
y = np.array([80, 100, 62, 76])

print(np.mean(y))
print(np.median(y))
print(np.std(y))

plt.xlabel("Courses")
plt.ylabel("Grades")

plt.plot(x, y)
plt.show()

mylabels = ["a1", "a2", "a3", "a4"]
plt.pie(y, labels=mylabels)
plt.show()

x = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
y = [25, 39, 50, 20, 68, 34, 83, 44, 96, 10]
plt.scatter(x, y)
plt.show()'''

root = tkinter.Tk()
root.resizable(False, False)

myCanvas = tkinter.Canvas(root, bg="white", height = 720, width = 1280)

shape1 = myCanvas.create_oval(20,20,100,100, fill="blue")
'''shape2 = myCanvas.create_arc(150, 150, 100, 100, start=270, extent=180, style=tkinter.ARC, outline="purple", width=10)'''
shape3 = myCanvas.create_oval(40, 40, 500, 500, fill="red")

xx =yy = 3
def move_shape1():
    global xx, yy
    #move the shape with the constanct xx, yy
    myCanvas.move(shape1, xx, yy)
    #get the current coordinates of the shape
    (x1, y1, x2, y2) = myCanvas.coords(shape1)
    #check the boundaries of the coordinates and change the constants xx, yy
    if x1 <= 0 or x2 >= 1280:
        xx = -xx
    if y1 <= 0 or y2 >= 720:
        yy = -yy
    #call the function recursively
    myCanvas.after(30, move_shape1)

def move_shape3():
    global xx, yy
    # move the shape with the constanct xx, yy
    myCanvas.move(shape3, xx, yy)
    # get the current coordinates of the shape
    (x1, y1, x2, y2) = myCanvas.coords(shape3)
    # check the boundaries of the coordinates and change the constants xx, yy
    if x1 <= 0 or x2 >= 1280:
        xx = -xx
    if y1 <= 0 or y2 >= 720:
        yy = -yy
    # call the function recursively
    myCanvas.after(30, move_shape3)

#in the main program call the function move_shape()
myCanvas.after(10,move_shape1())
myCanvas.after(10, move_shape3())
myCanvas.pack()
root.mainloop()
