from matplotlib import pyplot as plt
from pandas import read_csv

data = read_csv('energies.csv').to_numpy()
pe = data[:,0]
ke = data[:,1]
e = data[:,2]

ts = []
t = 0
while t < 1:
    ts.append(t)
    t += 1e-3

plt.xticks()
plt.xlabel('t')
plt.ylabel('Energy/J')
plt.plot(ts, pe, label='Potential Energy')
plt.plot(ts, ke, label='Kinetic Energy')
plt.plot(ts, e, label='Mechanical Energy')
plt.legend()
plt.show()