from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = np.arange(-3, 3, 0.01)
Y = np.arange(-3, 3, 0.01)
X, Y = np.meshgrid(X, Y)

total1 = 0
total2 = 0
for i in range(1,6):
	total1 = total1 + i * np.cos((i + 1) * X + 1)
	total2 = total2 + i * np.cos((i + 1) * Y + 1)

Z = total1 * total2 * -1
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, alpha = 0.5,
                       linewidth=0, antialiased=False)
num_func_params = 3
num_swarm = 100
velocity = np.zeros([num_swarm, num_func_params])
position = -4 + 8 * np.random.rand(num_swarm, num_func_params)
personal_best_position = np.copy(position)
personal_best_value = np.zeros(num_swarm)

for b in range(num_swarm):
    total1 = 0
    total2 = 0
    for i in range(1,6):
        total1 = total1 + i * np.cos((i + 1) * position[i][0] + 1)
        total2 = total2 + i * np.cos((i + 1) * position[i][1] + 1)
    personal_best_value[b] = total1 * total2 * -1
    
tmax = 200
c1 = 0.001
c2 = 0.002
levels = np.linspace(-1, 35, 100)
global_best = np.min(personal_best_value)
global_best_position = np.copy(personal_best_position[np.argmin(personal_best_value)])
ax.set_autoscaley_on(False)
ax.set_ylim([-4,4])
ax.set_autoscalex_on(False)
ax.set_xlim([-4,4])
ax.set_autoscalez_on(False)
ax.set_zlim([-275,250])
for t in range (100):
    for i in range(num_swarm):
        total1 = 0
        total2 = 0
        for v in range(1,6):
            total1 = total1 + i * np.cos((v + 1) * position[i][0] + 1)
            total2 = total2 + i * np.cos((v + 1) * position[i][1] + 1)
        error = total1 * total2 * -1
        if personal_best_value[i] > error:
            personal_best_value[i] = error
            personal_best_position[i] = position[i]
    best = np.min(personal_best_value)
    best_index = np.argmin(personal_best_value)
    if global_best > best:
        global_best = best
        global_best_position = np.copy(personal_best_position[best_index])
    for i in range (num_swarm):
        velocity[i] += (c1 * np.random.rand() * (personal_best_position[i]-position[i]) \
                    +  c2 * np.random.rand() * (global_best_position - position[i]))		
        position[i] += velocity[i]
       
        ax.scatter(position[i][0],position[i][1],-0.5,color='green',s=20)
    ax.scatter(global_best_position[0], global_best_position[1],-0.5,color='red',s=50,zorder=1200)
   
    filename = 'frame{0:03d}.png'.format(t)
    plt.savefig(filename, bbox_inches='tight')
    ax.cla()
    ax.set_autoscaley_on(False)
    ax.set_ylim([-4,4])
    ax.set_autoscalex_on(False)
    ax.set_xlim([-4,4])
    ax.set_autoscalez_on(False)
    ax.set_zlim([-275,250])
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, alpha = 0.5,
                       linewidth=0, antialiased=False)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
