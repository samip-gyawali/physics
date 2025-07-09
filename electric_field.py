from numpy import random
from matplotlib import pyplot as plt

class Charge():
    charges = []
    x_pos = random.uniform(-1e3, 1e3, 500)
    y_pos = random.uniform(-1e3, 1e3, 500)
    k = 9e9 # Nm^2/
    E = [[0, 0] for _ in range(100)]  # Field Strengths
    def __init__(self, pos: list[float, float], charge: float, velocity: list[float, float], mass) -> None:
        self.pos = pos
        self.charge = charge
        self.vel = velocity
        self.opos = pos
        self.ovel = velocity
        self.mass = mass

        Charge.charges.append(self)

    def timestep():
        delta_t = 5e-2
        Charge.E = [[0, 0] for _ in range(len(Charge.x_pos))] # reset
        for i, x in enumerate(Charge.x_pos):
            y = Charge.y_pos[i]
            for charge in Charge.charges:
                c_x = charge.opos[0]
                c_y = charge.opos[1]
                dist = ((x - c_x) ** 2 + (y - c_y) ** 2) ** 0.5
                fs = (Charge.k * charge.charge)/(dist) ** 3
                Charge.E[i][0] += fs * (x - c_x)
                Charge.E[i][1] += fs * (y - c_y)

        for charge in Charge.charges:
            for other in Charge.charges:
                if other != charge:
                    dist = ((charge.pos[0] - other.pos[0]) ** 2 + (charge.pos[1] - other.pos[1]) ** 2) ** 0.5
                    accel = Charge.k * other.charge * charge.charge / (charge.mass * dist ** 3 )
                    a_x = accel * (charge.pos[0] - other.pos[0])
                    a_y = accel * (charge.pos[1] - other.pos[1])
                    charge.pos[0] += charge.ovel[0] * delta_t + 1 / 2 * a_x * (delta_t) ** 2
                    charge.pos[1] += charge.ovel[1] * delta_t + 1 / 2 * a_y * (delta_t) ** 2
                    charge.vel[0] += a_x * delta_t
                    charge.vel[1] += a_y * delta_t

        for charge in Charge.charges:
            charge.opos = charge.pos
            charge.ovel = charge.vel


c1 = Charge([-9e2, 9e2], 1e-15, [1, -1], 1e-5)
c2 = Charge([9e2, 0], -1e-15, [-1, 0], 1e-5)
c2 = Charge([0, 0], -1e-18, [-1, 0], 1e-5)
timesteps = 50000
ax = plt.gca()


for _ in range(timesteps):
    Charge.timestep()
    if _ % 100 == 0:
        for i, x in enumerate(Charge.x_pos):
            y = Charge.y_pos[i]
            E_x = Charge.E[i][0]
            E_y = Charge.E[i][1]
            plt.quiver(x, y, E_x, E_y, color='red')

        for charge in Charge.charges:
            plt.scatter([charge.pos[0]], [charge.pos[1]])

        plt.savefig(f'./images/charge/{int(_ / 100):06}.png')
        plt.clf()