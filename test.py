from matplotlib import pyplot as plt
from numpy import random, array

ax = plt.gca()

radius = 5

ax.set_xlim([-(radius + 1), radius + 1])
ax.set_ylim([-(radius), radius])

circle = plt.Circle((0, 0), 5, fill = False)

plt.gca().add_patch(circle)
plt.clf()
ax.set_xlim([-(radius + 1), radius + 1])
ax.set_ylim([-(radius), radius])
plt.gca().add_patch(circle)
plt.show()