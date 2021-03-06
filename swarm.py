import numpy as np
import matplotlib
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

# Make data.
X = np.arange(-3, 3, 0.01)
Y = np.arange(-3, 3, 0.01)
X, Y = np.meshgrid(X, Y)
#declaring z value
Z = -((1.0+np.cos(12.0*np.sqrt((X**2.0)+(Y**2.0))))/(0.5*((X**2)+(Y**2))+2))

num_func_params = 2
num_swarm = 100
position = -3 + 6 * np.random.rand(num_swarm, num_func_params)
temp = -3 + 6 * np.random.rand(num_swarm, num_func_params)
velocity = np.zeros([num_swarm, num_func_params])
personal_best_position = np.copy(position)
personal_best_value = np.zeros(num_swarm)

for i in range(num_swarm):
    # Z = (1-X)**2 + 1 *(Y-X**2)**2
    #personal_best_value[i] = (1 - position[i][0]) ** 2 + 1 * (position[i][1] - position[i][0] ** 2) ** 2
	personal_best_value[i] = -((1.0+np.cos(12.0*np.sqrt((position[i][0]**2.0)+(position[i][1]**2.0))))/(0.5*((position[i][0]**2)+(position[i][1]**2))+2))
	
tmax = 200
c1 = 0.001
c2 = 0.002
levels = np.linspace(-1, 35, 100)
global_best = np.min(personal_best_value)
global_best_position = np.copy(personal_best_position[np.argmin(personal_best_value)])

for t in range(tmax):
	for i in range(num_swarm):
		error = -((1.0+np.cos(12.0*np.sqrt((position[i][0]**2.0)+(position[i][1]**2.0))))/(0.5*((position[i][0]**2)+(position[i][1]**2))+2))
		if personal_best_value[i] > error:
			personal_best_value[i] = error
			personal_best_position[i] = position[i]
	best = np.min(personal_best_value)
	best_index = np.argmin(personal_best_value)
	if global_best < best:
		global_best = best
		global_best_position = np.copy(personal_best_position[best_index])

	for i in range(num_swarm):
        # update velocity
		velocity[i] += c1 * np.random.rand() * (personal_best_position[i] - position[i]) \
						+ c2 * np.random.rand() * (global_best_position - position[i])
		temp[i] = position[i]
		position[i] += velocity[i]

 
	fig = plt.figure()

	CS = plt.contour(X, Y, Z, levels=levels, cmap=cm.gist_stern)
	plt.gca().set_xlim([-3, 3])
	plt.gca().set_ylim([-3, 3])
    # setting color
	fig.colorbar(CS, shrink=0.5, aspect=5)

	for i in range(num_swarm):
		ax = plt.axes()
		ax.arrow(temp[i][0],temp[i][1], position[i][0]-temp[i][0], position [i][1]-temp[i][1], head_width=0.2, head_length=0.1, zorder=100)
		plt.plot(position[i][0], position[i][1], 'go')
	plt.plot(global_best_position[0], global_best_position[1], 'ro')

	plt.title('{0:03d}'.format(t))
	filename = 'frame{0:03d}.png'.format(t)
	plt.savefig(filename, bbox_inches='tight')
	plt.close(fig)