from sympy import solve, symbols
import numpy as np

# 8.1.1
print('8.1.1')

# v)
# 2x - 3y = 5
# 7x + y = 3
x, y = symbols('x, y')

print(f"v) {solve([
    2*x - 3*y - 5,
    7*x + y - 3
])}")

# a)
# 2x + 3y = 11
# 7x - y = 4
x, y = symbols('x, y')

print(f"a) {solve([
    2*x + 3*y - 11,
    7*x - y - 4
])}")

# 8.1.2
print("\n8.1.2")

# v)
# 3x - y + 5z = 2
# 7x + 2y + 3z = 9
# 4x + y - 7z = 5
x, y, z = symbols('x, y, z')

print(f"v) {solve([
    3*x - y + 5*z - 2,
    7*x + 2*y + 3*z - 9,
    4*x + y - 7*z - 5
])}")

# a)
# 2x + y - 3z = 5
# -3x - y + 2z = -7
# 5x + 2y - 4z = 12
x, y, z = symbols('x, y, z')

print(f"a) {solve([
    2*x + y - 3*z - 5,
    -3*x - y + 2*z + 7,
    5*x + 2*y - 4*z - 12
])}")

# 8.1.3
print("\n8.1.3")

# v1)
# x + y + z = 3
# 2x + y - z = 2
# 4x + 3y + z = 5
x, y, z = symbols('x, y, z')

det = np.linalg.det([
    [1, 1, 1],
    [2, 1, -1],
    [4, 3, 1]
])

print(f"v1) Determinantti on {det}, ei ratkaisua")

# v2)
# x + y + z = 3
# 2x + y - z = 2
# 4x + 3y + z = 8
x, y, z = symbols('x, y, z')

det = np.linalg.det([
    [1, 1, 1],
    [2, 1, -1],
    [4, 3, 1]
])

print(f"v2) {solve([
    x + y + z - 3,
    2*x + y - z - 2,
    4*x + 3*y + z - 8
])}")

# a)
# 2x + y - 3z = 5
# -3x - y + 2z = -7
# 5x + 2y - 5z = 12
x, y, z = symbols('x, y, z')

det = np.linalg.det([
    [2, 1, -3],
    [-3, -1, 2],
    [5, 2, -5]
])

print(f"a) {solve([
    2*x + y - 3*z - 5,
    -3*x - y + 2*z + 7,
    5*x + 2*y - 5*z - 12
])}")

# b)
# 2x + y - 3z = 5
# -3x - y + 2z = -7
# 5x + 2y - 5z = 11
x, y, z = symbols('x, y, z')

det = np.linalg.det([
    [2, 1, -3],
    [-3, -1, 2],
    [5, 2, -5]
])

print(f"b) Determinantti on {det}, ei ratkaisua")
print(solve([
    2*x + y - 3*z - 5,
    -3*x - y + 2*z + 7,
    5*x + 2*y - 5*z - 11
]))