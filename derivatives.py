# import sympy as sp
# x = sp.symbols('x')
# y = (2*x + 5)**3
# dy = sp.diff(y, x)
# print(dy)

import sympy as sp

x = sp.symbols('x')

functions = [
    (2*x + 5)**3,
    (x**2 + 3)**4,
    sp.sin(3*x + 2),
    sp.exp(x**2 + 1),
    sp.sqrt(5*x**2 + 4)
]

for i, f in enumerate(functions, 1):
    print(f"Q{i}: {sp.diff(f, x)}")



# Partial derivatives
import sympy as sp

x, y = sp.symbols('x y')

f = x**2 + 3*x*y + y**2

# Partial derivative with respect to x
fx = sp.diff(f, x)

# Partial derivative with respect to y
fy = sp.diff(f, y)

print("Partial w.r.t x:", fx)
print("Partial w.r.t y:", fy)