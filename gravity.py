from matplotlib import pyplot as plt
import os, shutil

class Planet(object):
    planets = []
    G = 6.67e-11 # Nm^2/kg^2
    delta_t = 100

    def __init__(self, mass, x, y, z, vx, vy, vz):
        self.mass = mass
        self.x = x
        self.y = y
        self.z = z
        self.ox = x
        self.oy = y
        self.oz = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.ovx = vx
        self.ovy = vy
        self.ovz = vz
        Planet.planets.append(self)

    def update():
        delta_t = Planet.delta_t
        for planet in Planet.planets:
            a_x, a_y, a_z = 0, 0, 0
            for other in Planet.planets:
                if other != planet:
                    dist = ((planet.ox - other.ox) ** 2 + (planet.oy - other.oy) ** 2 + (planet.oz - other.oz) ** 2) ** 0.5
                    accel = (Planet.G * other.mass) / dist ** 3
                    a_x += accel * (other.ox - planet.ox)
                    a_y += accel * (other.oy - planet.oy)
                    a_z += accel * (other.oz - planet.oz)

            planet.x += planet.ovx * delta_t + 1/2 * a_x * (delta_t) ** 2
            planet.y += planet.ovy * delta_t + 1/2 * a_y * (delta_t) ** 2
            planet.z += planet.ovz * delta_t + 1/2 * a_z * (delta_t) ** 2
            planet.vx += a_x * delta_t
            planet.vy += a_y * delta_t
            planet.vz += a_z * delta_t

        for planet in Planet.planets:
            planet.ox = planet.x
            planet.oy = planet.y
            planet.oz = planet.z
            planet.ovx = planet.vx
            planet.ovy = planet.vy
            planet.ovz = planet.vz

folder = './images/gravity/'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))


Sun = Planet(2e30, 0, 0, 0, 0, 0, 0)
Mercury = Planet(3.3e23, 49902000000, 0, 0, 0, 47e3, 0)
Venus = Planet(4.9e24, 0, 107820000000, 0, -35e3, 0, 0)
Earth = Planet(6e24, 1.5e11, 0, 0, 0, 29722.2222, 0)
Mars = Planet(6.4e23, 208640000000, 0, 0, 0, -24130.772, 0)

timesteps = 1000000

coords = [[[planet.x], [planet.y], [planet.z]] for planet in Planet.planets]
count = 0
for _ in range(timesteps):
    Planet.update()
    for i, planet in enumerate(Planet.planets):
        coords[i][0].append(planet.x)
        coords[i][1].append(planet.y)
        coords[i][2].append(planet.z)
    
    if _ % 10000 == 0:
        for i in range(len(Planet.planets)):
            plt.plot(coords[i][0], coords[i][1])
            plt.scatter([coords[i][0][-1]], [coords[i][1][-1]])
        plt.savefig(f'./images/gravity/{count:06}.png', dpi=700)
        count += 1
        plt.clf()

os.system("ffmpeg -r 60 -s 1080x1620 -i images/gravity/%06d.png -vcodec libx264 -crf 25 gravity.mp4")