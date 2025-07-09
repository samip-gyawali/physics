from matplotlib import pyplot as plt
from numpy import random, sin

mass = 15 #kg
spring_constant = 1 #N/m
extension = 10 # m
x = extension
v = 0
timesteps = 100000
delta_t = 5e-3

ax = plt.gca()

for _ in range(timesteps):
    accel = -spring_constant * x
    x += v * delta_t + 1/2 * accel * (delta_t) ** 2
    v += accel * delta_t
    if _ % 500 == 0:
        plt.scatter(x, 0)
        plt.scatter(-extension, 0, s=0)
        plt.scatter(extension, 0, s=0)
        plt.plot([-extension, x], [0, 0])
        plt.title(f'Hooke\'s law with k = {spring_constant} N/m' )
        plt.savefig(f'./images/hooke/{int(_ / 500):06}.png')
        plt.clf()