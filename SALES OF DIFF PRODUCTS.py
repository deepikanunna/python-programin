import matplotlib.pyplot as plt
X = [1, 2, 3, 4, 5]
Y = [2, 4, 1, 3, 7]
plt.scatter(X, Y, color='purple', marker='o')
plt.title("Scatter Plot of X vs Y")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.show()