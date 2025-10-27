import matplotlib.pyplot as plt
import numpy as np

x = np.array(["c1", "c2", "c3", "c4"])
y = np.array([80, 100, 62, 76])

print(np.mean(y))
print(np.median(y))
print(np.std(y))

plt.xlabel("Courses")
plt.ylabel("Grades")

plt.plot(x, y)
plt.show()