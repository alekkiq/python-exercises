import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-3*np.pi, 3*np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.figure(figsize=(6.4*3, 4.8))

plt.xticks(
    [-3*np.pi, -2*np.pi, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 2*np.pi, 3*np.pi], 
    [r'$-3\pi$', r'$-2\pi$', r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$2\pi$', r'$3\pi$'])

plt.yticks([-1, 0, 1])

plt.plot(X,C, color="green", linewidth=3, linestyle="--")
plt.plot(X,S, color="purple",  linewidth=3, linestyle="--")

plt.show()