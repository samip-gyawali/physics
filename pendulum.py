from math import sin, cos, pi
from matplotlib import pyplot as plt
import os, shutil

delta_t = 1e-3
timesteps = 8000

L = 2
g = 9.8
m = 2
t = pi/3
w = 0
a = - g/L * sin(t)

PE = []
KE = []
E = []

xs, ys = [], []

folder = './images/pendulum/'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))


for _ in range(timesteps):
    xs.append(L * sin(t))
    ys.append(-L * cos(t))
    PE.append(m * g * (L - L * cos(t)))
    KE.append(1/2 * m * (w * L) ** 2)
    E.append(PE[-1] + KE[-1])
    t += (w * delta_t + 1/2 * a * delta_t ** 2)
    w += (a * delta_t)
    a = - g/L * sin(t)
    if _ % 50 == 0:
        plt.gca().set_xlim([- 2 * L, 2 * L])
        plt.gca().set_ylim([- 2 * L, 2 * L])
        plt.plot([0,xs[-1]], [0, ys[-1]])
        plt.scatter([xs[-1]], [ys[-1]], color='red')
        plt.savefig(f'./images/pendulum/{int(_ / 50):06}.png', dpi=500)
        plt.clf()

with open('energies.txt', 'w') as write_file:
    write_file.write('PE, KE, E\n')
    for i, pe in enumerate(PE):
        write_file.write(f'{pe}, {KE[i]}, {E[i]}\n')