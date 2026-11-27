
import numpy as np
import matplotlib.pyplot as plt

# 1. Create x and y values
x = np.linspace(-5, 5, 30)
y = np.linspace(-5, 5, 30)

X, Y = np.meshgrid(x, y)

# 2. Define the function
Z = X**2 + Y**2

# 3. Calculate gradient
FX = 2 * X
FY = 2 * Y

# 4. Create 3D figure
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 5. Plot surface
ax.plot_surface(
    X, Y, Z,
    cmap='viridis',
    alpha=0.8
)

# 6. Plot gradient arrows
ax.quiver(
    X[::4, ::4],
    Y[::4, ::4],
    Z[::4, ::4],
    FX[::4, ::4],
    FY[::4, ::4],
    np.zeros_like(FX[::4, ::4]),
    color='red',
    length=0.15,
    normalize=True
)

# 7. Labels
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z = f(x,y)")

ax.set_title("3D Surface with Gradient Arrows")

plt.show()



# Gradient Descent for f(x) = x^2

def gradient_descent(x, learning_rate, iterations):

    for i in range(iterations):

        gradient = 2 * x

        x = x - learning_rate * gradient

        print(f"Iteration {i+1}: x = {x:.6f}, f(x) = {x**2:.6f}")

    return x


result = gradient_descent(
    x=10,
    learning_rate=0.1,
    iterations=20
)

print("Minimum point:", result)
