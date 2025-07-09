from numpy import sin, cos
from matplotlib import pyplot as plt
import os, shutil

folder = './images/2-D/'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

r = [1, 1]
v = [0, 0]
k = [9, 4]
m = 1

xs = [r[0]]
ys = [r[1]]

timesteps = 200000
delta_t = 5e-4
img_t = 500

for i in range(timesteps):
    a = [- k[0] * r[0]/m, -k[1] * r[1]/m]
    r[0] += v[0] * delta_t + 1/2 * a[0] * delta_t ** 2
    r[1] += v[1] * delta_t + 1/2 * a[1] * delta_t ** 2
    v[0] += a[0] * delta_t
    v[1] += a[1] * delta_t
    xs.append(r[0])
    ys.append(r[1])

    if i % img_t == 0:
        plt.plot(xs, ys)
        plt.scatter(r[0], r[1])
        plt.savefig(f'./images/2-D/{int(i // img_t):06}.png')
        plt.clf()