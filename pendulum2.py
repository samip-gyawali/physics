from math import sin, cos, pi
from matplotlib import pyplot as plt
import os, shutil

folder = './images/pendulum_2/'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

g = 9.8
L = 1
F = 20
m = 2
f = F/m
t = pi/4
w = 0
a = 0

def t_dot_dot(t):
    return  (-g/L * sin(t) - f/L * cos(t))

delta_t = 5e-4
timesteps = 10000
xs, ys = [L * sin(t)], [-L * cos(t)]

for i in range(timesteps):
    a = t_dot_dot(t)
    w += a * delta_t
    t += w * delta_t + 1/2 * a * (delta_t * delta_t)
    xs.append(L * sin(t))
    ys.append(-L * cos(t))
    if i % 100 == 0:
        plt.gca().set_xlim([- 2 * L, 2 * L])
        plt.gca().set_ylim([- 2 * L, 2 * L])
        plt.scatter(xs[-1], ys[-1])
        plt.plot([0, xs[-1]], [0, ys[-1]])
        plt.savefig(f'./images/pendulum_2/{int(i / 100):06}.png')
        plt.clf()