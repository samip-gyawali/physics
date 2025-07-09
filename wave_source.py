from matplotlib import pyplot as plt
import os, shutil

class Source:
    sources = []
    waves = []
    t = 0
    def __init__(self, start: list[int, int], wavelength: float, frequency: float, velocity: tuple[int, int]) -> None:
        self.origin = start # (x,y)
        self.wavelength = wavelength # meter
        self.frequency = frequency # per second
        self.time_period = 1 / frequency if frequency != 0 else None
        self.speed = wavelength * frequency  # m/s
        self.velocity = velocity
        Wave(self)
        Source.sources.append(self)

    def timestep():
        ax.set_xlim([Source.sources[0].origin[0]-210, Source.sources[0].origin[0]+210])
        ax.set_ylim([Source.sources[0].origin[1]-205, Source.sources[0].origin[1]+205])
        delta_t = 5e-4 #s
        for wave in Source.waves:
            wave.radius += abs(wave.speed) * delta_t
            if wave.radius >= 200:
                Source.waves.remove(wave)

        for source in Source.sources:
            source.origin = [source.origin[0] + source.velocity[0] * delta_t, source.origin[1] + source.velocity[1] * delta_t]
            if abs((Source.t / source.time_period) - int(Source.t / source.time_period)) <= delta_t * 2:
                # create new wave
                Wave(source)

        Source.t += delta_t


class Wave:
    def __init__(self, source: Source, radius:float = 0.0) -> None:
        self.radius = radius
        self.source = source
        self.speed = source.speed
        self.origin = source.origin
        Source.waves.append(self)


ax = plt.gca()

def generate_circle(origin, radius):
    circle = plt.Circle(origin, radius, fill=False)
    ax.add_patch(circle)
        
folder = './images/waves/'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))


Source((0,0), 5, 100, (300, 0))
# Source((10,0), 5, 100, (150, 0))
timesteps = 10000

for i in range(timesteps):
    Source.timestep()
    if i % 10 == 0:
        for wave in Source.waves:
            generate_circle(wave.origin, wave.radius)
        for source in Source.sources:
            plt.scatter([source.origin[0]], [source.origin[1]], s=3)
        plt.savefig(f'./images/waves/{int(i/10):06}.png')
        plt.cla()